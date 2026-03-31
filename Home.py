import streamlit as st 
import os
import base64
from components.footer import footer
from components.translations import init_language, language_selector

st.set_page_config(page_title="WisFast AI", page_icon="⚡", layout="wide")

t = init_language()

# Fonction pour encoder l'image et l'afficher en HTML (Centrage parfait garanti)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# CSS GLOBAL 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }

    .main-header { 
        text-align: center; 
        margin-bottom: 2.5rem; 
        margin-top: 0.5rem;
        font-weight: 700; 
        letter-spacing: -0.5px;
    }

    .badge { 
        background-color: #046e5c; 
        color: white; 
        padding: 4px 12px; 
        border-radius: 20px; 
        font-weight: 600; 
        font-size: 0.85em;
        float: right; 
    }

    /* Bouton Recherche ROND - Aligné avec l'input */
    button[kind="primary"] { 
        border-radius: 50% !important; 
        width: 42px !important; 
        height: 42px !important; 
        background-color: transparent !important; 
        border: 2px solid #555 !important; 
        padding: 0 !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin-bottom: 0px !important; 
    }
    button[kind="primary"]:hover { 
        background-color: #046e5c !important; 
        border-color: #046e5c !important;
    }

    /* Bouton Langue ROND */
    button[key="global_lang_btn"] {
        border-radius: 50% !important;
        width: 45px !important;
        height: 45px !important;
        border: 1px solid #444 !important;
        font-size: 20px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    .rtl-text { text-align: right; direction: rtl; font-family: 'Tajawal', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# 1. Bouton de langue
language_selector()

# 2. Sidebar
logo_path = os.path.join(os.getcwd(), "assets", "WisFast.png")
bolt_path = os.path.join(os.getcwd(), "assets", "bolt.png")
if os.path.exists(bolt_path): st.logo(bolt_path)

with st.sidebar:
    rtl = "rtl-text" if st.session_state.lang == 'ar' else ""
    st.markdown(f"<div class='{rtl}' style='font-size: 1.05em; font-weight: 600; color: #ccc;'>{t['stats']}</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown(f"<div class='{rtl}' style='font-weight: 700;'><h3>{t['uploaded_books']}</h3></div>", unsafe_allow_html=True)
    for livre in ["Épictète.pdf", "MarcAurèle.pdf", "Sénèque.pdf"]:
        st.markdown(f"<div class='{rtl}' style='margin-bottom: 8px;'>📄 <b>{livre}</b></div>", unsafe_allow_html=True)

# 3. Main Page : Logo Centré et Titre
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    # Affichage du logo via HTML/Base64 pour forcer le centrage et enlever le bouton "Fullscreen"
    if os.path.exists(logo_path):
        img_base64 = get_base64_of_bin_file(logo_path)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="data:image/png;base64,{img_base64}" width="280">'
            f'</div>', 
            unsafe_allow_html=True
        )
    
    st.markdown(f"<h1 class='main-header {rtl}'>{t['main_title']}</h1>", unsafe_allow_html=True)

# 4. Barre de recherche 
search_col, btn_col = st.columns([12, 1], vertical_alignment="bottom")

with search_col:
    query = st.text_input("Search", placeholder=t['search_placeholder'], label_visibility="collapsed")
with btn_col:
    search_button = st.button("🔍", type="primary", use_container_width=True)

st.write("")
uploaded_file = st.file_uploader(t['upload_label'], type=["pdf"])

# 5. Résultats
if search_button and query:
    st.divider()
    st.markdown(f"<h3 class='{rtl}' style='font-weight: 600;'>{t['search_results']}</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    for i, res in enumerate(t['mock_results']):
        col = col1 if i % 2 == 0 else col2
        with col:
            with st.container(border=True):
                badge_float = "float: left;" if st.session_state.lang == 'ar' else "float: right;"
                st.markdown(f"<div class='{rtl}'><h4 style='margin-top:0;'>{t['page']} {i*10 + 12} <span class='badge' style='{badge_float}'>{(9-i)*10}%</span></h4></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='{rtl}' style='margin-bottom: 15px; color: #ddd; font-size: 0.95em;'>{res}</div>", unsafe_allow_html=True)
                st.button(t['read_btn'], key=f"btn_read_{i}", use_container_width=True)

# 6. Appel du Footer
footer(t)