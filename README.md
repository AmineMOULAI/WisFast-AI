# ⚡ WisFast AI

<div align="center">
  <img src="assets/bolt.png" width="200" alt="WisFast Logo">
  <h1>BEYOND SEARCH. <br><span style="color: #046e5c;">UNDERSTANDING.</span></h1>
  <p><i>A Personal Project by <b>Amine Moulai</b></i></p>
  <p>Experience the power of Semantic Intelligence. Transform your PDFs into a dynamic knowledge base that understands your intent.</p>
</div>

---

## 🚀 Overview
**WisFast AI** is a professional-grade research assistant designed to move beyond traditional keyword matching. By leveraging **TF-IDF algorithms** and **Cosine Similarity**, it understands the *intent* behind your questions, finding exactly what you need in seconds across hundreds of pages.

## ✨ Key Features
- **⚡ Instant Indexing:** Semantically index large PDF documents in seconds.
- **🎯 Semantic Precision:** Intelligent ranking that maps intent, not just keywords.
- **🛡️ Private & Secure:** Local SQLite storage and processing ensures your data stays yours.
- **📱 Modern UI:** Glassmorphism design with a dark theme, built for high-speed research.

## 🛠️ Tech Stack
- **Frontend:** Streamlit with Custom CSS (Glassmorphism)
- **NLP Engine:** Scikit-learn (TF-IDF), NLTK (French Tokenization)
- **Data Layer:** SQLite for metadata, Pickle for sparse matrices
- **PDF Core:** PyPDF2

## 📦 Quick Start

### Prerequisites
- Python 3.11+
- Virtual environment (recommended)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AmineMOULAI/WisFast-AI.git
   cd WisFast-AI
   ```

2. **Setup Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Launch the Engine:**
   ```bash
   streamlit run Home.py
   ```

---

## 📐 Detailed Architecture

WisFast AI is built on a modular, service-oriented architecture designed for scalability and performance.

### 1. Data Processing Pipeline (`wisfast/services/`)
- **`PDFProcessor`**: Handles high-speed text extraction from multipage PDF documents using `PyPDF2`. It includes interruptible callbacks for real-time progress tracking in the UI.
- **`TextPreprocessor`**: A sophisticated normalization engine that performs lowercasing, French-specific tokenization, and filters out stop-words and punctuation using `NLTK`. This ensures the semantic search focuses on meaningful content.

### 2. Semantic Intelligence Engine
- **`TfidfIndexManager`**: A Singleton service that manages the lifecycle of search indices. It lazily loads vectorizers and sparse matrices, caching them in memory for sub-500ms query responses.
- **`SearchStrategy (TF-IDF + Cosine Similarity)`**: Instead of looking for exact word matches, this module transforms queries and document pages into high-dimensional vectors. It calculates the **Cosine Similarity** between these vectors to rank pages by their conceptual relevance to the user's intent.

### 3. Persistence Layer (`wisfast/data/`)
- **SQLite Metadata Store**: Manages persistent storage for uploaded book metadata, individual page content, and user search history.
- **Pickle Binary Store**: Optimized storage for the `scikit-learn` TF-IDF models and pre-computed sparse matrices, enabling instant index loading without re-processing.

### 4. UI & Experience (`wisfast/ui/`)
- **Streamlit View Controller**: Orchestrates the multi-page application flow, handling session state for search history and book selection.
- **Custom CSS Engine**: Injects custom Glassmorphism styles and CSS animations (like the glowing bolt) to provide a premium, modern feel that diverges from standard Streamlit templates.

---

<div align="center">
  <p>CRAFTED BY <a href="https://github.com/AmineMOULAI" target="_blank" style="color: #046e5c; font-weight: bold; text-decoration: none;">AMINE MOULAI</a></p>
  <p><i>Pushing the boundaries of Semantic Research.</i></p>
</div>
