import streamlit as st
import random
import resend
from datetime import datetime

# Configuração da página (Design Mobile / Responsivo)
st.set_page_config(page_title="Pastel do Júlio & MarcosCaldodeCana - Pedidos", page_icon="🥟", layout="wide")

# Estilo visual focado em conversão e usabilidade mobile
st.markdown("<style>.main { background-color: #fffdf9; } .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }</style>", unsafe_allow_html=True)

# Cabeçalho Oficial com o endereço completo do Trailer Branco
st.markdown("<h1 style='text-align: center; color: #e67e22; margin-bottom: 0;'>🥟 PASTEL DO JÚLIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 15px; font-weight: bold; color: #4a3319;'>📍 Retirada: Trailer Branco<br>Morada do Sol, Indaiatuba - SP | CEP: 13348-070</p>", unsafe_allow_html=True)
st.divider()

# =========================================================================
# 💰 INFORMAÇÕES DE PAGAMENTO E REGRAS DE TEMPO LIMEITE
# =========================================================================
st.sidebar.markdown("### 💰 Regras de Pagamento")
st.sidebar.warning("⚠️ **PEDIDOS PARA RETIRADA:** O pagamento deve ser feito obrigatoriamente via **PIX** após gerar o seu Ticket.")
st.sidebar.error("⏱️ **ATENÇÃO:** O pagamento via PIX é válido por até **5 minutos**. Caso o pagamento não seja confirmado dentro desse prazo, o pedido será **cancelado automaticamente**.")
st.sidebar.info("""
**Chave PIX (Celular):** 
`19991692630`
**Nome do Cobrador:** 
Marcos Prado
""")
st.sidebar.success("💵 **Dinheiro e Débito:** Aceitos somente para compras feitas presencialmente no Trailer Branco.")
# =========================================================================

# Cardápio completo
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
    st.subheader("🛒 Monte seu Pedido")
    
    with st.expander("1) Pastéis Tradicionais - R$ 14,00"):
        for nome in cardapio["Tradicionais"]:
            c1, c2 = st.columns(2)
            c1.write(f"**{nome}**")
            if c2.button("Adicionar", key=f"simples_{nome}"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("2) Pastéis Combinados"):
        for nome, preco in cardapio["Combinados"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — {texto_preco}")
            if c2.button("Adicionar", key=f"comb_{nome}"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("3) Pastéis Especiais"):
        for nome, preco in cardapio["Especiais"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — {texto_preco}")
            if c2.button("Adicionar", key=f"esp_{nome}"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("4) Pastéis Imperiais (Os Gigantes)"):
        for nome, preco in cardapio["Imperiais"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — {texto_preco}")
            if c2.button("Adicionar", key=f"imp_{nome}"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("🍔 Hambúrgueres"):
        for nome, preco in cardapio["Hambúrgueres"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — {texto_preco}")
            if c2.button("Adicionar", key=f"burguer_{nome}"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

    with st.expander("🥤 Bebidas"):
        for nome, preco in cardapio["Bebidas"].items():
            c1, c2 = st.columns(2)
            texto_preco = f"R$ {preco:.2f}".replace('.', ',')
            c1.write(f"**{nome}** — {texto_preco}")
            if c2.button("Adicionar", key=f"beb_{nome}"):
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.rerun()

with col_carrinho:
    st.subheader("🛍️ Dados da Retirada")
    
    # Alerta móvel reforçado com o tempo limite
    st.error("⚠️ **Aviso Importante:** Pedidos para retirada aceitam apenas **PIX**. O pagamento deve ser feito em até **5 minutos** ou o pedido será cancelado.")
    
    nome_cliente = st.text_input("Seu Nome:", placeholder="Ex: João Silva")
    whats_cliente = st.text_input("Seu WhatsApp com DDD (Obrigatório):", placeholder="Ex: 19999999999")
    email_cliente = st.text_input("Seu E-mail:", placeholder="Ex: cliente@email.com")
    horario_busca = st.time_input("Horário programado para buscar no Trailer:", value=datetime.now().time())
    
    st.divider()
    st.write("### 📋 Resumo da Sacola")
    
    if not st.session_state.carrinho:
        st.info("Adicione os itens desejados no menu ao lado.")
        total_geral = 0.0
    else:
        total_geral = 0.0
        for nome_item, qtd in list(st.session_state.carrinho.items()):
            preco_item = 14.00
            if nome_item in cardapio["Combinados"]: preco_item = cardapio["Combinados"][nome_item]
            elif nome_item in cardapio["Especiais"]: preco_item = cardapio["Especiais"][nome_item]
            elif nome_item in cardapio["Imperiais"]: preco_item = cardapio["Imperiais"][nome_item]
            elif nome_item in cardapio["Hambúrgueres"]: preco_item = cardapio["Hambúrgueres"][nome_item]
            elif nome_item in cardapio["Bebidas"]: preco_item = cardapio["Bebidas"][nome_item]
            
            subtotal = preco_item * qtd
            total_geral += subtotal
            st.write(f"**{qtd}x** {nome_item} — R$ {subtotal:.2f}".replace('.', ','))
        
        st.markdown(f"#### **Total: R$ {total_geral:.2f}**".replace('.', ','))
        
        if st.button("Limpar Sacola", type="secondary"):
            st.session_state.carrinho = {}
            st.session_state.ticket_gerado = None
            st.rerun()

        if st.button("Finalizar Pedido e Gerar Ticket 🚀", type="primary"):
            if not nome_cliente.strip():
                st.error("⚠️ Por favor, digite seu nome!")
            elif not whats_cliente.strip() or len(whats_cliente) < 10:
                st.error("⚠️ Por favor, digite seu WhatsApp de contato com DDD!")
            elif not email_cliente.strip() or "@" not in email_cliente:
                st.error("⚠️ Por favor, digite um e-mail válido!")
            else:
                numero_ticket = random.randint(100, 999)
                hora_formatada = horario_busca.strftime("%H:%M")
                
