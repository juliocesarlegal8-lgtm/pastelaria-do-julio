import streamlit as st
import random
import resend
from datetime import datetime

# Configuração da página (Design Mobile / Responsivo em Estilo Neon)
st.set_page_config(page_title="Pastel do Júlio - Neon", page_icon="⚡", layout="wide")

# =========================================================================
# 🎛️ ARQUITETURA DE DESIGN NEON FORTE (CSS NEON INJETADO)
# =========================================================================
st.markdown("""
    <style>
    /* Fundo escuro absoluto para destacar o neon */
    .stApp {
        background-color: #050505 !important;
        color: #ffffff !important;
    }
    
    /* Títulos com efeito de brilho Neon */
    h1 {
        color: #00ff66 !important;
        font-family: 'Arial Black', Gadget, sans-serif !important;
        text-shadow: 0 0 10px #00ff66, 0 0 20px #00ff66, 0 0 40px #00ff66 !important;
    }
    h2, h3, h5 {
        color: #ff007f !important;
        font-family: 'Arial Black', Gadget, sans-serif !important;
        text-shadow: 0 0 8px #ff007f, 0 0 15px #ff007f !important;
    }
    
    /* Caixas de Alerta e Avisos em Neon */
    .stAlert {
        background-color: #0f0008 !important;
        color: #ff007f !important;
        border: 2px solid #ff007f !important;
        border-radius: 12px !important;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.4) !important;
    }
    
    /* Inputs de Texto com bordas brilhantes */
    .stTextInput>div>div>input {
        background-color: #111111 !important;
        color: #00ff66 !important;
        border: 2px solid #333333 !important;
        border-radius: 8px !important;
        font-weight: bold !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00ff66 !important;
        box-shadow: 0 0 15px #00ff66 !important;
    }

    /* Botão de Confirmação - Verde Neon Pulsante */
    .stButton>button[kind="primary"] {
        background-color: #00ff66 !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 15px !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px #00ff66 !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #ffffff !important;
        box-shadow: 0 0 35px #ffffff, 0 0 10px #00ff66 !important;
        transform: scale(1.02) !important;
    }

    /* Botão de Adicionar - Rosa Fluorescente */
    .stButton>button[kind="secondary"] {
        background-color: #000000 !important;
        color: #ff007f !important;
        border: 2px solid #ff007f !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 8px rgba(255, 0, 127, 0.3) !important;
        width: 100%;
    }
    .stButton>button[kind="secondary"]:hover {
        background-color: #ff007f !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #ff007f !important;
    }

    /* Menus de Categorias (Expanders) no estilo Cyberpunk */
    .streamlit-expanderHeader {
        background-color: #111111 !important;
        border: 2px solid #00ff66 !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        box-shadow: 0 0 10px rgba(0, 255, 102, 0.2) !important;
    }
    .streamlit-expanderContent {
        background-color: #050505 !important;
        border-left: 2px solid #ff007f !important;
        border-right: 2px solid #00ff66 !important;
        border-bottom: 2px solid #00ff66 !important;
        border-bottom-left-radius: 8px !important;
        border-bottom-right-radius: 8px !important;
    }

    /* Caixa do Ticket Final em Estilo Painel Futurista */
    .ticket-neon { 
        background-color: #000000;
        color: #ffffff; 
        padding: 30px; 
        border-radius: 16px; 
        text-align: center; 
        border: 3px solid #00ff66;
        box-shadow: 0 0 30px rgba(0, 255, 102, 0.6);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Neon
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 0;'>⚡ PASTEL DO JÚLIO ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #00ff66; font-weight: bold; letter-spacing: 3px; text-transform: uppercase;'>Sabor de Alta Voltagem</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #ffffff;'>📍 RETIRADA: <span style='color:#ff007f; font-weight:bold;'>TRAILER BRANCO</span> — Morada do Sol, Indaiatuba - SP</p>", unsafe_allow_html=True)
st.markdown("<div style='border-bottom: 2px solid #ff007f; box-shadow: 0 0 10px #ff007f; margin: 20px 0;'></div>", unsafe_allow_html=True)

# =========================================================================
# 💰 INFORMAÇÕES DE PAGAMENTO NA BARRA LATERAL (NEON)
# =========================================================================
st.sidebar.markdown("<h2 style='font-size:22px; text-align:center;'>⚡ PAGAMENTO ⚡</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style='background-color: #111111; padding: 15px; border-radius: 8px; border: 2px solid #ff007f; box-shadow: 0 0 10px rgba(255,0,127,0.4); font-size: 14px;'>
<b style='color: #00ff66;'>📱 RETIRADAS VIA SITE:</b><br>
Aceitas exclusivamente via <b>PIX</b> de forma antecipada.<br><br>
<b style='color: #ff0000;'>⏱️ PRAZO DO CRONÔMETRO:</b><br>
Faça o PIX em até <b>5 minutos</b> ou seu pedido será cancelado no sistema.<br><br>
<b style='color: #ffffff;'>💵 COMPRA LOCAL:</b><br>
Dinheiro e Débito somente no balcão presencial do Trailer.
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.code("CHAVE PIX (CELULAR):\n19991692630\n\nFAVORECIDO:\nMarcos Prado", language="text")

# 📋 CARDÁPIO TOTALMENTE COMPLETO RECONSTITUÍDO
cardapio = {
    "Tradicionais": ["Queijo", "Carne", "Frango", "Cheddar", "Calabresa"],
    "Combinados": {
        "Carne com Queijo": 17.00, "Frango com Requeijão": 16.00, "Calabresa com Queijo": 16.00,
        "Presunto e Queijo": 16.00, "Cheddar com Carne": 17.00, "Cheddar com Frango": 16.00
    },
    "Especiais": {
        "Cheddar com Frango e Requeijão": 19.00, "Calabresa com Cheddar": 18.00, "Especial Queijo e Presunto": 20.00,
        "Mega Queijo (4 Fatias)": 20.00, "Carne com Cheddar e Requeijão": 19.00, "Calabresa Suprema": 18.00,
        "A Moda do Júlio": 22.00, "Bomba de Frango": 22.00
    },
    "Imperiais": {
        "O Fenomenal (O Rei)": 26.00, "Imperial de Carne": 25.00, "Super Frangresa": 23.00,
        "Misto Cremoso": 22.00, "Misto do Júlio": 22.00
    },
    "Hambúrgueres": {
        "Hambúrguer Assado": 9.00
    },
    "Bebidas": {
        "Caldo de Cana (Copo 500ml)": 10.00, 
        "Caldo de Cana (Copo 770ml)": 14.00,
        "Caldo de Cana (Garrafa 500ml)": 11.00, 
        "Caldo de Cana (Garrafa 1 Litro)": 21.00,
        "Água de Coco": 10.00
    }
}

if "carrinho" not in st.session_state:
    st.session_state.carrinho = {}
if "ticket_gerado" not in st.session_state:
    st.session_state.ticket_gerado = None

# FUNÇÃO QUE FAZ O ENVIO DIRETO PARA O SEU GMAIL UTILIZANDO SUA API KEY DO RESEND
def disparar_email_producao(num_ticket, nome_cli, whats_cli, email_cli, hora_busca, itens_sacola, total_pagar):
    resend.api_key = "re_gRHuzJpe_EybdTWWETWpKh2bGSB4qBUrE"

    lista_formatada = ""
    for produto, quantidade in itens_sacola.items():
        lista_formatada += f"• {quantidade}x {produto}<br>"

    corpo_html = f"""
    <h3>⚡ NOVO PEDIDO NEON - PASTEL DO JÚLIO ⚡</h3>
    <p>--------------------------------------------------</p>
    <p><strong>🎟️ TICKET:</strong> #{num_ticket}</p>
    <p><strong>👤 CLIENTE:</strong> {nome_cli}</p>
    <p><strong>📱 WHATSAPP:</strong> {whats_cli}</p>
    <p><strong>✉️ E-MAIL:</strong> {email_cli}</p>
    <p><strong>⏰ HORÁRIO RETIRADA:</strong> {hora_busca}h</p>
    <p>--------------------------------------------------</p>
    <p><strong>📋 ITENS DO PEDIDO:</strong><br>{lista_formatada}</p>
    <p>--------------------------------------------------</p>
    <p><strong>💰 TOTAL A COBRAR:</strong> R$ {total_pagar:.2f} (Aguardando PIX)</p>
    <p>📍 <strong>LOCAL:</strong> Trailer Branco (Morada do Sol, Indaiatuba - SP)</p>
    """

    try:
        resend.Emails.send({
            "from": "Pastelaria do Julio <onboarding@resend.dev>",
            "to": "juliocesarlegal8@gmail.com",
            "subject": f"⚡ NOVO PEDIDO - Ticket #{num_ticket} - {nome_cli}",
            "html": corpo_html
        })
        return True
    except Exception as e:
        print(f"Erro no envio da API do Resend: {e}")
        return False

# Organização da tela do sistema em 2 colunas principais
col_cardapio, col_carrinho = st.columns(2)

with col_cardapio:
    st.markdown("<h3>⚡ SELECIONE OS SABORES</h3>", unsafe_allow_html=True)
    
    with st.expander("🟢 1) Pastéis Tradicionais - R$ 14,00"):
        for nome in cardapio["Tradicionais"]:
            c1, c2 = st.columns(2)
            c1.write(f"**{nome}**")
            if c2.button("+ Add", key=f"simples_{nome}", type="secondary"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("🟢 2) Pastéis Combinados"):
        for nome, preco in cardapio["Combinados"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — <span style='color:#00ff66;'>{texto_preco}</span>", unsafe_allow_html=True)
            if c2.button("+ Add", key=f"comb_{nome}", type="secondary"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("🟢 3) Pastéis Especiais"):
