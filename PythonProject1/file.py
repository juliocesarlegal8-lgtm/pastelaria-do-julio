import streamlit as st
import random
import resend
from datetime import datetime

# Configuração da página (Design Mobile Premium / Responsivo)
st.set_page_config(page_title="Pastel do Júlio - Premium", page_icon="🥟", layout="wide")

# =========================================================================
# 🎨 ARQUITETURA DE DESIGN PREMIUM (CSS CUSTOMIZADO)
# =========================================================================
st.markdown("""
    <style>
    /* Fundo geral da aplicação */
    .stApp {
        background-color: #0d0d0d !important;
        color: #f2f2f2 !important;
    }
    
    /* Customização dos Títulos */
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', 'Georgia', serif !important;
        letter-spacing: 1px;
    }
    
    /* Caixa de Alerta de Erro/Aviso Customizada */
    .stAlert {
        background-color: #1a1510 !important;
        color: #e6b800 !important;
        border: 1px solid #bd9313 !important;
        border-radius: 12px !important;
    }
    
    /* Inputs de Texto Premium */
    .stTextInput>div>div>input {
        background-color: #141414 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 8px rgba(212, 175, 55, 0.4) !important;
    }

    /* Botão Principal Dourado (Confirmar) */
    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg, #d4af37 0%, #aa7c11 100%) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 14px 20px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4) !important;
    }

    /* Botão Secundário (Adicionar e Limpar) */
    .stButton>button[kind="secondary"] {
        background-color: #191919 !important;
        color: #d4af37 !important;
        border: 1px solid #aa7c11 !important;
        border-radius: 6px !important;
        transition: all 0.2s ease !important;
        width: 100%;
    }
    .stButton>button[kind="secondary"]:hover {
        background-color: #d4af37 !important;
        color: #000000 !important;
    }

    /* Estilização dos Menus Retráteis (Expanders) */
    .streamlit-expanderHeader {
        background-color: #141414 !important;
        border: 1px solid #262626 !important;
        border-radius: 8px !important;
        color: #e6e6e6 !important;
        font-weight: 600 !important;
    }
    .streamlit-expanderContent {
        background-color: #0d0d0d !important;
        border-left: 1px solid #aa7c11 !important;
        border-right: 1px solid #262626 !important;
        border-bottom: 1px solid #262626 !important;
        border-bottom-left-radius: 8px !important;
        border-bottom-right-radius: 8px !important;
    }

    /* Caixa do Ticket de Alta Linha */
    .ticket-premium { 
        background: linear-gradient(145deg, #14110c 0%, #0d0b08 100%);
        color: #f2f2f2; 
        padding: 30px; 
        border-radius: 16px; 
        text-align: center; 
        border: 1px solid #aa7c11;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
        margin-top: 20px;
    }
    .ticket-header {
        color: #d4af37 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        text-transform: uppercase;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho de Luxo
st.markdown("<h1 style='text-align: center; color: #d4af37; font-size: 3rem; margin-bottom: 0; font-weight: 800;'>PASTEL DO JÚLIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; letter-spacing: 2px; color: #8c8c8c; text-transform: uppercase;'>Experiência Gastronômica Artesanal</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 15px; color: #aa7c11;'>📍 Retirada Exclusiva: Trailer Branco — Morada do Sol, Indaiatuba - SP</p>", unsafe_allow_html=True)
st.markdown("<div style='border-bottom: 1px solid #aa7c11; margin: 20px 0;'></div>", unsafe_allow_html=True)

# =========================================================================
# 💰 INFORMAÇÕES DE PAGAMENTO NA BARRA LATERAL
# =========================================================================
st.sidebar.markdown("<h3 style='color: #d4af37;'>Políticas de Pagamento</h3>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style='background-color: #141414; padding: 15px; border-radius: 8px; border-left: 3px solid #d4af37; font-size: 14px;'>
<b style='color: #ffffff;'>📱 Retiradas Agendadas:</b><br>
Aceitas exclusivamente via <b>PIX</b> de forma antecipada.<br><br>
<b style='color: #ea2027;'>⏱️ Prazo de Tolerância:</b><br>
O PIX deve ser efetuado em até <b>5 minutos</b> após o pedido, ou a reserva será desconsiderada.<br><br>
<b style='color: #ffffff;'>🤝 Compra Presencial:</b><br>
Dinheiro e cartões de débito são aceitos apenas diretamente no balcão do Trailer.
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='color: #aa7c11; margin-bottom:5px;'>Dados para Depósito</h4>", unsafe_allow_html=True)
st.sidebar.code("Chave PIX: 19991692630\nFavorecido: Marcos Prado", language="text")

# 📋 CARDÁPIO 100% COMPLETO (TODOS OS ITENS UNIFICADOS)
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
    <h3>🔥 NOVO PEDIDO CHEGOU - PASTEL DO JÚLIO 🔥</h3>
    <p>--------------------------------------------------</p>
    <p><strong>🎟️ TICKET DO CLIENTE:</strong> #{num_ticket}</p>
    <p><strong>👤 NOME DO CLIENTE:</strong> {nome_cli}</p>
    <p><strong>📱 WHATSAPP DO CLIENTE:</strong> {whats_cli}</p>
    <p><strong>✉️ E-MAIL DO CLIENTE:</strong> {email_cli}</p>
    <p><strong>⏰ HORÁRIO DE RETIRADA NO TRAILER:</strong> {hora_busca}h</p>
    <p>--------------------------------------------------</p>
    <p><strong>📋 ITENS PARA PRODUÇÃO:</strong><br>{lista_formatada}</p>
    <p>--------------------------------------------------</p>
    <p><strong>💰 VALOR TOTAL A COBRAR:</strong> R$ {total_pagar:.2f} (Aguardando PIX em 5 min)</p>
    <p>📍 <strong>LOCAL DE RETIRADA:</strong> Trailer Branco (Morada do Sol, Indaiatuba - SP, 13348-070)</p>
    """

    try:
        resend.Emails.send({
            "from": "Pastelaria do Julio <onboarding@resend.dev>",
            "to": "juliocesarlegal8@gmail.com",
            "subject": f"🥟 NOVO PEDIDO - Ticket #{num_ticket} - {nome_cli}",
            "html": corpo_html
        })
        return True
    except Exception as e:
        print(f"Erro no envio da API do Resend: {e}")
        return False

# Organização da tela do sistema em 2 colunas principais
col_cardapio, col_carrinho = st.columns(2)

with col_cardapio:
    st.markdown("<h3 style='color: #d4af37;'>✨ Cardápio Exclusivo</h3>", unsafe_allow_html=True)
    
    with st.expander("👑 1) Pastéis Tradicionais - R$ 14,00"):
        for nome in cardapio["Tradicionais"]:
            c1, c2 = st.columns(2)
            c1.write(f"**{nome}**")
            if c2.button("Selec.", key=f"simples_{nome}", type="secondary"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("🌟 2) Pastéis Combinados"):
        for nome, preco in cardapio["Combinados"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — <span style='color:#d4af37;'>{texto_preco}</span>", unsafe_allow_html=True)
            if c2.button("Selec.", key=f"comb_{nome}", type="secondary"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("💎 3) Pastéis Especiais"):
        for nome, preco in cardapio["Especiais"].items():
            c1, c2 = st.columns(2)
