FROM python:3.11-slim

WORKDIR /app

# Install system dependencies needed for PyPDF2 / NLTK
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download NLTK data to speed up runtime
RUN python -m nltk.downloader stopwords punkt punkt_tab

# Copy app code
COPY . .

# Expose port
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]