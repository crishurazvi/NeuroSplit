import streamlit as st
import streamlit.components.v1 as components

# 1. Configurare pagină pentru a folosi tot spațiul
st.set_page_config(
    page_title="NeuroSplit Quiz Arena",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Ascundem meniul standard Streamlit și footer-ul pentru un look "clean"
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Citim fișierul HTML
def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

html_code = load_html()

# 4. Randăm HTML-ul în Streamlit
# height=1200 asigură că avem destul loc pe verticală fără scroll dublu
components.html(html_code, height=1200, scrolling=True)
