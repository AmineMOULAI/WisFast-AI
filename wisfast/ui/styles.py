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

    /* --- SIDEBAR REFINEMENTS --- */
    section[data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border-color) !important;
    }

    .sidebar-section-header {
        font-family: 'Squada One', cursive;
        color: var(--secondary-color);
        font-size: 0.85rem;
        letter-spacing: 1.5px;
        margin: 1.5rem 0 0.8rem 0.5rem;
        opacity: 0.8;
        text-transform: uppercase;
    }

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

    /* --- ROUND DELETE BUTTON --- */
    div.stButton > button[key*="del"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        color: rgba(255, 255, 255, 0.3) !important;
        width: 34px !important;
        height: 34px !important;
        min-width: 34px !important;
        border-radius: 50% !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: var(--transition) !important;
        margin-top: 4px !important;
    }

    /* --- HERO SECTION --- */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        text-align: center;
        gap: 2rem;
    }

    .hero-bolt {
        width: 120px;
        filter: drop-shadow(0 0 15px rgba(78, 205, 196, 0.4));
        animation: bolt-float 3s ease-in-out infinite;
    }

    @keyframes bolt-float {
        0%, 100% { transform: translateY(0) scale(1); filter: drop-shadow(0 0 15px rgba(78, 205, 196, 0.4)); }
        50% { transform: translateY(-20px) scale(1.05); filter: drop-shadow(0 0 30px rgba(78, 205, 196, 0.8)); }
    }

    /* --- MODERN UPLOADER --- */
    .hero-uploader [data-testid="stFileUploader"] {
        width: 300px;
        margin: 0 auto;
    }

    .hero-uploader [data-testid="stFileUploader"] section {
        background-color: rgba(4, 110, 92, 0.1) !important;
        border: 2px dashed var(--primary-color) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        transition: var(--transition);
    }

    .hero-uploader [data-testid="stFileUploader"] section:hover {
        border-color: var(--secondary-color) !important;
        background-color: rgba(4, 110, 92, 0.2) !important;
        transform: translateY(-5px);
    }

    /* --- COMPACT UPLOADER AS GREEN + ICON --- */
    .compact-uploader [data-testid="stFileUploader"] {
        width: 48px;
        padding: 0 !important;
    }
    
    /* Hide ALL default Streamlit uploader elements */
    [data-testid="stFileUploader"] section {
        padding: 0 !important;
        background: transparent !important;
        border: none !important;
        min-height: 0 !important;
    }
    [data-testid="stFileUploader"] label, 
    [data-testid="stFileUploader"] small, 
    [data-testid="stFileUploader"] div[data-testid="stMarkdownContainer"],
    [data-testid="stFileUploaderDropzone"] > div {
        display: none !important;
    }
    /* Hide the uploaded file list */
    [data-testid="stFileUploader"] section + div {
        display: none !important;
    }

    .compact-uploader [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #00c853 0%, #009624 100%) !important;
        border-radius: 50% !important;
        width: 44px !important;
        height: 44px !important;
        min-width: 44px !important;
        margin: 0 !important;
        color: white !important;
        border: none !important;
        font-size: 0 !important;
        box-shadow: 0 4px 15px rgba(0, 200, 83, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .compact-uploader [data-testid="stFileUploader"] button::before {
        content: "+";
        font-size: 30px;
        font-weight: 500;
        display: block;
        line-height: 1;
    }
    .compact-uploader [data-testid="stFileUploader"] button:hover {
        transform: rotate(90deg) scale(1.1) !important;
        box-shadow: 0 6px 20px rgba(0, 200, 83, 0.5) !important;
    }

    /* --- SEARCH BAR --- */
    .bottom-bar-fixed {
        position: fixed;
        bottom: 50px;
        left: 0;
        right: 0;
        z-index: 99;
        display: flex;
        justify-content: center;
        padding: 0 20px;
    }

    .action-bar-pill {
        background: rgba(15, 35, 32, 0.8);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 10px 20px;
        width: 100%;
        max-width: 800px;
        display: flex;
        align-items: center;
        gap: 15px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.6);
    }

    .stTextInput input {
        background-color: transparent !important;
        border: none !important;
        padding: 12px 0 !important;
        color: white !important;
        font-size: 1.1rem !important;
    }
    .stTextInput div[data-baseweb="base-input"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* --- RESULTS --- */
    .main-content-container {
        max-width: 850px;
        margin: 0 auto;
        padding-top: 2rem;
        padding-bottom: 150px;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid var(--border-color);
        margin-bottom: 1.5rem;
        transition: var(--transition);
    }
    .result-card:hover {
        background: rgba(255, 255, 255, 0.04);
        border-color: rgba(78, 205, 196, 0.2);
    }

    .doc-badge {
        background: rgba(78, 205, 196, 0.1);
        color: var(--secondary-color);
        padding: 4px 12px;
        border-radius: 8px;
        font-family: 'Squada One', cursive;
        font-size: 0.85rem;
        display: inline-block;
        margin-bottom: 12px;
    }

    /* --- ANIMATIONS --- */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    .fade-in { animation: fadeIn 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }

    #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)
