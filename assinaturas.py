
# Clube de Assinatura Los Hombres - Versão Estética com Logo, Wide Layout e Cores Personalizadas

import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# === Configurações Gerais ===
st.set_page_config(page_title="Clube de Assinatura Los Hombres", layout="wide")

LOGO_PATH = "logo.png"

col1, col2, col3 = st.columns([1.5,1,1])

with col2:
    with st.container():
        st.markdown(
            """
            <style>
            .logo-container {
                margin-top: 30px;
                margin-bottom: 5px;
            }
            </style>
            <div class="logo-container">
            """,
            unsafe_allow_html=True
        )
        st.image(LOGO_PATH, width=250)
        st.markdown("</div>", unsafe_allow_html=True)



st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
    }
    .block-container {
        padding-top: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stButton > button {
        color: #FFFFFF;
        border: 1px solid #AD9955;
        background-color: #000000;
        padding: 0.5em 1em;
        font-size: 1em;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background-color: #AD9955;
        color: #000000;
    }
    .stDownloadButton > button {
        color: #FFFFFF;
        border: 1px solid #AD9955;
        background-color: #000000;
        padding: 0.5em 1em;
        font-size: 1em;
        border-radius: 8px;
    }
    .stDownloadButton > button:hover {
        background-color: #AD9955;
        color: #000000;
    }
    .stExpanderHeader {
        color: #AD9955 !important;
    }
    .card {
    padding: 10px;
    margin-bottom: 10px;
    border: none;
    background-color: transparent;
    box-shadow: none;
}
    </style>
    """,
    unsafe_allow_html=True
)

POLITICA_PDF_PATH = "docs/Politica_de_Uso_Assinaturas.pdf"
REMETENTE_EMAIL = "loshombresbarbearia@gmail.com"
DESTINATARIO_EMAIL = "loshombresbarbearia@gmail.com"
SENHA_APP = "xlxo jisd lokl wyhy"


# === Título personalizado ===
st.markdown(
    "<h1 style='text-align: center; color: #AD9955;'>Clube de Assinatura Los Hombres</h1>",
    unsafe_allow_html=True
)

st.write("Escolha o seu plano de assinatura, preencha seus dados e aceite a política de uso para prosseguir com o pagamento.")

# === Dados dos Planos ===
planos = {
    "Assinatura Corte Seg a Qua (R$130,00)": {
        "descricao": "Corte ilimitado no mês, agendamento de segunda a quarta.",
        "link_pagamento": "https://cielolink.com.br/3VjGKA4"
    },
    "Assinatura Barba Seg a Qua (R$130,00)": {
        "descricao": "Barba ilimitada no mês, agendamento de segunda a quarta.",
        "link_pagamento": "https://cielolink.com.br/419bhnY"
    },
    "Assinatura Completo Seg a Qua (R$250,00)": {
        "descricao": "Corte e barba ilimitados no mês, agendamento de segunda a quarta.",
        "link_pagamento": "https://cielolink.com.br/3ZgdeMD"
    },
    "Assinatura Corte Todos os Dias (R$165,00)": {
        "descricao": "Corte ilimitado no mês, agendamento todos os dias.",
        "link_pagamento": "https://cielolink.com.br/45MKNL9"
    },
    "Assinatura Barba Todos os Dias (R$165,00)": {
        "descricao": "Barba ilimitada no mês, agendamento todos os dias.",
        "link_pagamento": "https://cielolink.com.br/45jfUho"
    },
    "Assinatura Completo Todos os Dias (R$295,00)": {
        "descricao": "Corte e barba ilimitados no mês, agendamento todos os dias.",
        "link_pagamento": "https://cielolink.com.br/4kAtu4B"
    }
}

# === Função de envio de e-mail com anexo ===
def enviar_email(nome, cpf, plano):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    corpo_email = f"""Novo aceite de Política de Uso - Clube de Assinatura Los Hombres

Nome do cliente: {nome}
CPF do cliente: {cpf}
Plano escolhido: {plano}
Data e hora do aceite: {data_hora}
"""

    msg = MIMEMultipart()
    msg['Subject'] = "Novo aceite - Clube de Assinatura Los Hombres"
    msg['From'] = REMETENTE_EMAIL
    msg['To'] = DESTINATARIO_EMAIL
    msg.attach(MIMEText(corpo_email))

    try:
        with open(POLITICA_PDF_PATH, "rb") as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="Politica_de_Uso_Assinaturas.pdf"')
            msg.attach(part)
    except Exception as e:
        print(f"Erro ao anexar o PDF: {e}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(REMETENTE_EMAIL, SENHA_APP)
            server.sendmail(REMETENTE_EMAIL, DESTINATARIO_EMAIL, msg.as_string())
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False

# === Interface: cards de planos ===
# Garantir que plano_escolhido existe no session_state
if 'plano_escolhido' not in st.session_state:
    st.session_state['plano_escolhido'] = None

plano_escolhido = st.session_state['plano_escolhido']


# Separar os planos
planos_seg_a_qua = {k: v for k, v in planos.items() if "Seg a Qua" in k}
planos_todos_dias = {k: v for k, v in planos.items() if "Todos os Dias" in k}

# Criar as duas colunas
col1, col2 = st.columns(2)

# Coluna da esquerda - Segunda a Quarta
with col1:
    st.markdown("<h2 style='color:#AD9955;'>Planos Segunda a Quarta</h2>", unsafe_allow_html=True)

    for plano, info in planos_seg_a_qua.items():
        with st.container():
            st.markdown(f"<div class='card'>", unsafe_allow_html=True)
            
            st.markdown(f"<h3 style='color:#AD9955; border-bottom:1px solid #AD9955; padding-bottom:5px; margin-bottom:10px;'>{plano}</h3>", unsafe_allow_html=True)
            
            st.write(info['descricao'])
            
            if st.button(f"Selecionar {plano}"):
                st.session_state['plano_escolhido'] = plano
            
            st.markdown("</div>", unsafe_allow_html=True)

# Coluna da direita - Todos os Dias
with col2:
    st.markdown("<h2 style='color:#AD9955;'>Planos Todos os Dias</h2>", unsafe_allow_html=True)

    for plano, info in planos_todos_dias.items():
        with st.container():
            st.markdown(f"<div class='card'>", unsafe_allow_html=True)
            
            st.markdown(f"<h3 style='color:#AD9955; border-bottom:1px solid #AD9955; padding-bottom:5px; margin-bottom:10px;'>{plano}</h3>", unsafe_allow_html=True)
            
            st.write(info['descricao'])
            
            if st.button(f"Selecionar {plano}"):
                st.session_state['plano_escolhido'] = plano
            
            st.markdown("</div>", unsafe_allow_html=True)



# === Fluxo pós seleção ===
if 'plano_escolhido' in st.session_state:
    plano_escolhido = st.session_state['plano_escolhido']

if plano_escolhido:
    st.success(f"Plano selecionado: {plano_escolhido}")
    st.write(f"**Descrição:** {planos[plano_escolhido]['descricao']}")

    nome = st.text_input("Nome completo *")
    cpf = st.text_input("CPF *")

    with st.expander("📜 Política de Uso - Clique para ler"):
        st.write("""
        POLÍTICA DE USO — CLUBE DE ASSINATURA LOS HOMBRES
Bem-vindo ao Clube Exclusivo Los Hombres! Ao aderir a um de nossos planos de assinatura, você declara estar ciente e de acordo com os termos e condições abaixo:
1. PLANOS E VALIDADE<br><br>
•O Clube de Assinatura oferece planos mensais, renovados automaticamente a cada período de 30 dias.<br>
•Os serviços inclusos em cada plano estão descritos na oferta comercial no momento da adesão.<br>
2. REGRAS DE USO<br><br>
•A assinatura é pessoal e intransferível. Apenas o titular cadastrado poderá utilizar os serviços inclusos no plano.<br>
•O não uso dos serviços durante o período contratado não gera crédito para períodos futuros nem dá direito a reembolso.<br>
•As visitas deverão ser agendadas previamente, conforme disponibilidade da agenda da barbearia.<br>
3. REEMBOLSO<br><br>
•Após o pagamento da assinatura, não haverá reembolso parcial ou total em caso de desistência ou não utilização dos serviços.<br>
•Em casos excepcionais (ex.: fechamento da unidade ou impossibilidade total de prestação de serviços), um reembolso proporcional poderá ser considerado.<br>
4. CANCELAMENTO<br><br>
•O cliente poderá solicitar o cancelamento a qualquer momento, sem multa, através do canal oficial de atendimento (WhatsApp ou e-mail informado).<br>
•O cancelamento será efetivado ao término do período vigente. Não haverá reembolso proporcional por dias não utilizados no mês corrente.<br>
5. CONDIÇÕES GERAIS<br><br>
•A barbearia se reserva o direito de revisar os valores e condições dos planos, mediante aviso prévio de 30 dias aos assinantes.<br>
•O não pagamento da renovação automática implicará no bloqueio do uso do plano até a regularização.<br>
6. ACEITE<br><br>
•Ao realizar a adesão ao Clube de Assinatura, o cliente declara ter lido, compreendido e aceito todos os termos aqui dispostos.""")
        with open(POLITICA_PDF_PATH, "rb") as file:
            st.download_button(label="📄 Baixar PDF da Política de Uso",
                               data=file,
                               file_name="Politica_de_Uso_Assinaturas.pdf",
                               mime="application/pdf")

    aceite = st.checkbox("Li e concordo com a Política de Uso *")

    if st.button("Prosseguir para pagamento"):
        if not nome or not cpf:
            st.error("Por favor, preencha todos os campos obrigatórios (Nome e CPF).")
        elif not aceite:
            st.error("Você deve aceitar a Política de Uso para prosseguir.")
        else:
            enviado = enviar_email(nome, cpf, plano_escolhido)
            if enviado:
                st.success("Registro de aceite enviado com sucesso! Você será redirecionado para o pagamento.")
                st.markdown(f"[Clique aqui para pagar]({planos[plano_escolhido]['link_pagamento']})")
            else:
                st.error("Erro ao enviar o registro de aceite. Por favor, tente novamente ou entre em contato com a barbearia.")

#=========== RODAPÉ==========

st.markdown(
    """
    <div style='margin-top: 70px; padding-top: 20px; text-align: center; color: #888888; font-size: 12px; line-height: 1.4;'>
    <p style='font-weight: bold; margin-bottom: 5px;'>Los Hombres Barbearia</p>
    Rua 13 Norte, Lote 04 - Ed. Ilha de Manhattan - Águas Claras, Brasília - DF, 71909-720<br>
    Telefone: (61) 3546-3241 | WhatsApp: (61) 99651-1331<br><br>
    <em>Os preços e condições apresentados neste site podem sofrer alterações sem aviso prévio.</em>
    </p>
    """,
    unsafe_allow_html=True
)
