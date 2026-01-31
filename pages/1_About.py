import time
import os
import streamlit as st
from components.footer import footer
from components.warning import warning


bolt = os.path.join(os.getcwd(), "docs/bolt.png")
st.logo(bolt, size="large")

with st.container(border=False, horizontal =True,horizontal_alignment = "center", vertical_alignment="top"):
    st.image(os.path.join(os.getcwd(), "docs/WisFast.png"), width=300)

about = """
transforms your PDF documents into a smart research assistant. Upload any book or lengthy file, ask questions in plain language like "conseils patience face épreuves," and instantly get the top 5 most relevant pages with helpful context excerpts.​
"""
mission = """
Tired of Ctrl+F searches that bury you under 50 irrelevant pages? We solve that frustration by delivering precise results in seconds, saving you 30-45 minutes per research session. Perfect for students tackling philosophy texts on Stoicism, researchers scanning reports, or anyone with dense PDFs.​
"""
funct = """
Simply upload your PDF (up to 200 pages), type your question, and watch the magic. We analyze the content to surface exactly what you need—no more wasted time flipping pages.
"""
creation = """
Developed for the L3 Computer Science Software Engineering course at Université de Perpignan Via Domitia (UPVD), under Benjamin Antunes. Due April 12, 2026. [**Amine Moulai**](https://github.com/AmineMOULAI) building real-world skills.​
"""
txt = [about, mission, funct, creation]
badges = ["WisFast AI", "Our Mission", "How it works", "Created At"]
def aboutWis():
    for badge, t in zip(badges, txt):
        yield f"**{badge}** \n\n"
        for word in t.split(" "):
            yield word + " "
            time.sleep(0.02)

        yield "\n\n"

if st.button("**WisFast**", width="stretch"):
    st.write_stream(aboutWis())
    warning()

footer()