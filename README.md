# ⚡ WisFast AI

<div align="center">
  <img src="assets/bolt.png" width="200" alt="WisFast Logo">
  <h1>BEYOND SEARCH. <br><span style="color: #046e5c;">UNDERSTANDING.</span></h1>
  <p><i>Experience the power of Semantic Intelligence. Transform your PDFs into a dynamic knowledge base.</i></p>
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

## 📐 Architecture
WisFast follows a clean service-oriented architecture:
- `PDFProcessor`: Extracting raw text from multipage documents.
- `TextPreprocessor`: Cleaning and normalizing French philosophical and technical text.
- `TfidfIndexManager`: Managing lazy-loaded vector spaces and persistence.
- `SemanticSearch`: Executing cosine similarity queries against the indexed knowledge base.

---

<div align="center">
  <p>Built with ❤️ by <b>Amine Moulai</b> for the L3 Software Engineering course (UPVD)</p>
</div>
