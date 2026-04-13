import pytest
import os
import sqlite3
import uuid
from wisfast.data.sqlite_repository import SQLiteRepository
from wisfast.services.text_preprocessor import TextPreprocessor
from wisfast.services.index_manager import TfidfIndexManager
from wisfast.services.search_strategies import TfidfSemanticStrategy, ResultRanker

@pytest.fixture
def temp_db():
    db_name = "test_wisfast.db"
    repo = SQLiteRepository(db_path=db_name)
    yield repo
    if os.path.exists(db_name):
        os.remove(db_name)

def test_repo_create_and_get_book(temp_db):
    book_id = str(uuid.uuid4())
    temp_db.create_book(book_id, "test.pdf", "Test Book", 10)
    
    book = temp_db.get_book(book_id)
    assert book is not None
    assert book['display_name'] == "Test Book"
    assert book['page_count'] == 10

def test_repo_save_and_get_pages(temp_db):
    book_id = str(uuid.uuid4())
    temp_db.create_book(book_id, "test.pdf", "Test Book", 2)
    
    pages = [
        {'page_number': 1, 'raw_text': "Page 1 content", 'cleaned_text': "page 1 content"},
        {'page_number': 2, 'raw_text': "Page 2 content", 'cleaned_text': "page 2 content"}
    ]
    temp_db.save_pages(book_id, pages)
    
    retrieved_pages = temp_db.get_pages(book_id)
    assert len(retrieved_pages) == 2
    assert retrieved_pages[0]['raw_text'] == "Page 1 content"

def test_text_preprocessor_french():
    preprocessor = TextPreprocessor()
    # Test French specific cleaning
    text = "L'éducation est le mouvement de l'obscurité à la lumière."
    cleaned = preprocessor.clean(text)
    
    # Check if key content words are present
    assert "mouvement" in cleaned
    assert "lumière" in cleaned
    assert "est" not in cleaned.split()

def test_result_ranker_snippet():
    query_tokens = ["patience", "virtue"]
    raw_text = "This is a long text where patience is considered a great virtue in many cultures."
    # Use a larger snippet length to ensure we catch the relevant parts
    snippet = ResultRanker.extract_snippet(query_tokens, raw_text, snippet_length=50)
    
    assert "patience" in snippet.lower()
    assert "virtue" in snippet.lower()

def test_search_integration(temp_db):
    # Setup index manager and preprocessor
    preprocessor = TextPreprocessor()
    index_manager = TfidfIndexManager()
    # Override repo in index manager for testing
    index_manager.repo = temp_db
    
    book_id = "search_test_id"
    temp_db.create_book(book_id, "search.pdf", "Search Test", 3)
    
    pages = [
        {'page_number': 1, 'raw_text': "Le bonheur est une vertu.", 'cleaned_text': preprocessor.clean("Le bonheur est une vertu.")},
        {'page_number': 2, 'raw_text': "La sagesse est la clé.", 'cleaned_text': preprocessor.clean("La sagesse est la clé.")},
        {'page_number': 3, 'raw_text': "Le courage face au danger.", 'cleaned_text': preprocessor.clean("Le courage face au danger.")}
    ]
    temp_db.save_pages(book_id, pages)
    
    # Force indexing
    index_manager.ensure_index(book_id)
    
    # Test search
    strategy = TfidfSemanticStrategy(index_manager, preprocessor)
    results = strategy.search("sagesse", book_id, k=1)
    
    assert len(results) > 0
    assert results[0].page_number == 2
    assert results[0].relevance_percent > 0
