import streamlit as st
import streamlit.components.v1 as components

# 1. Configurare pagină (Wide layout)
st.set_page_config(
    page_title="NeuroSplit Suite",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Ascundem elementele standard Streamlit pentru imersiune
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0; margin: 0;}
    
    /* Stilizare Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #09090b;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    div[data-testid="stSidebarNav"] {
        padding-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Meniul de Navigare (Sidebar)
st.sidebar.title("🧠 NeuroSplit")
st.sidebar.markdown("---")
app_mode = st.sidebar.radio(
    "Alege Modul:",
    ["🛠️ The Architect (Generator)", "🎮 The Arena (Quiz Player)"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("Selectează 'Architect' pentru a crea prompturi AI sau 'Arena' pentru a juca grilele generate.")

# 4. Funcția de încărcare HTML
def load_html(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1 style='color:red'>Eroare: Nu am găsit fișierul {file_name}!</h1>"

# 5. Afișarea conținutului în funcție de selecție
if app_mode == "🛠️ The Architect (Generator)":
    html_code = load_html("generator.html")
    # Height mare pentru generator
    components.html(html_code, height=1300, scrolling=True)

elif app_mode == "🎮 The Arena (Quiz Player)":
    html_code = load_html("game.html")
    # Height pentru joc
    components.html(html_code, height=1200, scrolling=True)
