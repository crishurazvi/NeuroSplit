import streamlit as st
import streamlit.components.v1 as components

# 1. Configurare pagină (Wide layout)
st.set_page_config(
    page_title="NeuroSplit Suite",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded" # Forțăm meniul să fie deschis la start
)

# 2. CSS REPARAT (Safe Mode)
st.markdown("""
<style>
    /* Ascundem meniul standard din dreapta sus (cele 3 liniuțe) și footer-ul "Made with Streamlit" */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* CRITIC: Nu ascundem header-ul complet, ci doar îl facem transparent.
       Astfel, butonul de sidebar rămâne vizibil și funcțional.
    */
    header {
        background-color: transparent !important;
    }
    
    /* Ajustăm spațierea de sus ca să nu fie o gaură mare */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }

    /* Stilizare Sidebar pentru aspect "Dark Mode" curat */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF; /* Același negru ca în aplicația ta */
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Facem textul din sidebar mai vizibil */
    div[data-testid="stSidebarNav"] * {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Meniul de Navigare (Sidebar)
with st.sidebar:
    st.title("🧠 NeuroSplit")
    st.markdown("---")
    
    # Folosim Radio Button pentru navigare
    app_mode = st.radio(
        "Navigare:",
        ["🛠️ The Architect", "🎮 The Arena"],
        index=0,
        help="Alege între generatorul de prompturi și zona de joc."
    )
    
    st.markdown("---")
    
    # Instrucțiuni contextuale
    if app_mode == "🛠️ The Architect":
        st.info("Folosește această pagină pentru a transforma cursurile în prompturi AI.")
    else:
        st.success("Încarcă fișierul .txt generat pentru a începe sesiunea de învățare.")

# 4. Funcția de încărcare HTML
def load_html(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"""
        <div style='color: #fb7185; background: #2d1215; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2>⚠️ Fișier lipsă: {file_name}</h2>
            <p>Asigură-te că fișierele <b>generator.html</b> și <b>game.html</b> sunt în același folder cu app.py.</p>
        </div>
        """

# 5. Logică Afișare
if app_mode == "🛠️ The Architect":
    # Generatorul are nevoie de mai mult spațiu vertical
    html_code = load_html("generator.html")
    components.html(html_code, height=1400, scrolling=True)

elif app_mode == "🎮 The Arena":
    # Jocul
    html_code = load_html("game.html")
    components.html(html_code, height=1200, scrolling=True)
