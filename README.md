# wisFast AI

A production-ready Streamlit web app that performs semantic search over uploaded PDF books using a TF‑IDF + cosine similarity pipeline.

## Features
- **Fast Upload & Processing**: Upload PDFs and automatically extract text page-by-page.
- **Semantic Search**: Searches using TF-IDF and Cosine Similarity to find the most relevant pages.
- **Smart Interface**: Built with Streamlit, provides snippet extraction, relevance scores, and allows you to read the matching pages.

## Quickstart

### Running Locally
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `streamlit run app.py`

### Running with Docker
1. `docker build -t wisfast-ai .`
2. `docker run -p 8501:8501 wisfast-ai`
   *Or with Docker Compose:*
   `docker-compose up -d`

## NLP Pipeline
- **Extraction**: Uses `PyPDF2` to extract text from each page.
- **Preprocessing**: Cleans the text by converting it to lowercase, tokenizing, removing punctuation and French stopwords using `NLTK`.
- **Indexing**: A `TfidfVectorizer` (max_features=5000, n-gram=(1,2)) transforms the page texts into a sparse matrix per book.
- **Search**: Computes the cosine similarity between the query vector and the book's document matrix to rank the top pages.