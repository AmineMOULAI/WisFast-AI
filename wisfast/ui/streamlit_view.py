import streamlit as st
import os
import time
import uuid
from typing import List
from wisfast.data.sqlite_repository import SQLiteRepository
from wisfast.services.pdf_processor import PDFProcessor
from wisfast.services.text_preprocessor import TextPreprocessor
from wisfast.services.index_manager import TfidfIndexManager
from wisfast.services.search_strategies import TfidfSemanticStrategy, SearchResult
from wisfast.ui.styles import apply_custom_styles

def run():
    st.set_page_config(page_title="wisFast AI", page_icon="⚡", layout="wide")
    apply_custom_styles()
    
    # Initialize services
    repo = SQLiteRepository()
    preprocessor = TextPreprocessor()
    index_manager = TfidfIndexManager()
    search_strategy = TfidfSemanticStrategy(index_manager, preprocessor)
    
    # Sidebar
    with st.sidebar:
        st.image("assets/WisFast.png", width='stretch')
        st.markdown("---")
        st.header("📚 Your Library")
        
        books = repo.get_books()
        book_options = {b['id']: b['display_name'] for b in books}
        
        if not book_options:
            st.info("No books yet. Upload one to get started!")
            selected_book_id = None
        else:
            selected_book_id = st.selectbox(
                "Select a book to search",
                options=list(book_options.keys()),
                format_func=lambda x: book_options[x]
            )
            
        st.markdown("---")
        st.caption("WisFast AI v1.0")

    # Hero Section
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    col_h1, col_h2 = st.columns([2, 1])
    with col_h1:
        st.title("WisFast AI")
        st.markdown("### Smart research in your books. ⚡")
        st.write("Stop wasting hours on Ctrl+F. Get precise answers from your PDFs in seconds.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # Upload & Search Tabs
    tab_search, tab_upload = st.tabs(["🔍 Search", "📤 Upload"])
    
    with tab_upload:
        st.subheader("Add to your library")
        uploaded_file = st.file_uploader("Drop your PDF here", type=["pdf"])
        
        if uploaded_file is not None:
            file_name = uploaded_file.name
            if not any(b['file_name'] == file_name for b in books):
                if "is_uploading" not in st.session_state:
                    st.session_state.is_uploading = False

                if not st.session_state.is_uploading:
                    if st.button(f"Start Processing {file_name}", width='stretch'):
                        st.session_state.is_uploading = True
                        st.session_state.stop_upload = False
                        st.rerun()
                else:
                    with st.status(f"Processing {file_name}...", expanded=True) as status:
                        # Save uploaded file temporarily
                        temp_pdf_path = f"temp_{uuid.uuid4()}.pdf"
                        with open(temp_pdf_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        try:
                            stop_placeholder = st.empty()
                            if stop_placeholder.button("⏹️ Stop Process", key="stop_upload_btn"):
                                st.session_state.stop_upload = True
                                st.session_state.is_uploading = False

                            def extraction_callback(current, total):
                                if st.session_state.get("stop_upload", False):
                                    return True
                                status.write(f"Extracting page {current} of {total}...")
                                return False

                            st.write("Extracting text...")
                            processor = PDFProcessor()
                            pages_text = processor.extract_pages(temp_pdf_path, callback=extraction_callback)

                            if st.session_state.get("stop_upload", False):
                                status.update(label="❌ Process stopped by user.", state="error", expanded=False)
                                st.warning("Upload cancelled.")
                                st.session_state.is_uploading = False
                                return

                            if pages_text:
                                st.write("Preprocessing and indexing...")
                                db_pages = []
                                for pt in pages_text:
                                    if st.session_state.get("stop_upload", False): break
                                    cleaned = preprocessor.clean(pt.raw_text)
                                    db_pages.append({
                                        'page_number': pt.page_number,
                                        'raw_text': pt.raw_text,
                                        'cleaned_text': cleaned
                                    })

                                if not st.session_state.get("stop_upload", False):
                                    repo.create_book(book_id, file_name, file_name.replace('.pdf', ''), len(db_pages))
                                    repo.save_pages(book_id, db_pages)
                                    index_manager.ensure_index(book_id)

                                    status.update(label=f"✅ {file_name} indexed!", state="complete", expanded=False)
                                    st.success(f"Success! {len(db_pages)} pages are now searchable.")
                                    time.sleep(1)
                                    st.session_state.is_uploading = False
                                    st.rerun()
                            else:
                                st.error("Could not extract text from this PDF.")
                                st.session_state.is_uploading = False
                        finally:
                            if os.path.exists(temp_pdf_path):
                                os.remove(temp_pdf_path)
            else:
                st.info("This book is already in your library.")
    with tab_search:
        if not selected_book_id:
            st.warning("Please upload or select a book first.")
        else:
            search_col1, search_col2 = st.columns([4, 1])
            with search_col1:
                query = st.text_input("Search query", placeholder="What are you looking for today?", label_visibility="collapsed")
            with search_col2:
                search_btn = st.button("Search", width='stretch')
            
            if query or search_btn:
                if not query:
                    st.toast("Please enter a query first!")
                else:
                    with st.spinner("Searching through pages..."):
                        results = search_strategy.search(query, selected_book_id, k=5)
                        
                    if not results:
                        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
                        st.warning("No matches found. Try different keywords.")
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f"#### Found {len(results)} relevant pages")
                        # Display results in a grid (2 columns)
                        for i in range(0, len(results), 2):
                            cols = st.columns(2)
                            for j in range(2):
                                if i + j < len(results):
                                    r = results[i + j]
                                    with cols[j]:
                                        with st.container(border=True):
                                            st.metric(label=f"PAGE {r.page_number}", value=f"{r.relevance_percent}%")
                                            st.markdown("**Snippet:**")
                                            st.markdown(f"_{r.snippet}_")
                                            with st.expander("Read Full Page"):
                                                st.write(r.raw_text)
                            st.markdown(" ") # Spacer
    
    # Footer (can be imported from components if needed)
    st.markdown("---")
    st.caption("Built with ❤️ for UPVD")