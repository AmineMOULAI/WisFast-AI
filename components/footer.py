import streamlit as st

def footer():
    st.markdown("""
    <div style='
        position: fixed; 
        bottom: 0; 
        left: 0; 
        width: 100%; 
        background: #046e5c; 
        color: white; 
        text-align: center; 
        padding: 10px; 
        font-size: 14px;
        z-index: 1000;
    '>
        <p>⚡ WisFast AI - Semantic search in your PDFs | 
        <a href="https://github.com/AmineMOULAI" style="color: #90EE90;">GitHub</a> | 
        Made with ❤️ for UPVD L3 GL</p>
    </div>
    <style>
        .stApp { 
            padding-bottom: 100px; 
        }
    </style>
    """, unsafe_allow_html=True)