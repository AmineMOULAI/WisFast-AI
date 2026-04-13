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

    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown(f"""
        <div class="bolt-container" style="margin-bottom: 2rem;">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/lightning-bolt.png" style="width:30px;">
            <span class="bolt-text" style="font-size: 1.5rem; color: white; margin-left:10px;">WisFast AI</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="sidebar-section-header">Navigation</div>', unsafe_allow_html=True)
        if st.button("🏠 Home Feed", width='stretch', key="nav_home"):
            st.session_state.selected_book_id = None
            st.session_state.search_query = ""
            st.switch_page("Home.py")
        
        st.markdown('<div class="sidebar-section-header">Recent Research</div>', unsafe_allow_html=True)
        all_history = repo.get_all_search_history(limit=5)
        if not all_history:
            st.caption("No recent threads.")
        for h in all_history:
            h_col1, h_col2 = st.columns([5, 1])
            with h_col1:
                if st.button(f"🔍 {h['query'][:20]}...", key=f"side_h_{h['id']}", width='stretch'):
                    st.session_state.selected_book_id = h['book_id']
                    st.session_state.search_query = h['query']
                    st.rerun()
            with h_col2:
                if st.button("🗑️", key=f"del_h_{h['id']}", help="Delete thread"):
                    repo.delete_search_history(h['id'])
                    st.rerun()

        st.markdown('<div class="sidebar-section-header">Knowledge Library</div>', unsafe_allow_html=True)
        books = repo.get_books()
        if not books:
            st.caption("Library is empty.")
        for b in books:
            b_col1, b_col2 = st.columns([5, 1])
            with b_col1:
                if st.button(f"📄 {b['display_name'][:20]}", width='stretch', key=f"side_b_{b['id']}"):
                    st.session_state.selected_book_id = b['id']
                    st.session_state.search_query = ""
                    st.rerun()
            with b_col2:
                if st.button("🗑️", key=f"del_b_{b['id']}", help="Remove book"):
                    repo.delete_book(b['id'])
                    if st.session_state.selected_book_id == b['id']:
                        st.session_state.selected_book_id = None
                    st.rerun()

    # --- MAIN CONTENT AREA ---
    current_book = repo.get_book(st.session_state.selected_book_id) if st.session_state.selected_book_id else None
    query = st.session_state.search_query
    
    # If no book is selected, show the HERO view
    if not current_book:
        logo_base64 = get_image_as_base64("assets/bolt.png")
        st.markdown(f"""
            <div class="hero-container fade-in">
                <img src="data:image/png;base64,{logo_base64}" class="hero-bolt">
                <h1 style='font-size: 4rem; font-family: "Squada One", cursive; color: white; margin: 0;'>
                    WISFAST ENGINE
                </h1>
                <p style="color: #a0aec0; font-size: 1.4rem; max-width: 600px; margin-bottom: 1rem;">
                    Upload a research paper or choose from your library to start your intelligent search experience.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Center uploader in hero
        _, uploader_col, _ = st.columns([1, 2, 1])
        with uploader_col:
            st.markdown('<div class="hero-uploader">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Drop your PDF here", type=["pdf"], key="hero_uploader")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        # We have a book, show search results or prompt
        st.markdown('<div class="main-content-container fade-in">', unsafe_allow_html=True)
        
        header_text = f"Research in: {current_book['display_name']}"
        st.markdown(f"<h3 style='font-family: \"Squada One\", cursive; color: #4ecdc4; margin-bottom: 2rem;'>{header_text}</h3>", unsafe_allow_html=True)

        if query:
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
            st.info("Ready! Use the search bar below to ask questions about this document.")

        st.markdown('</div>', unsafe_allow_html=True)

        # --- FIXED BOTTOM ACTION BAR (Only shown when book is selected) ---
        st.markdown('<div class="bottom-bar-fixed">', unsafe_allow_html=True)
        st.markdown('<div class="action-bar-pill">', unsafe_allow_html=True)
        
        bar_col1, bar_col2 = st.columns([1, 15])
        
        with bar_col1:
            st.markdown('<div class="compact-uploader">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader("+", type=["pdf"], label_visibility="collapsed", key="bar_uploader")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with bar_col2:
            def handle_search():
                st.session_state.search_query = st.session_state.new_query_input
                if st.session_state.search_query and current_book:
                    repo.add_search_history(current_book['id'], st.session_state.search_query)

            st.text_input(
                "Search",
                placeholder=f"Search in {current_book['display_name']}...",
                label_visibility="collapsed",
                key="new_query_input",
                on_change=handle_search
            )

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
                    st.rerun()
            finally:
                if os.path.exists(temp_pdf_path):
                    os.remove(temp_pdf_path)


if __name__ == "__main__":
    run()
