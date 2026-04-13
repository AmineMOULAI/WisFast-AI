# Plan: wisFast AI Streamlit Web App

Goal: Implement a production-ready Streamlit web app that performs semantic search over uploaded PDF books using a TF‑IDF + cosine similarity pipeline, with a UI matching the provided wisFast AI mockup. [file:2]

Status legend:
- [ ] TODO
- [~] IN PROGRESS
- [x] DONE

---

## 1. Context & Constraints

- Target users: L3 students and general readers who want fast semantic search in philosophy / study PDFs. [file:2]
- Core capabilities:
  - Upload one or more PDF books.
  - Index each page into a TF‑IDF vector space.
  - Accept natural-language queries in French.
  - Return the top 5 most relevant pages with snippets and a relevance score. [file:2]
- Tech stack:
  - Python 3.11+, Streamlit, PyPDF2, scikit-learn, NLTK, pandas, numpy, SQLite, Docker. [file:2]

Non‑goals in this track:
- No OCR for scanned PDFs.
- No BERT/embedding-based search (only TF‑IDF, but architecture must be BERT‑ready). [file:2]
- No user authentication or multi-tenant accounts.

---

## 2. High-Level Architecture

- UI: Streamlit single-page app with:
  - Sidebar listing uploaded books.
  - Central upload area (drag & drop or “Télécharger un fichier” button).
  - Search bar.
  - Results area with cards (page number, relevance %, snippet, “Lire la page”). [file:2]
- Backend services (Python modules):
  - `PDFProcessor`: extract raw text per page via PyPDF2. [file:2]
  - `TextPreprocessor`: normalize, remove punctuation and French stopwords, tokenize. [file:2]
  - `TfidfIndexer`: train and store TF‑IDF vectors for pages. [file:2]
  - `SemanticSearch`: run cosine similarity over TF‑IDF matrix. [file:2]
  - `ResultRanker`: sort and format the top‑K results. [file:2]
- Data layer:
  - SQLite for page metadata (book, page number, original text).
  - Pickle files for TF‑IDF vectorizer and sparse matrix per book. [file:2]

---

## 3. Milestone 0 – Repository & Environment

Objective: Establish a clean, reproducible Python project that Gemini CLI can safely modify.

### Tasks

- [x] Create a new Git repo `wisfast-ai-streamlit` with a minimal `README.md` describing the project and linking to `wisFast_AI_Official.md`. [file:2]
- [x] Add `.gitignore` for Python, Streamlit, virtualenv, and IDE files.
- [x] Create and activate a Python 3.11 virtualenv.
- [x] Add `requirements.txt` including:
  - `streamlit`, `pypdf2`, `pandas`, `numpy`, `scikit-learn`, `nltk`. [file:2]
- [x] Run `pip install -r requirements.txt` and commit the lockfiles if using `uv` or `pip-tools`.
- [x] Initialize a simple `app.py` that shows “wisFast AI – Hello world”.

---

## 4. Milestone 1 – Project Structure & Core Modules

Objective: Define a clear package layout that matches the architecture and is easy for AI agents to navigate.

### Proposed layout

- `app.py` – Streamlit entrypoint.
- `wisfast/`
  - `__init__.py`
  - `ui/streamlit_view.py`
  - `services/pdf_processor.py`
  - `services/text_preprocessor.py`
  - `services/search_strategies.py`
  - `services/index_manager.py`
  - `data/sqlite_repository.py`
  - `evaluation/metrics.py`
  - `config.py`
- `data/` – SQLite DB file, pickled models.
- `tests/` – pytest test files.

### Tasks

- [x] Create the `wisfast` package and subpackages (`ui`, `services`, `data`, `evaluation`). 
- [x] Implement a `config.py` module to centralize constants (paths for DB and pickle files, TF‑IDF settings, top‑K result count, language configuration).
- [x] Wire `app.py` to call a `run()` function in `wisfast/ui/streamlit_view.py` to keep the entrypoint thin. [5315df4]

---

## 5. Milestone 2 – PDF Extraction & Text Preprocessing

Objective: Implement reliable text extraction and normalization for French philosophical texts.

### Tasks

- [x] Implement `PDFProcessor` in `services/pdf_processor.py`:
  - API: `extract_pages(pdf_path) -> list[PageText]` where `PageText` includes `page_number`, `raw_text`.
  - Use PyPDF2 to iterate over pages and extract text. [file:2]
  - Handle empty/very short pages gracefully (log and skip).
- [x] Implement `TextPreprocessor` in `services/text_preprocessor.py`:
  - Initialize NLTK French stopwords, ensure required corpora are downloaded at install/dev time. [file:2]
  - Provide `clean(text: str) -> str` applying: lowercase, punctuation removal, stopword filtering, basic tokenization. [file:2]
  - Optionally retain original punctuation for snippets while using cleaned text only for indexing.
- [ ] Add unit tests for extraction and preprocessing on small sample PDFs (including one public-domain Stoic text).

---

## 6. Milestone 3 – TF‑IDF Indexing & Search Strategy Pattern

Objective: Build the semantic search pipeline with clean abstractions and persistence.

### Tasks

- [x] Define an abstract `SearchStrategy` interface in `services/search_strategies.py` with method `search(query: str, book_id: str, k: int = 5) -> list[SearchResult]`. [file:2]
- [x] Implement `KeywordSearchStrategy` (simple baseline using term presence / count in pages) for early testing. [file:2]
- [x] Implement `TfidfSemanticStrategy`:
  - Use `TfidfVectorizer(max_features=5000, ngram_range=(1, 2))`. [file:2]
  - Train on cleaned page texts for a given book.
  - Store trained vectorizer and sparse matrix (per book) as pickles under `data/`.
  - Implement cosine similarity over the TF‑IDF matrix to rank pages. [file:2]
- [x] Implement `TfidfIndexManager` in `services/index_manager.py` as a Singleton responsible for:
  - Lazy loading / caching TF‑IDF models for each book.
  - Triggering re‑indexing when a new PDF is uploaded.
  - Exposing APIs like `ensure_index(book_id)` and `search(book_id, query, k)`. [file:2]
- [x] Implement `ResultRanker` logic to:
  - Convert raw scores to 0–100 percentages for display (e.g., `score * 100` rounded).
  - Attach page metadata and short snippets. [file:2]
- [ ] Add basic tests for TF‑IDF indexing and search correctness on a small corpus.

---

## 7. Milestone 4 – Data Layer with SQLite

Objective: Persist page metadata and support multi‑book search.

### Tasks

- [x] Design SQLite schema in `data/sqlite_repository.py`:
  - `books(id, file_name, display_name, page_count, created_at, updated_at)`
  - `pages(id, book_id, page_number, raw_text, cleaned_text)`
  - Index on `(book_id, page_number)` and full‑text indices as needed.
- [x] Implement repository functions:
  - `create_book(...)`, `get_books()`, `get_book(id)`.
  - `save_pages(book_id, pages)`.
  - `get_page(book_id, page_number)` and `get_pages(book_id, page_numbers)`.
- [x] Ensure PDF upload flow:
  - When a user uploads a PDF, create a new `book` record, store page texts, and kick off TF‑IDF index creation via `TfidfIndexManager`. [file:2]
- [ ] Add tests ensuring that upload followed by search returns consistent page IDs and metadata.

---

## 8. Milestone 5 – Streamlit UI Matching Mockup

Objective: Build the Streamlit front‑end to closely match the wisFast AI screenshot / wireframe.

### Tasks

- [x] Implement sidebar:
  - Display wisFast AI logo/title.
  - Section “Livres Uploadés” listing all books from SQLite (e.g., “Épictète.pdf”, “MarcAurele.pdf”). [file:2]
  - Allow selecting the active book for search.
- [x] Implement main header:
  - Title “wisFast AI – Recherche intelligente dans tes livres”.
  - Short subtitle if desired.
- [x] Implement upload area (center top):
  - Drag‑and‑drop / file uploader with text “Glissez & déposez vos PDF ici ou” and a “Télécharger un fichier” button.
  - On upload:
    - Show progress indicator while extracting and indexing pages.
    - Update status text like “Épictète.pdf – 234 pages indexées”. [file:2]
- [x] Implement search bar:
  - Single text input, placeholder “conseils patience épreuves…”.
  - On submit:
    - Call the selected `SearchStrategy` (default TF‑IDF).
    - Capture query for logging / evaluation.
- [x] Implement results area:
  - Section title “Résultats de la recherche”.
  - For each of the top 5 pages:
    - Card with:
      - “Page XX”.
      - Badge with relevance % (e.g., “92%”).
      - Short excerpt (≈ 1–2 sentences or 50 words around the best‑matching span).
      - “Lire la page” button that:
        - Expands to show the full page text or scrolls to a modal with full page content.
- [x] Apply a dark theme similar to the mockup using Streamlit’s theming options or custom CSS.

---

## 9. Milestone 6 – Observer Pattern & Live Indexing Feedback

Objective: Provide responsive UI updates during indexing using an Observer‑style pattern. [file:2]

### Tasks

- [ ] Implement an internal observable `SearchIndex` or `IndexingJob` object that:
  - Tracks indexing status (pending, running, completed, failed).
  - Notifies attached observers on progress updates. [file:2]
- [ ] Implement a simple `UIObserver` layer:
  - In Streamlit, periodically poll or react to state changes and update status messages / progress bars.
- [ ] Ensure that the user sees:
  - Clear messages while pages are being extracted.
  - A success state when indexing is complete and search is ready.

---

## 10. Milestone 7 – Evaluation Metrics & Experiments

Objective: Quantify search quality and speed according to the course requirements. [file:2]

### Tasks

- [ ] Implement evaluation utilities in `evaluation/metrics.py` for:
  - Precision@K.
  - Recall@K.
  - Mean Reciprocal Rank (MRR). [file:2]
- [ ] Create a `notebooks/evaluation.ipynb` (or a Python script) that:
  - Defines at least 10 representative queries and expected relevant pages.
  - Runs evaluation against:
    - `KeywordSearchStrategy`.
    - `TfidfSemanticStrategy`.
  - Compares metrics and response time (< 500 ms target for 5‑page results). [file:2]
- [ ] Store evaluation results as CSV in `evaluation/results/` for inclusion in the final report.

---

## 11. Milestone 8 – Testing, Performance & Error Handling

Objective: Ensure the app is robust and fast enough for 200–1000 pages. [file:2]

### Tasks

- [ ] Add pytest tests for:
  - PDF parsing edge cases (empty pages, weird encoding).
  - Preprocessing correctness for typical French text.
  - TF‑IDF search returning higher scores for truly relevant pages.
- [ ] Add simple performance tests:
  - Measure indexing time for a 200‑page PDF.
  - Measure search latency across several queries.
- [ ] Implement error handling in Streamlit:
  - User‑friendly messages for unsupported PDFs, indexing failures, DB errors.
  - Logging of stack traces to a file for debugging.

---

## 12. Milestone 9 – Dockerization & Run Scripts

Objective: Make the app runnable with a single command for grading and deployment. [file:2]

### Tasks

- [ ] Create `Dockerfile`:
  - Base image: slim Python 3.11.
  - Install system packages required for PyPDF2 / NLTK.
  - Copy `requirements.txt` and install dependencies.
  - Copy application code.
  - Set default command to `streamlit run app.py --server.port=8501 --server.address=0.0.0.0`.
- [ ] Create `docker-compose.yml` (optional but recommended):
  - Single service exposing port 8501.
  - Volume for persistent `data/` directory.
- [ ] Document Docker usage in `README.md`:
  - `docker build -t wisfast-ai .`
  - `docker run -p 8501:8501 wisfast-ai`.

---

## 13. Milestone 10 – Documentation & Final Polish

Objective: Prepare for submission and future maintenance.

### Tasks

- [ ] Update `README.md` with:
  - Project overview, architecture diagram, and screenshots of the UI.
  - Quickstart instructions (local and Docker).
  - Short description of the NLP pipeline and evaluation metrics. [file:2]
- [ ] Add `ARCHITECTURE.md` capturing:
  - Component diagram (PDFProcessor, TextPreprocessor, TfidfIndexer, SemanticSearch, ResultRanker, SQLite, Streamlit). [file:2]
  - Explanation of design patterns used (Strategy, Singleton, Observer) and why. [file:2]
- [ ] Ensure code is consistently formatted (black/ruff or similar) and follows clear naming conventions.
- [ ] Tag a final Git release (e.g., `v1.0.0`) for the L3 project delivery.

---

## 14. Approval

- [ ] Review this plan with the instructor or teammate.
- [ ] Once approved, allow Gemini CLI / Conductor to start implementing tasks milestone by milestone, updating checkbox states and adding commit SHAs back into this `PLAN.md` as work progresses. [web:8]
