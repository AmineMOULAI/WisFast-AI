import sqlite3
from typing import List, Dict, Any, Optional
import os
from datetime import datetime
from wisfast.config import DB_PATH

class SQLiteRepository:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id TEXT PRIMARY KEY,
                    file_name TEXT NOT NULL,
                    display_name TEXT NOT NULL,
                    page_count INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id TEXT NOT NULL,
                    page_number INTEGER NOT NULL,
                    raw_text TEXT NOT NULL,
                    cleaned_text TEXT NOT NULL,
                    FOREIGN KEY (book_id) REFERENCES books(id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS search_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id TEXT NOT NULL,
                    query TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (book_id) REFERENCES books(id)
                )
            ''')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_book_page ON pages(book_id, page_number)')
            conn.commit()

    def add_search_history(self, book_id: str, query: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO search_history (book_id, query) VALUES (?, ?)', (book_id, query))
            conn.commit()

    def get_search_history(self, book_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM search_history WHERE book_id = ? ORDER BY timestamp DESC LIMIT ?', (book_id, limit))
            return [dict(row) for row in cursor.fetchall()]

    def get_all_search_history(self, limit: int = 20) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT sh.*, b.display_name 
                FROM search_history sh 
                JOIN books b ON sh.book_id = b.id 
                ORDER BY sh.timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cursor.fetchall()]

    def delete_search_history(self, history_id: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM search_history WHERE id = ?', (history_id,))
            conn.commit()

    def delete_book(self, book_id: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Delete history, pages and then the book itself
            cursor.execute('DELETE FROM search_history WHERE book_id = ?', (book_id,))
            cursor.execute('DELETE FROM pages WHERE book_id = ?', (book_id,))
            cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()

    def create_book(self, book_id: str, file_name: str, display_name: str, page_count: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO books (id, file_name, display_name, page_count, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (book_id, file_name, display_name, page_count, datetime.now().isoformat(), datetime.now().isoformat()))
            conn.commit()

    def get_books(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books ORDER BY created_at DESC')
            return [dict(row) for row in cursor.fetchall()]

    def get_book(self, book_id: str) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def save_pages(self, book_id: str, pages: List[Dict[str, Any]]):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany('''
                INSERT INTO pages (book_id, page_number, raw_text, cleaned_text)
                VALUES (?, ?, ?, ?)
            ''', [(book_id, p['page_number'], p['raw_text'], p['cleaned_text']) for p in pages])
            conn.commit()

    def get_pages(self, book_id: str) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM pages WHERE book_id = ? ORDER BY page_number', (book_id,))
            return [dict(row) for row in cursor.fetchall()]

    def get_page(self, book_id: str, page_number: int) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM pages WHERE book_id = ? AND page_number = ?', (book_id, page_number))
            row = cursor.fetchone()
            return dict(row) if row else None