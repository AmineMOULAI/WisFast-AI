import streamlit as st
import os
import time
import uuid
import base64
from typing import List
from wisfast.data.sqlite_repository import SQLiteRepository
from wisfast.services.pdf_processor import PDFProcessor
from wisfast.services.text_preprocessor import TextPreprocessor
from wisfast.services.index_manager import TfidfIndexManager
from wisfast.services.search_strategies import TfidfSemanticStrategy, SearchResult
from wisfast.ui.styles import apply_custom_styles
from components.footer import footer

def get_image_as_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

def run():
    st.set_page_config(page_title="WisFast Engine", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")
    apply_custom_styles()
    
    repo = SQLiteRepository()
    preprocessor = TextPreprocessor()
    index_manager = TfidfIndexManager()
    search_strategy = TfidfSemanticStrategy(index_manager, preprocessor)
    
    # Initialize state
    if "selected_book_id" not in st.session_state:
        st.session_state.selected_book_id = None
    if "is_uploading" not in st.session_state:
        st.session_state.is_uploading = False
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""
    if "show_uploader" not in st.session_state:
        st.session_state.show_uploader = False

    # --- SIDEBAR ---
    # ... (sidebar code remains the same)

    # --- MAIN CONTENT AREA ---
    current_book = repo.get_book(st.session_state.selected_book_id) if st.session_state.selected_book_id else None
    query = st.session_state.search_query
    
    # Hero / Upload file container (Shared logic for hero bar or book-page toggle)
    uploaded_file = None

    if not current_book:
        # HERO STATE
        logo_base64 = get_image_as_base64("assets/bolt.png")
        st.markdown(f"""
            <div class="hero-container fade-in">
                <img src="data:image/png;base64,{logo_base64}" class="hero-bolt">
                <h1 style='font-size: 4rem; font-family: "Squada One", cursive; color: white; margin: 0;'>
                    WISFAST ENGINE
                </h1>
                <p style="color: #a0aec0; font-size: 1.4rem; max-width: 600px; margin-bottom: 0.5rem;">
                    Your intelligent research companion.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="hero-bar-uploader">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload a PDF to start searching", type=["pdf"], key="hero_bar_uploader")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # BOOK STATE
        st.markdown('<div class="main-content-container fade-in">', unsafe_allow_html=True)
        
        # Animated uploader panel (toggled by + button in bottom bar)
        panel_class = "visible" if st.session_state.show_uploader else ""
        st.markdown(f'<div class="uploader-panel {panel_class}"><div class="panel-content">', unsafe_allow_html=True)
        # Use a normal uploader in this panel
        uploaded_file = st.file_uploader("Select a new PDF document", type=["pdf"], key="panel_uploader")
        st.markdown('</div></div>', unsafe_allow_html=True)

        if query:
            header_text = f"Research in: {current_book['display_name']}"
            st.markdown(f"<h3 style='font-family: \"Squada One\", cursive; color: #4ecdc4; margin-bottom: 2rem;'>{header_text}</h3>", unsafe_allow_html=True)
            
            with st.spinner("Sourcing..."):
                results = search_strategy.search(query, current_book['id'], k=5)
            
            if results:
                for r in results:
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="doc-badge">PAGE {r.page_number} &nbsp; | &nbsp; {r.relevance_percent}% Match</div>
                        <p style="font-size:1.15rem; line-height:1.8; color: #ffffff; margin-bottom: 1rem;">{r.snippet}</p>
                        <details style="cursor:pointer; color:#a0aec0; font-size: 0.9rem;">
                            <summary>Show source text</summary>
                            <div class="source-text-block">
                                {r.raw_text}
                            </div>
                        </details>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No exact matches found. Try broad keywords.")
        else:
            st.markdown(f"""
                <div style="text-align: center; margin-top: 25vh; opacity: 0.5;">
                    <p style="color: #a0aec0; font-family: 'Squada One', cursive; letter-spacing: 2px;">
                        READY TO SEARCH IN: {current_book['display_name'].upper()}
                    </p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # --- SHARED FIXED BOTTOM ACTION BAR ---
    st.markdown('<div class="bottom-bar-fixed">', unsafe_allow_html=True)
    st.markdown('<div class="action-bar-pill">', unsafe_allow_html=True)
    
    # Conditional + button based on page state
    if current_book:
        # Use a clickable div/button to toggle the uploader panel
        # Streamlit buttons don't easily allow custom HTML wrapping for specific animations,
        # but we can use st.button and style it to look like our request.
        btn_col, search_col = st.columns([1, 4])
        with btn_col:
            if st.button("➕ Add new book", key="toggle_upload_btn", use_container_width=True):
                st.session_state.show_uploader = not st.session_state.show_uploader
                st.rerun()
        with search_col:
            def handle_search():
                if st.session_state.new_query_input:
                    st.session_state.search_query = st.session_state.new_query_input
                    repo.add_search_history(current_book['id'], st.session_state.search_query)
                    st.session_state.show_uploader = False # Hide uploader if searching

            st.text_input(
                "Search",
                placeholder=f"Ask anything about {current_book['display_name']}...",
                label_visibility="collapsed",
                key="new_query_input",
                on_change=handle_search
            )
    else:
        # Hero state: simple text input as placeholder or just leave it blank if hero bar uploader is used
        st.markdown('<p style="color:rgba(255,255,255,0.3); margin:0;">Upload a document above to unlock search.</p>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

    # File processing logic
    if uploaded_file:
        with st.status(f"Indexing {uploaded_file.name}...", expanded=True) as status:
            temp_pdf_path = f"temp_{uuid.uuid4()}.pdf"
            book_id = str(uuid.uuid4())
            with open(temp_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            try:
                def extraction_callback(current, total):
                    status.write(f"Extracting page {current} of {total}...")
                    return False

                pages_text = PDFProcessor.extract_pages(temp_pdf_path, callback=extraction_callback)
                if pages_text:
                    db_pages = []
                    for pt in pages_text:
                        db_pages.append({
                            'page_number': pt.page_number,
                            'raw_text': pt.raw_text,
                            'cleaned_text': preprocessor.clean(pt.raw_text)
                        })
                    repo.create_book(book_id, uploaded_file.name, uploaded_file.name.replace('.pdf', ''), len(db_pages))
                    repo.save_pages(book_id, db_pages)
                    index_manager.ensure_index(book_id)
                    
                    status.update(label="✅ Index Ready!", state="complete")
                    st.session_state.selected_book_id = book_id
                    st.session_state.search_query = ""
                    st.session_state.show_uploader = False
                    st.rerun()
            finally:
                if os.path.exists(temp_pdf_path):
                    os.remove(temp_pdf_path)


if __name__ == "__main__":
    run()
