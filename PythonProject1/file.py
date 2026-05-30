st.set_page_config(
    page_title="🚚 Trailer do Marcos & JULIO",
    page_icon="🚚",
    layout="wide"
)

st.markdown("""
<style>

/* FUNDO */
.stApp{
    background:linear-gradient(
        135deg,
        #050505,
        #120024,
        #001f3f,
        #000000
    );
}

/* TEXTO GERAL */
html, body, p, div, span, label {
    color:white !important;
}

/* TÍTULOS */
h1{
    color:#00ffff !important;
    text-shadow:
        0 0 5px #00ffff,
        0 0 10px #00ffff,
        0 0 20px #00ffff,
        0 0 40px #00ffff;
}

h2,h3{
    color:#ff00ff !important;
    text-shadow:
        0 0 5px #ff00ff,
        0 0 10px #ff00ff;
}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #18002f,
        #000814
    );
}

/* BOTÕES */
.stButton > button{
    width:100%;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        90deg,
        #ff00ff,
        #00ffff
    );
    color:white !important;
    font-weight:bold;
    box-shadow:
        0 0 10px #00ffff,
        0 0 20px #ff00ff;
}

.stButton > button:hover{
    box-shadow:
        0 0 20px #00ffff,
        0 0 40px #ff00ff;
}

/* CAMPOS */
.stTextInput input,
.stTimeInput input{
    background:#111 !important;
    color:white !important;
    border:2px solid #00ffff !important;
    box-shadow:0 0 10px #00ffff;
}

/* EXPANDERS (CATEGORIAS) */
.streamlit-expanderHeader{
    color:#00ffff !important;
    font-weight:bold !important;
    text-shadow:
        0 0 5px #00ffff,
        0 0 10px #00ffff;
}

/* TODAS AS MENSAGENS */
.stAlert{
    border-radius:12px;
}

/* ITENS DO CARDÁPIO */
strong{
    color:#39ff14 !important;
    text-shadow:
        0 0 5px #39ff14,
        0 0 10px #39ff14;
}

/* LINHAS */
hr{
    border:1px solid #00ffff;
    box-shadow:0 0 10px #00ffff;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="text-align:center;">
🚚 TRAILER DO MARCOS & JULIO 🚚
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style="text-align:center;">
🌈 Pastéis • Hambúrgueres • Bebidas • Caldo de Cana 🌈
</h3>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center;font-size:18px;">
📍 Retirada no Trailer Branco<br>
Morada do Sol - Indaiatuba/SP | CEP 13348-070
</p>
""", unsafe_allow_html=True)

st.divider()
