import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Squada+One&display=swap');

    :root {
        --primary-color: #046e5c;
        --primary-light: #058c75;
        --secondary-color: #4ecdc4;
        --bg-dark: #0b1a18; 
        --sidebar-bg: #0e2623;
        --text-main: #ffffff;
        --text-muted: #a0aec0;
        --border-color: rgba(255, 255, 255, 0.08);
        --btn-gradient: linear-gradient(135deg, #046e5c 0%, #035246 100%);
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Global App Background */
    .stApp {
        background-color: var(--bg-dark) !important;
    }

    /* --- PROFESSIONAL RECTANGULAR BUTTONS --- */
    div.stButton > button {
        border-radius: 10px !important; /* Professional radius */
        padding: 0.6rem 1.8rem !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 600 !important;
        background: var(--btn-gradient) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
        transition: var(--transition) !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #058c75 0%, #046e5c 100%) !important;
        border-color: var(--secondary-color) !important;
        transform: translateY(-2px) !important;
    }

    /* --- SIDEBAR REFINEMENTS --- */
    section[data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border-color) !important;
    }

    /* Sidebar Section Headers */
    .sidebar-section-header {
        font-family: 'Squada One', cursive;
        color: var(--secondary-color);
        font-size: 0.85rem;
        letter-spacing: 1.5px;
        margin: 1.5rem 0 0.8rem 0.5rem;
        opacity: 0.8;
        text-transform: uppercase;
    }

    /* Sidebar Navigation & Library Buttons */
    section[data-testid="stSidebar"] div.stButton > button {
        background: rgba(255, 255, 255, 0.02) !important;
        border-radius: 8px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        padding: 14px 18px !important;
        font-size: 0.95rem !important;
        color: #cbd5e0 !important;
        border: 1px solid transparent !important;
    }

    section[data-testid="stSidebar"] div.stButton > button:hover {
        background: rgba(78, 205, 196, 0.08) !important;
        transform: translateX(6px) !important;
    }

    /* --- ONLY DELETE BUTTON IS ROUND --- */
    div.stButton > button[key*="del"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        color: rgba(255, 255, 255, 0.3) !important;
        width: 34px !important;
        height: 34px !important;
        min-width: 34px !important;
        border-radius: 50% !important; /* Perfect Circle */
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: var(--transition) !important;
        margin-top: 4px !important;
    }

    div.stButton > button[key*="del"]:hover {
        background: rgba(255, 107, 107, 0.15) !important;
        border-color: #ff6b6b !important;
        color: #ff6b6b !important;
        box-shadow: 0 0 20px rgba(255, 107, 107, 0.3) !important;
        transform: scale(1.1) rotate(10deg) !important;
    }

    /* --- CIRCULAR GREEN BUTTON --- */
    .green-circle-btn button {
        background: var(--btn-gradient) !important;
        border-radius: 50% !important;
        width: 48px !important;
        height: 48px !important;
        min-width: 48px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 15px rgba(4, 110, 92, 0.4) !important;
        transition: var(--transition) !important;
    }

    .green-circle-btn button:hover {
        transform: scale(1.1) rotate(90deg) !important;
        box-shadow: 0 0 25px rgba(78, 205, 196, 0.4) !important;
        border-color: var(--secondary-color) !important;
    }

    /* --- COMPACT FILE UPLOADER AS BUTTON --- */
    .compact-uploader [data-testid="stFileUploader"] {
        width: 48px;
        padding: 0;
    }
    .compact-uploader [data-testid="stFileUploader"] section {
        padding: 0 !important;
        background: transparent !important;
        border: none !important;
    }
    .compact-uploader [data-testid="stFileUploader"] section > div {
        display: none; /* Hide 'Drag and drop' text */
    }
    .compact-uploader [data-testid="stFileUploader"] button {
        background: var(--btn-gradient) !important;
        border-radius: 50% !important;
        width: 48px !important;
        height: 48px !important;
        min-width: 48px !important;
        margin: 0 !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        font-size: 0 !important; /* Hide 'Browse files' text */
    }
    .compact-uploader [data-testid="stFileUploader"] button::before {
        content: "➕";
        font-size: 20px;
    }
    .compact-uploader [data-testid="stFileUploader"] button:hover {
        transform: scale(1.1) rotate(90deg);
        border-color: var(--secondary-color) !important;
    }

    /* --- SEARCH BAR REFINEMENT --- */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.04) !important;
        border-radius: 12px !important; /* Structured, not pill */
        border: 1.5px solid var(--border-color) !important;
        padding: 1.2rem 1.5rem !important;
        color: white !important;
    }

    .stTextInput input:focus {
        border-color: var(--secondary-color) !important;
        box-shadow: 0 0 30px rgba(78, 205, 196, 0.1) !important;
    }

    /* Result Cards */
    .result-card {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px;
        padding: 2.2rem;
        border: 1px solid var(--border-color);
        margin-bottom: 2.5rem;
    }

    /* Citation & Badge Styling */
    .doc-badge {
        background: rgba(4, 110, 92, 0.3);
        color: var(--secondary-color);
        padding: 6px 14px;
        border-radius: 10px;
        font-family: 'Squada One', cursive;
        font-size: 0.9rem;
        letter-spacing: 1px;
    }

    /* --- SOURCE TEXT ENHANCEMENT --- */
    .source-text-block {
        margin-top: 15px;
        padding: 20px;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.8;
        white-space: pre-wrap;
        max-height: 400px;
        overflow-y: auto;
    }

    /* Animations */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    .fade-in { animation: fadeIn 0.7s cubic-bezier(0.4, 0, 0.2, 1) forwards; }

    @keyframes bolt-glow {
        0% { filter: drop-shadow(0 0 5px rgba(78, 205, 196, 0.2)); transform: translateY(0); }
        50% { filter: drop-shadow(0 0 20px rgba(78, 205, 196, 0.6)); transform: translateY(-10px); }
        100% { filter: drop-shadow(0 0 5px rgba(78, 205, 196, 0.2)); transform: translateY(0); }
    }
    .bolt-animated {
        animation: bolt-glow 3s ease-in-out infinite;
    }

    #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)
