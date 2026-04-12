import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "wisfast.db")
MODELS_DIR = os.path.join(DATA_DIR, "models")

# TF-IDF Settings
MAX_FEATURES = 5000
NGRAM_RANGE = (1, 2)
TOP_K_RESULTS = 5

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)