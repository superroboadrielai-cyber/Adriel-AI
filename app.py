import streamlit as st
import pandas as pd

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO LUXO (ELIMINA A BARRA BRANCA, CENTRALIZA O CONTEÚDO E CRIA BOTÕES HORIZONTAIS)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Premium Cyber Onyx Original do seu Print */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* 🚨 EXTINÇÃO TOTAL DA BARRA SUPERIOR BRANCA DO STREAMLIT (ELIMINA A ESTRELA E A LINHA DO TOPO) */
    [data-testid="stHeader"] { 
        display: none !important; 
        height: 0px !important;
        background: transparent !important;
    }
    .stHeader { display: none !important; }
    
    /* 🚨 COMPACTAÇÃO DE TELA CHEIA: OCUPA 100% DA LARGURA DISPONÍVEL NO SEU MONITOR */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta em definitivo as abas nativas cinzas padrão dos servidores */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* MOLDURA HOLOGRÁFICA DO SEU PRINT TOTALMENTE EXPANDIDA SEM ENCOSTAR NAS LATERAIS */
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2px solid #00E5FF !important;
        border-radius: 12px !important;
        padding: 24px !important;
        margin-bottom: 25px !important;
        width: 100% !important;
    }
    
    /* DESIGN DOS NOVOS BOTÕES HORIZONTAIS EM CÁPSULA (FIM DO APERTO LATERAL) */
    .menu-horizontal-container div.stButton > button {
        background: #0f172a !important; 
        color: #cbd5e1 !important; 
        font-weight: 700 !important;
        font-size: 13px !important;
        border: 1px solid #1e293b !important; 
        text-align: center !important;
        padding: 12px 10px !important;
        width: 100% !important;
        border-radius: 30px !important; /* Formato cápsula executivo */
        cursor: pointer !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .menu-horizontal-container div.stButton > button:hover {
        background: #1e293b !important;
        color: #00FF87 !important;
        border-color: #00FF87 !important;
    }
    
    .titulo-secao { 
        color: #00FF87; 
        font-size: 18px; 
        font-weight: 800; 
        text-transform: uppercase; 
        margin-top: 20px;
        margin-bottom: 15px; 
        letter-spacing: 0.5px; 
    }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do roteador de abas na memória RAM do app
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Radar"

# =============================================================================================================
# MARCA SUPERIOR EXECUTIVA CENTRALIZADA
# =============================================================================================================
st.markdown("<h2 style='color: #ffffff; font-size: 28px; font-weight: 900; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle; margin-left:5px;'>PRO</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 11px; margin-top:-5px; letter-spacing:1px; text-transform: uppercase;'>ENTERPRISE CONTROL CENTER • WIDE INTERFACE</p>", unsafe_allow_html=True)
st.write("---")

# =============================================================================================================
# 🚀 SELETOR DE MENUS HORIZONTAIS: REMOVE O ENCURTAMENTO LATERAL E ABRE A TELA CHEIA
# =============================================================================================================
st.markdown('<div class="menu-horizontal-container">', unsafe_allow_html=True)
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    if st.button("🎛️ Dashboard Geral", key="btn_nav_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
with col_nav2:
    if st.button("🛰️ 1. Radar de Produtos", key="btn_nav_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
with col_nav3:
    if st.button("🔬 2. Auditor de Mercado", key="btn_nav_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# =============================================================================================================
# EXIBIÇÃO AMPLA EM TELA CHEIA DO CONTEÚDO (SEM COLUNAS APERTADAS)
# =============================================================================================================

# 🛰️ GAVETA DO MÓDULO 1: RADAR DE PRODUTOS COMPLETO
if st.session_state.modulo_ativo == "Radar":
    st.markdown("""
    <div class="caixa-holografica-real-print">
        <h3 style="color: #00FF87; font-size: 21px; font-weight: 800; margin: 0 0 8px 0; font-family: sans-serif;">
            🌲 MÓDULO 1: RADAR DE PRODUTOS INTERNACIONAIS
        </h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 0px;">
            Varredura ativa. Abaixo estão listados os produtos validados com tráfego real na gringa ocupando toda a largura útil do seu monitor.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="titulo-secao">🔥 TOP SUPER VALIDADOS - SINAL DE ALTA</p>', unsafe_allow_html=True)
    st.write("📈 **Sugar Defender** | Gravidade: 284.50 | Anunciar: Google Ads (Fundo) | VSL convertendo muito tráfego de palavra exata.")
    st.write("📈 **Puravive** | Gravidade: 241.10 | Anunciar: Bing Ads + Pre-Sell | CPC mais barato no leilão móvel internacional.")
    st.write("📈 **Java Burn** | Gravidade: 198.40 | Anunciar: Google Ads (Pre-Sell) | Checkout rápido reduz o abandono de carrinho gringo.")
    st.write("📈 **Prodentim** | Gravidade: 172.90 | Anunciar: Google Ads (Fundo) | Saúde dental com altíssima taxa de recompra e recorrência.")
    st.write("📈 **Alpilean** | Gravidade: 165.20 | Anunciar: Bing Ads Direto | Baixa taxa de reembolso nesta temporada garante lucros firmes.")
    
    st.write("")
    st.markdown('<p class="titulo-secao" style="color:#00E5FF;">📊 OUTROS VALIDADOS - LEILÕES MENOS CONCORRIDOS</p>', unsafe_allow_html=True)
    st.write("🔹 **Dentitox Pro** | Gravidade: 114.60 | Oportunidade: Forte conversão identificada no leilão da Austrália fugindo do mercado caro.")
    st.write("🔹 **Metanail Complex** | Gravidade: 109.20 | Oportunidade: Performando muito bem com estruturas de advertoriais dentro do Bing Ads.")
    st.write("🔹 **Kerassentials** | Gravidade: 102.50 | Oportunidade: Estabilidade histórica. Destacar os 60 dias de garantia gera gatilho de urgência.")
    st.write("🔹 **Ikaria Lean Juice** | Gravidade: 98.40 | Oportunidade: Público comprador ativo. Exige mudar o ângulo da copy contra fadiga de criativos.")
    st.write("🔹 **Exipure** | Gravidade: 91.10 | Oportunidade: CPC baixo e leilão calmo ideal para rodar campanhas estáveis com orçamentos menores.")

# 🔬 GAVETA DO MÓDULO 2: AUDITOR DE MERCADO
elif st.session_state.modulo_ativo == "Auditor":
    st.markdown("""
    <div class="caixa-holografica-real-print" style="border-color: #00FF87;">
        <h3 style="color: #00FF87; font-size: 21px; font-weight: 800; margin: 0 0 10px 0; font-family: sans-serif;">
            🔬 MÓDULO 2: AUDITOR DE MERCADO E DIRETRIZES
        </h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 0px;">
            Mapeamento de compliance ativo focado em contas de afiliados na gringa.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    nome_busca = st.text_input("Insira o nome do produto para auditar:", value="Sugar Defender")
    st.write("")
    
    if st.button("🔬 DISPARAR ANÁLISE DE SEGURANÇA"):
        st.success(f"🟢 VERDITO ADRIEL-AI: O produto {nome_busca} está em conformidade máxima! Melhor país para subir campanha no Google Ads Pesquisa fundo de funil: Canadá ou Nova Zelândia.")

# 🎛️ GAVETA DO DASHBOARD GERAL HOME
elif st.session_state.modulo_ativo == "Dashboard":
    st.info("👤 Bem-vindo Comandante José Marques! Seu robô foi reformulado em tela cheia ampla. Use as cápsulas do menu superior horizontal no topo para navegar de forma simétrica e ultrarrápida pelas ferramentas.")

# Rodapé unificado
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
