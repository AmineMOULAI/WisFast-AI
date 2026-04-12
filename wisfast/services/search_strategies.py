from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import issparse
import numpy as np
from wisfast.services.text_preprocessor import TextPreprocessor

@dataclass
class SearchResult:
    page_number: int
    score: float
    raw_text: str
    relevance_percent: int
    snippet: str

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query: str, book_id: str, k: int = 5) -> List[SearchResult]:
        pass

class ResultRanker:
    @staticmethod
    def extract_snippet(query_tokens: List[str], raw_text: str, snippet_length: int = 50) -> str:
        words = raw_text.split()
        if not words:
            return ""
        
        # Simple snippet extraction: find first match
        lower_words = [w.lower() for w in words]
        best_idx = 0
        for token in query_tokens:
            try:
                best_idx = lower_words.index(token)
                break
            except ValueError:
                continue
                
        start_idx = max(0, best_idx - snippet_length // 2)
        end_idx = min(len(words), start_idx + snippet_length)
        snippet = " ".join(words[start_idx:end_idx])
        
        if start_idx > 0:
            snippet = "..." + snippet
        if end_idx < len(words):
            snippet = snippet + "..."
            
        return snippet

    @staticmethod
    def rank_results(scores: np.ndarray, pages: List[Dict[str, Any]], query_tokens: List[str], k: int = 5) -> List[SearchResult]:
        top_indices = np.argsort(scores)[::-1][:k]
        results = []
        for idx in top_indices:
            score = float(scores[idx])
            if score <= 0:
                continue
            
            page = pages[idx]
            relevance = int(round(score * 100))
            snippet = ResultRanker.extract_snippet(query_tokens, page['raw_text'])
            
            results.append(SearchResult(
                page_number=page['page_number'],
                score=score,
                raw_text=page['raw_text'],
                relevance_percent=relevance,
                snippet=snippet
            ))
        return results

class TfidfSemanticStrategy(SearchStrategy):
    def __init__(self, index_manager, preprocessor: TextPreprocessor):
        self.index_manager = index_manager
        self.preprocessor = preprocessor

    def search(self, query: str, book_id: str, k: int = 5) -> List[SearchResult]:
        vectorizer, matrix, pages = self.index_manager.get_index(book_id)
        if not vectorizer or not issparse(matrix) or matrix.nnz == 0 or not pages:
            return []

        cleaned_query = self.preprocessor.clean(query)
        if not cleaned_query:
            return []
            
        query_vector = vectorizer.transform([cleaned_query])
        similarities = cosine_similarity(query_vector, matrix).flatten()
        
        query_tokens = cleaned_query.split()
        return ResultRanker.rank_results(similarities, pages, query_tokens, k)