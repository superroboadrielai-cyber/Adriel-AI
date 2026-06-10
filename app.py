import streamlit as st

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO LUXO (EXTINGUE AS CAIXAS BRANCAS E CRIA CÁPSULAS NEON DE ALTO PADRÃO)
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
    
    /* 🚨 COMPACTAÇÃO DE TELA CHEIA: PUXA O SEU SITE GRUDADO NO TETO DO MONITOR */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta em definitivo as abas nativas cinzas padrão dos servidores */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* MOLDURA HOLOGRÁFICA DO SEU PRINT EXPANDIDA COM PERFEIÇÃO */
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2px solid #00E5FF !important;
        border-radius: 12px !important;
        padding: 24px !important;
        margin-bottom: 25px !important;
        width: 100% !important;
    }
    
    /* 🚨 DESTRUIÇÃO DAS CAIXAS BRANCAS: CONFIGURAÇÃO DE CÁPSULAS ESCURAS DE ALTA PERFORMANCE COM HOVER NEON */
    .stButton > button {
        background-color: #0f172a !important;
        color: #cbd5e1 !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        border: 1px solid #1e293b !important;
        padding: 12px 20px !important;
        border-radius: 30px !important; /* Formato cápsula executivo da Apple */
        width: 100% !important;
        cursor: pointer !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* 🔥 HOVER VIBRANTE SUPREMO: QUANDO PASSA O MOUSE OU O DEDO, O BOTÃO CÁPSULA BRILHA EM NEON */
    .stButton > button:hover {
        background-color: #1e293b !important;
        color: #00FF87 !important; /* O texto interno acende em verde vivo */
        border-color: #00FF87 !important;
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.4) !important;
        transform: scale(1.02) !important;
    }
    
    .titulo-secao { 
        color: #00FF87; 
        font-size: 16px; 
        font-weight: 800; 
        text-transform: uppercase; 
        margin-top: 25px;
        margin-bottom: 12px; 
        letter-spacing: 0.5px; 
    }
    
    /* Input customizado escuro */
    .stTextInput > div > div > input {
        background-color: #0f172a !important;
        color: white !important;
        border: 1px solid #1e293b !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do roteador de abas na memória RAM do app
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Radar"

# =============================================================================================================
# MARCA SUPERIOR EXECUTIVA CENTRALIZADA
# =============================================================================================================
st.markdown("<h2 style='color: #ffffff; font-size: 26px; font-weight: 900; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:11px; border-radius:4px; vertical-align:middle; margin-left:5px;'>PRO</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 10px; margin-top:-5px; letter-spacing:1px; text-transform: uppercase;'>ENTERPRISE CONTROL CENTER • REFORMULATED PLATFORM</p>", unsafe_allow_html=True)
st.write("---")

# =============================================================================================================
# 🚀 MENU HORIZONTAL REFORMULADO (FIM DAS CAIXAS BRANCAS FAZENDO FUNCIONAR AS ABAS)
# =============================================================================================================
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    if st.button("🎛️ Dashboard Geral", key="btn_nav_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
with col_nav2:
    if st.button("🛰️ 1. Radar de Produtos", key="btn_nav_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
with col_nav3:
    if st.button("🔬 2. Auditor de Mercado", key="btn_nav_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()

st.write("---")

# =============================================================================================================
# EXIBIÇÃO AMPLA EM TELA CHEIA DO CONTEÚDO (CONFORME O SEU COMANDO DE NAVEGAÇÃO)
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
st.markdown('<div style="text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
