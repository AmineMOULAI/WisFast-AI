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

    /* --- CHAT-LIKE CONTENT AREA --- */
    .main-content-container {
        max-width: 850px;
        margin: 0 auto;
        padding-bottom: 150px; /* Space for bottom bar */
    }

    .result-card {
        background: transparent;
        padding: 1.5rem 0;
        border-bottom: 1px solid var(--border-color);
        margin-bottom: 1rem;
    }

    .doc-badge {
        background: rgba(4, 110, 92, 0.2);
        color: var(--secondary-color);
        padding: 4px 10px;
        border-radius: 6px;
        font-family: 'Squada One', cursive;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 10px;
    }

    .source-text-block {
        margin-top: 15px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.8;
        white-space: pre-wrap;
    }

    /* --- FLOATING BOTTOM ACTION BAR --- */
    .stChatInputContainer {
        padding-bottom: 30px !important;
    }

    /* Styling for the custom action bar container */
    .bottom-bar-fixed {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px 0 40px 0;
        background: linear-gradient(to top, var(--bg-dark) 70%, transparent);
        z-index: 99;
        display: flex;
        justify-content: center;
    }

    .action-bar-pill {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid var(--border-color);
        border-radius: 20px;
        padding: 8px 15px;
        width: 100%;
        max-width: 800px;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }

    /* --- COMPACT UPLOADER AS + ICON --- */
    .compact-uploader [data-testid="stFileUploader"] {
        width: 40px;
    }
    .compact-uploader [data-testid="stFileUploader"] section {
        padding: 0 !important;
        background: transparent !important;
        border: none !important;
    }
    .compact-uploader [data-testid="stFileUploader"] section > div {
        display: none;
    }
    .compact-uploader [data-testid="stFileUploader"] button {
        background: rgba(255,255,255,0.1) !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        margin: 0 !important;
        color: white !important;
        border: none !important;
        font-size: 0 !important;
    }
    .compact-uploader [data-testid="stFileUploader"] button::before {
        content: "+";
        font-size: 24px;
        font-weight: 300;
    }
    .compact-uploader [data-testid="stFileUploader"] button:hover {
        background: var(--primary-color) !important;
        transform: scale(1.1);
    }

    /* --- SEARCH INPUT REFINEMENT --- */
    .stTextInput input {
        background-color: transparent !important;
        border: none !important;
        padding: 10px 0 !important;
        color: white !important;
        font-size: 1.1rem !important;
    }
    .stTextInput div[data-baseweb="base-input"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* --- ANIMATIONS --- */
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
