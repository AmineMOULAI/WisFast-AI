import streamlit as st 
import os

with st.container(border=False, horizontal =True,horizontal_alignment = "center", vertical_alignment="top"):
    st.image(os.path.join(os.getcwd(), "docs/WisFast.png"), width=300)
    #st.title("WisFast")
    st.header("Smart search in your books")


def main():

    file = st.file_uploader("Upload your book")
    print(file)
    query = st.text_input("What are you looking for ...?", "What are you looking for ...?", label_visibility="hidden")
    print(query)

    st.divider()

    fb = st.feedback("stars")
    print(fb)


def book1():
    st.title("Book 1")

def book2():
    st.title("Book 2")

def book3():
    st.title("Book 3")

pages = {
    "main" : main,
    "Book 1" : book1, 
    "Book 2 " : book2, 
    "Book 3" : book3
         }

selected_page = st.sidebar.selectbox("Choose a Book", options=pages.keys())
print(selected_page)
pages[selected_page]()