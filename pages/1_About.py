import time
import os
import streamlit as st
from components.footer import footer
from components.warning import warning
from components.translations import init_language, language_selector

t = init_language()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }
    .about-subheader { 
        text-align: center; 
        color: #888; 
        margin-top: -10px; 
        margin-bottom: 40px; 
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    .rtl-text { text-align: right; direction: rtl; font-family: 'Tajawal', sans-serif !important;}
    
    /* Bouton Langue élégant (copié du Home) */
    button[key="global_lang_btn"] {
        border-radius: 12px !important;
        border: 1px solid #444 !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

language_selector()

bolt_path = os.path.join(os.getcwd(), "assets", "bolt.png")
if os.path.exists(bolt_path): st.logo(bolt_path)

# Logo Principal Centré et de taille fixe (Résout le problème du logo géant)
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
logo_path = os.path.join(os.getcwd(), "assets", "WisFast.png")
if os.path.exists(logo_path):
    # La largeur est bloquée à 280px ici
    st.image(logo_path, width=280)
st.markdown("</div>", unsafe_allow_html=True)

rtl = "rtl-text" if st.session_state.lang == 'ar' else ""
st.markdown(f"<h3 class='about-subheader {rtl}'>{t['about_subtitle']}</h3>", unsafe_allow_html=True)

def about_stream():
    for badge, txt in zip(t['badges'], t['texts_about']):
        yield f"<div class='{rtl}'><h3 style='color: #046e5c;'>{badge}</h3>"
        yield f"<p style='line-height: 1.6; color: #ddd;'>{txt}</p></div><hr style='border-color: #333;'>"
        time.sleep(0.3)

if st.button(t['about_btn'], use_container_width=True):
    with st.container(border=True):
        for chunk in about_stream():
            st.markdown(chunk, unsafe_allow_html=True)
    warning()

footer()