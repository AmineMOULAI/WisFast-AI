import streamlit as st
import os
from components.footer import footer
from wisfast.ui.styles import apply_custom_styles

apply_custom_styles()

# Animation container
st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# Hero Section for About Page
col1, col2 = st.columns([1, 2], vertical_alignment="center")
with col1:
    st.image("assets/WisFast.png", width='stretch')
with col2:
    st.markdown("""
    # REIMAGINING RESEARCH
    ### BEYOND THE LIMITS OF CTRL+F
    """)

st.markdown("---")

# Main Content with Custom Styling
st.markdown("""
<style>
    .about-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(4, 110, 92, 0.1);
        margin-bottom: 2rem;
    }
    .feature-header {
        color: #046e5c;
        font-family: 'Squada One', cursive;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    .about-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #444;
    }
    .highlight {
        color: #046e5c;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="about-card">
        <div class="feature-header">THE VISION</div>
        <p class="about-text">
            <span class="highlight">WisFast AI</span> was born from a simple frustration: 
            the traditional way of searching through large documents is broken. 
            Standard keyword matching is too literal, often missing the context that matters most. 
            I built this tool to bridge that gap, using <span class="highlight">Semantic Search</span> 
            to understand the <i>intent</i> behind your questions, not just the words.
        </p>
    </div>
    """, unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div class="about-card">
        <div class="feature-header">SMART INDEXING</div>
        <p class="about-text">
            By leveraging advanced <b>TF-IDF algorithms</b> and <b>Cosine Similarity</b>, 
            WisFast transforms flat PDF text into a multi-dimensional knowledge base. 
            It analyzes page relevance in milliseconds.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="about-card">
        <div class="feature-header">YOUR DATA, SECURE</div>
        <p class="about-text">
            This is a <b>privacy-first</b> application. All processing happens locally or on your dedicated 
            instance. Your documents are indexed into a private SQLite database, 
            ensuring your research stays yours.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="about-card" style="text-align: center;">
    <div class="feature-header">CRAFTED BY AMINE MOULAI</div>
    <p class="about-text">
        A passion project focused on pushing the boundaries of what's possible with 
        Python and Natural Language Processing. Built for researchers, students, 
        and anyone who values their time.
    </p>
    <br>
    <a href="https://github.com/AmineMOULAI" target="_blank" style="text-decoration: none;">
        <button style="
            background-color: #046e5c;
            color: white;
            padding: 10px 30px;
            border-radius: 50px;
            border: none;
            font-family: 'Squada One', cursive;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(4, 110, 92, 0.3);
        ">VIEW PORTFOLIO</button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

footer()
