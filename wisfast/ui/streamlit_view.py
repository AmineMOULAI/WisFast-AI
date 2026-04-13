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
    st.set_page_config(page_title="WisFast Engine", page_icon="⚡", layout="wide")
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

    # --- MAIN CONTENT ---
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # 1. Top Section
    col_t1, col_t2, col_t3 = st.columns([1, 6, 1])
    
    with col_t2:
        # Logo above header
        logo_base64 = get_image_as_base64("assets/bolt.png")
        if logo_base64:
            st.markdown(f"""
                <div style="text-align: center; margin-top: 1rem;">
                    <img src="data:image/png;base64,{logo_base64}" class="bolt-animated" style="width: 250px;">
                </div>
            """, unsafe_allow_html=True)

        current_book = repo.get_book(st.session_state.selected_book_id) if st.session_state.selected_book_id and st.session_state.selected_book_id != "UPLOAD" else None
        
        header_text = f"Research in: {current_book['display_name']}" if current_book else "What do you want to know?"
        st.markdown(f"<h1 style='text-align: center; margin-top: 1rem; font-size: 3rem;'>{header_text}</h1>", unsafe_allow_html=True)
        
        # Action Bar
        search_col, upload_col = st.columns([6, 1], gap="small")
        with search_col:
            placeholder = "Ask anything..." if not current_book else f"Search in {current_book['display_name']}..."
            query = st.text_input("Search", value=st.session_state.search_query, placeholder=placeholder, label_visibility="collapsed", key="main_search_input")
        with upload_col:
            if st.button("➕", width='stretch', help="Upload new PDF"):
                st.session_state.selected_book_id = "UPLOAD"
                st.rerun()

    # 2. Results Area
    if st.session_state.selected_book_id == "UPLOAD":
        st.markdown("---")
        st.markdown("### Add New Knowledge")
        uploaded_file = st.file_uploader("Drop your PDF here", type=["pdf"], label_visibility="collapsed")
        
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
                        st.rerun()
                finally:
                    if os.path.exists(temp_pdf_path):
                        os.remove(temp_pdf_path)
    
    elif query:
        st.markdown("---")
        search_target_id = st.session_state.selected_book_id if current_book else (books[0]['id'] if books else None)
        
        if not search_target_id:
            st.warning("Please upload a document to begin searching.")
        else:
            if st.session_state.search_query != query:
                repo.add_search_history(search_target_id, query)
                st.session_state.search_query = query
                
            with st.spinner("Sourcing..."):
                results = search_strategy.search(query, search_target_id, k=5)
            
            if results:
                for r in results:
                    st.markdown(f"""
                    <div class="result-card">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                            <div class="doc-badge">PAGE {r.page_number}</div>
                            <span style="color: #4ecdc4; font-weight:700;">{r.relevance_percent}% Match</span>
                        </div>
                        <p style="font-size:1.1rem; line-height:1.7; color: #ffffff;">{r.snippet}</p>
                        <details style="cursor:pointer; margin-top:15px; color:#a0aec0;">
                            <summary>Show source text</summary>
                            <div class="source-text-block">
                                {r.raw_text}
                            </div>
                        </details>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No matches found.")
    
    else:
        if not current_book:
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown("""
            <div style='text-align: center; opacity: 0.6;'>
                <h3>Select a book from the sidebar to start a deep-dive research session.</h3>
                <p>Or use the search bar above to query your library globally.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("---")
            st.info(f"Book: {current_book['display_name']} | Pages: {current_book['page_count']} indexed.")
            if st.button("🗑️ Forget this Book", type="secondary"):
                repo.delete_book(current_book['id'])
                st.session_state.selected_book_id = None
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    footer()
