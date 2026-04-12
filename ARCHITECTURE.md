# Architecture

This document describes the software architecture and design patterns used in **wisFast AI**.

## System Components

- **UI / Views**: Streamlit acts as the presentation layer (`wisfast/ui/streamlit_view.py`).
- **Domain Services**:
  - `PDFProcessor`: Extracts text using `PyPDF2`.
  - `TextPreprocessor`: Normalizes text using `NLTK`.
  - `SearchStrategies`: Interface for querying the indexed PDFs.
  - `TfidfIndexManager`: Caches and manages the vector matrices.
- **Data Layer**:
  - `SQLiteRepository`: Manages metadata mapping (books to pages) for retrieval (`wisfast/data/sqlite_repository.py`).
  - Pickle Files: Serialized scikit-learn models (`wisfast/services/index_manager.py`).

## Design Patterns

1. **Strategy Pattern**: `SearchStrategy` allows us to easily swap between a simple keyword matcher and the `TfidfSemanticStrategy`.
2. **Singleton Pattern**: `TfidfIndexManager` loads the model files lazily and maintains them in memory to prevent slow disk reads across multiple searches.
3. **Repository Pattern**: `SQLiteRepository` abstractions isolate the application logic from the underlying SQLite queries.
