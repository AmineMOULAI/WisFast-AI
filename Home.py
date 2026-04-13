import streamlit as st
import os
import base64
from wisfast.ui.styles import apply_custom_styles
from components.footer import footer

def get_image_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(page_title="WisFast AI", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")
    apply_custom_styles()

    # Get logo base64 for animation
    logo_base64 = get_image_as_base64("assets/WisFast.png")

    # Animated Hero Section - Centered and Compact for "Above the Fold" visibility
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0 1rem 0; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <img src="data:image/png;base64,{logo_base64}" class="bolt-animated" style="width: 320px; margin-bottom: 1rem;">
        <h1 style="font-size: 5rem; color: #ffffff; line-height: 1.1; margin: 0; font-family: 'Squada One', cursive;">
            BEYOND SEARCH. <br><span style="color: #046e5c;">UNDERSTANDING.</span>
        </h1>
        <p style="font-size: 1.3rem; color: #a0aec0; max-width: 700px; margin: 1.5rem auto 2rem auto;">
            Experience the power of Semantic Intelligence. Transform your PDFs into a dynamic knowledge base that understands your intent.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Glassmorphism Launch Button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 LAUNCH RESEARCH ENGINE", width='stretch'):
            st.switch_page("pages/2_App.py")

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # Feature Cards with Dark Theme Styling
    f1, f2, f3 = st.columns(3)
    
    card_style = """
        background: rgba(255, 255, 255, 0.05); 
        padding: 2rem; 
        border-radius: 24px; 
        border: 1px solid rgba(78, 205, 196, 0.1); 
        height: 100%;
        backdrop-filter: blur(10px);
    """
    
    with f1:
        st.markdown(f"""
        <div class="float-card" style="{card_style}">
            <span style="font-size:2rem;">⚡</span>
            <h3 style="color:#ffffff; margin-top:0.8rem; font-family: 'Squada One', cursive;">INSTANT INDEXING</h3>
            <p style="color:#a0aec0; line-height:1.5; font-size: 0.95rem;">Semantically index hundreds of pages in seconds. Your data is ready for research when you are.</p>
        </div>
        """, unsafe_allow_html=True)
    with f2:
        st.markdown(f"""
        <div class="float-card" style="{card_style}">
            <span style="font-size:2rem;">🎯</span>
            <h3 style="color:#ffffff; margin-top:0.8rem; font-family: 'Squada One', cursive;">SEMANTIC PRECISION</h3>
            <p style="color:#a0aec0; line-height:1.5; font-size: 0.95rem;">TF-IDF & Cosine Similarity map the intent of your questions, finding exactly what you mean.</p>
        </div>
        """, unsafe_allow_html=True)
    with f3:
        st.markdown(f"""
        <div class="float-card" style="{card_style}">
            <span style="font-size:2rem;">🛡️</span>
            <h3 style="color:#ffffff; margin-top:0.8rem; font-family: 'Squada One', cursive;">PRIVATE & SECURE</h3>
            <p style="color:#a0aec0; line-height:1.5; font-size: 0.95rem;">Privacy is our foundation. All processing happens on your local knowledge base.</p>
        </div>
        """, unsafe_allow_html=True)

    footer()

if __name__ == "__main__":
    main()
