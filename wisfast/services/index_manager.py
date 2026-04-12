import os
import pickle
from typing import Tuple, Optional, List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from wisfast.config import MODELS_DIR, MAX_FEATURES, NGRAM_RANGE
from wisfast.data.sqlite_repository import SQLiteRepository

class TfidfIndexManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TfidfIndexManager, cls).__new__(cls)
            cls._instance.cache = {}
            cls._instance.repo = SQLiteRepository()
        return cls._instance
        
    def _get_paths(self, book_id: str) -> Tuple[str, str]:
        vec_path = os.path.join(MODELS_DIR, f"{book_id}_vectorizer.pkl")
        mat_path = os.path.join(MODELS_DIR, f"{book_id}_matrix.pkl")
        return vec_path, mat_path

    def ensure_index(self, book_id: str):
        vec_path, mat_path = self._get_paths(book_id)
        
        if os.path.exists(vec_path) and os.path.exists(mat_path):
            return

        pages = self.repo.get_pages(book_id)
        if not pages:
            return

        cleaned_texts = [p['cleaned_text'] for p in pages]
        
        vectorizer = TfidfVectorizer(max_features=MAX_FEATURES, ngram_range=NGRAM_RANGE)
        matrix = vectorizer.fit_transform(cleaned_texts)
        
        with open(vec_path, 'wb') as f:
            pickle.dump(vectorizer, f)
        with open(mat_path, 'wb') as f:
            pickle.dump(matrix, f)
            
        # Update cache
        self.cache[book_id] = (vectorizer, matrix, pages)

    def get_index(self, book_id: str) -> Tuple[Optional[TfidfVectorizer], Any, List[Dict[str, Any]]]:
        if book_id in self.cache:
            return self.cache[book_id]
            
        vec_path, mat_path = self._get_paths(book_id)
        if not os.path.exists(vec_path) or not os.path.exists(mat_path):
            return None, None, []
            
        with open(vec_path, 'rb') as f:
            vectorizer = pickle.load(f)
        with open(mat_path, 'rb') as f:
            matrix = pickle.load(f)
            
        pages = self.repo.get_pages(book_id)
        self.cache[book_id] = (vectorizer, matrix, pages)
        
        return vectorizer, matrix, pages