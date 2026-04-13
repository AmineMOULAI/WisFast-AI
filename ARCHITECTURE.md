# ⚡ WisFast AI - Architecture

This document provides a deep dive into the technical design and architectural patterns that power **WisFast AI**.

## 🏗️ System Overview

WisFast AI is built on a clean, service-oriented architecture that separates the presentation layer from the core semantic intelligence logic.

<div align="center">
  <img src="assets/bolt.png" width="100" alt="WisFast Logo">
</div>

### 📡 Presentation Layer
- **Streamlit (`wisfast/ui/streamlit_view.py`)**: Acts as the main orchestrator for the reactive UI. It handles session state, user input, and coordinates calls to the underlying services.
- **Custom Styling (`wisfast/ui/styles.py`)**: A dedicated CSS injection module that applies the high-end Glassmorphism theme and custom animations.

### 🧠 Domain Services (`wisfast/services/`)
- **`PDFProcessor`**: An efficient extraction utility that converts raw PDF bytes into structured page objects.
- **`TextPreprocessor`**: A linguistic pipeline that prepares French text for vectorization through normalization and noise reduction.
- **`TfidfIndexManager`**: A centralized manager for the lifecycle of TF-IDF models. It handles the lazy-loading, caching, and persistence of vector matrices.
- **`SearchStrategies`**: An extensible interface for different search algorithms. The primary implementation uses **Cosine Similarity** over TF-IDF vectors.

### 💾 Persistence Layer (`wisfast/data/`)
- **SQLite Database**: A relational store for structured metadata, including book details, page-by-page content, and user search history.
- **Pickle Binary Store**: High-performance storage for the sparse matrices and vectorizers that constitute the search indices.

---

## 🎨 Design Patterns

### 1. Strategy Pattern
We use the **Strategy Pattern** for our search implementation. This allows the system to swap search algorithms (e.g., from TF-IDF to BERT or simple Keyword) without modifying the UI or the `IndexManager`.

### 2. Singleton Pattern
The `TfidfIndexManager` is implemented as a **Singleton**. This ensures that model files are loaded into memory exactly once, providing ultra-fast query responses across the entire user session.

### 3. Repository Pattern
All database interactions are encapsulated within the `SQLiteRepository`. This isolates the application's domain logic from the specifics of SQL queries and schema design.

### 4. Observer-Inspired Processing
The indexing and extraction pipeline uses a callback mechanism to provide real-time status updates back to the UI, ensuring a responsive user experience during heavy processing tasks.

---

<div align="center">
  <p><i>WisFast AI: Engineering for Speed and Precision.</i></p>
</div>
