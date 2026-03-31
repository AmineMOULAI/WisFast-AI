import streamlit as st

def footer(t):
    # Séparateur visuel avant le footer
    st.markdown("<br><hr style='border-color: #333;'>", unsafe_allow_html=True)
    
    # Footer classique dans le flux de la page (pas de 'position: fixed')
    st.markdown(f"""
    <div style='
        width: 100%; 
        color: #888; 
        text-align: center; 
        padding: 20px 0; 
        font-size: 14px;
    '>
        <p>{t['footer_text']}</p>
    </div>
    """, unsafe_allow_html=True)