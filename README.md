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

---

## 🗺️ Roadmap & Future Enhancements
We are constantly pushing the boundaries of what WisFast AI can do. Here are the features currently in development:

- **🔍 OCR Integration:** Adding support for scanned documents and images using Tesseract/PaddleOCR to ensure no knowledge is left behind.
- **🌍 Multilingual Expansion:** Full UI and semantic search support for **English (EN)** and **Arabic (AR)** to cater to a global research audience.
- **🤖 Advanced NLP (LLM/BERT):** Transitioning from TF-IDF to Transformer-based embeddings (BERT/E5) for deeper, context-aware semantic understanding.
- **📊 Research Export:** Capability to export search results and snippets into structured Research Reports (PDF/Markdown).
- **☁️ Cloud Sync:** Optional encrypted cloud backup for your knowledge library across devices.

---

## 📖 How to Use

1. **Launch the Engine**: Access the application via your browser (default: `http://localhost:8501`).
2. **Add Knowledge**: Click on the **"➕"** (Upload) button in the top action bar or use the upload area.
3. **Index Your PDF**: Drop your PDF file. The engine will extract, clean, and index the text automatically.
4. **Search Smart**:
   - Type natural language queries (e.g., "la vision stoïcienne du bonheur").
   - Switch between books using the **Knowledge Library** in the sidebar.
   - Review match percentages and snippets to find the exact page you need.

---

## 🛠️ Deployment & Setup Tutorials

### 🐳 Option A: Docker (Recommended)
The fastest way to get started with zero configuration.

1. **Build and Run**:
   ```bash
   docker-compose up --build
   ```
2. **Access**: Open `http://localhost:8501` in your browser.
3. **Persistence**: Your indexed data is saved in the `./data` folder on your host machine.

### 🐍 Option B: Manual Installation
For users who want to run the project directly with Python.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AmineMOULAI/WisFast-AI.git
   cd WisFast-AI
   ```
2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch the Engine**:
   ```bash
   streamlit run Home.py
   ```

---

## 📐 Detailed Architecture

WisFast AI is built on a modular, service-oriented architecture designed for scalability and performance.

### 1. Data Processing Pipeline (`wisfast/services/`)
- **`PDFProcessor`**: Handles high-speed text extraction using `PyPDF2` with real-time UI callbacks.
- **`TextPreprocessor`**: A sophisticated normalization engine for French-specific tokenization and stop-word filtering using `NLTK`.

### 2. Semantic Intelligence Engine
- **`TfidfIndexManager`**: A Singleton service managing the lifecycle and caching of vector matrices for sub-500ms responses.
- **`SearchStrategy`**: Transforms queries into high-dimensional vectors and calculates **Cosine Similarity** to find conceptual relevance.

### 3. Persistence Layer (`wisfast/data/`)
- **SQLite Store**: Manages book metadata, page content, and thread history.
- **Pickle Store**: Optimized binary storage for pre-computed sparse matrices.

---

<div align="center">
  <p>CRAFTED BY <a href="https://github.com/AmineMOULAI" target="_blank" style="color: #046e5c; font-weight: bold; text-decoration: none;">AMINE MOULAI</a></p>
  <p><i>Pushing the boundaries of Semantic Research.</i></p>
</div>
