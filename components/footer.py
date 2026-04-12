import streamlit as st

def footer():
    # We remove 'position: fixed' so it stays in the flow of the main content 
    # and follows the sidebar status naturally.
    st.markdown("""
    <style>
    .custom-footer {
        margin-top: 5rem;
        margin-bottom: 2rem;
        width: 100%; 
        background: rgba(4, 110, 92, 0.1);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        color: white; 
        text-align: center; 
        padding: 20px; 
        font-size: 14px;
        border-radius: 24px;
        border: 1px solid rgba(78, 205, 196, 0.1);
        transition: all 0.4s ease;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        flex-wrap: wrap;
    }
    .custom-footer:hover {
        background: rgba(4, 110, 92, 0.2);
        border-color: rgba(78, 205, 196, 0.3);
    }
    .footer-item {
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .footer-link {
        color: #4ecdc4 !important;
        text-decoration: none;
        font-weight: 700;
        transition: color 0.3s ease;
    }
    .footer-link:hover {
        color: #ffffff !important;
        text-decoration: underline;
    }
    .footer-divider {
        opacity: 0.3;
        color: #a0aec0;
    }
    /* Responsive adjustment */
    @media (max-width: 600px) {
        .custom-footer {
            flex-direction: column;
            gap: 10px;
        }
        .footer-divider {
            display: none;
        }
    }
    </style>
    <div class="custom-footer">
        <div class="footer-item">
            ⚡ <b>WisFast AI</b>
        </div>
        <span class="footer-divider">|</span>
        <div class="footer-item">
            Built by <b>Amine Moulai</b>
        </div>
        <span class="footer-divider">|</span>
        <div class="footer-item">
            📧 <a class="footer-link" href="mailto:moulaiamine01@gmail.com">moulaiamine01@gmail.com</a>
        </div>
        <span class="footer-divider">|</span>
        <div class="footer-item">
            👨‍💻 <a class="footer-link" href="https://github.com/AmineMOULAI" target="_blank">GitHub Portfolio</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
