# Configuração da página
st.set_page_config(
    page_title="Trailer do Marcos & JULIO",
    page_icon="🌈",
    layout="wide"
)

# Tema Neon
st.markdown("""
<style>
/* Fundo geral */
.stApp {
    background: linear-gradient(135deg, #050505, #120024, #001f3f);
    color: white;
}

/* Área principal */
.main {
    background-color: transparent;
}

/* Títulos */
h1 {
    color: #00ffff !important;
    text-shadow: 0 0 10px #00ffff,
                 0 0 20px #00ffff,
                 0 0 40px #00ffff;
}

h2, h3 {
    color: #ff00ff !important;
    text-shadow: 0 0 8px #ff00ff;
}

/* Botões */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 2px solid #00ffff;
    background: linear-gradient(90deg, #ff00ff, #00ffff);
    color: white;
    font-weight: bold;
    box-shadow: 0 0 15px #00ffff;
}

.stButton > button:hover {
    box-shadow: 0 0 25px #ff00ff;
    transform: scale(1.03);
}

/* Inputs */
.stTextInput input,
.stTimeInput input {
    background-color: #111;
    color: white;
    border: 1px solid #00ffff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a0033, #000814);
}

/* Expansores */
.streamlit-expanderHeader {
    color: #00ffff !important;
    font-weight: bold;
}

/* Cartões */
div[data-testid="stVerticalBlock"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
