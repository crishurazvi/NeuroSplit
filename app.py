import streamlit as st
import streamlit.components.v1 as components

# 1. Configurare pagină
st.set_page_config(
    page_title="NeuroSplit Suite",
    page_icon="🧠",
    layout="wide"
)

# 2. CSS minimal (ascundem doar footer-ul și meniul hamburger, dar lăsăm header-ul pentru layout corect)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    
    /* Stilizare Tab-uri pentru a fi mai mari */
    button[data-baseweb="tab"] {
        font-size: 1.2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. Titlu Principal
st.title("🧠 NeuroSplit Suite")

# 4. Funcția de încărcare HTML
def load_html(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1 style='color:red'>Eroare: Nu am găsit fișierul {file_name}!</h1>"

# 5. Crearea Tab-urilor (Navigația)
tab_generator, tab_joc = st.tabs(["🛠️ The Architect (Generator)", "🎮 The Arena (Quiz Player)"])

with tab_generator:
    html_code = load_html("generator.html")
    components.html(html_code, height=1300, scrolling=True)

with tab_joc:
    html_code = load_html("game.html")
    components.html(html_code, height=1200, scrolling=True)
