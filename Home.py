import streamlit as st 
import os
from components.footer import footer
from components.warning import warning


with st.container(border=False, horizontal =True, horizontal_alignment = "center", vertical_alignment="bottom"):
    st.image(os.path.join(os.getcwd(), "docs/WisFast.png"), width=300)
    #st.title("WisFast")
    st.header("Smart search in your books", text_alignment="center")

st.divider()

bolt = os.path.join(os.getcwd(), "docs/bolt.png")
st.logo(bolt, size="large")

file = st.file_uploader("Upload your book")
print(file)


with st.container(border = False, horizontal = True, horizontal_alignment = "center", vertical_alignment = "top"):
    search, startSearch = st.columns([6, 1], gap="small", vertical_alignment="bottom")

    search.space("xxsmall")
    startSearch.space("small")
    query = search.text_input("What are you looking for ...?", "What are you looking for ...?", label_visibility="hidden")
    icon_path = os.path.join(os.getcwd(), "docs/search.png")
    search_button = startSearch.button("", icon="🔍", width="content")

    if search_button:
        print(f"Searching for : {query}")

st.divider()

#warning()
fb = st.feedback("stars")


footer()


st.markdown("""
<style>
div.stButton > button {
    width: 50px;
    height: 50px;
    background-color : #046e5c;
    color: white;
    border-radius: 50%;    
    box-shadow: 
        0 0 20px rgba(78, 205, 196, 0.6),  /* Outer glow */
        inset 0 2px 10px rgba(255,255,255,0.3),  /* Inner highlight */
        0 8px 20px rgba(0,0,0,0.2);  /* Drop shadow */
    transition: all 0.3s ease;        
}

div.stButton > button:hover{
    background-color: white;
    color : #046e5c;
    transform: scale(1.05);

            }          
</style>


""", unsafe_allow_html=True)

