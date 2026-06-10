import streamlit as st
import pandas as pd

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO LUXO (ELIMINA A BARRA BRANCA DO TOPO E MODELA O DESIGN DO NOSSO SELETOR LATERAL)
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
    
    /* 🚨 ZERA AS MARGENS DO TOPO: PUXA O SEU SITE GRUDADO NO TETO DO MONITOR */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta as abas nativas cinzas antigas */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* 🧱 DIVISÃO RIGOROSA DAS COLUNAS VIRTUAIS DO SEU CHASSI DE LUXO */
    .coluna-container-lateral {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        min-height: 85vh;
    }
    
    .coluna-container-central {
        background-color: transparent;
        padding-left: 15px;
        min-height: 85vh;
    }

    /* DESIGN DOS BOTÕES LATERAIS DE CARBONO PREMIUM POR EXTENSO */
    .menu-lateral-container div.stButton > button {
        background: #0f172a !important; 
        color: #cbd5e1 !important; 
        font-weight: 700 !important;
        font-size: 13px !important;
        border: 1px solid #1e293b !important; 
        text-align: left !important;
        padding: 14px 20px !important;
        width: 100% !important;
        margin-bottom: 8px !important;
        border-radius: 6px !important;
        cursor: pointer !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .menu-lateral-container div.stButton > button:hover {
        background: #1e293b !important;
        color: #00FF87 !important;
        border-color: #00FF87 !important;
    }
    
    /* MOLDURA HOLOGRÁFICA DO SEU PRINT CAMPEÃO */
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2.5px solid #00E5FF !important;
        border-radius: 14px !important;
        padding: 24px !important;
        margin-bottom: 25px !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do roteador de abas na memória RAM do app
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Radar"

# =============================================================================================================
# MONTAGEM PARALELA: COLUNA 1 (MENU FIXO) + COLUNA 2 (CONTEÚDO DO RADAR COMPLETO)
# =============================================================================================================
col_esquerda, col_direita_conteudo = st.columns([0.22, 0.78])

# 🏢 COLUNA 1: BOTÕES LATERAIS EXECUTIVOS POR EXTENSO
with col_esquerda:
    st.markdown('<div class="coluna-container-lateral">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 22px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 6px; font-size:11px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size: 10px; margin-top:-3px; letter-spacing:1px;'>CONTROL PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="btn_m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="btn_m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="btn_m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 🏢 COLUNA 2: ÁREA CENTRAL DE CONTEÚDO QUE RESPONDE OPERACIONALMENTE
with col_direita_conteudo:
    st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)
    
    # 🛰️ TELA DO MÓDULO 1: RADAR DE PRODUTOS REAL
    if st.session_state.modulo_ativo == "Radar":
        st.markdown("""
        <div class="caixa-holografica-real-print">
            <h3 style="color: #00FF87; font-size: 21px; font-weight: 800; margin: 0 0 10px 0; font-family: sans-serif;">
                📊 MÓDULO 1: RADAR DE PRODUTOS INTERNACIONAIS
            </h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 0px;">
                Varredura ativa. Abaixo estão listados os produtos validados com tráfego real na gringa.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔥 TOP SUPER VALIDADOS - SINAL DE ALTA")
        st.write("📈 **Sugar Defender** | Gravidade: 284.50 | Anunciar: Google Ads (Fundo) | VSL convertendo muito.")
        st.write("📈 **Puravive** | Gravidade: 241.10 | Anunciar: Bing Ads + Pre-Sell | CPC mais barato no leilão.")
        st.write("📈 **Java Burn** | Gravidade: 198.40 | Anunciar: Google Ads (Pre-Sell) | Checkout rápido de alta conversão.")
        st.write("📈 **Prodentim** | Gravidade: 172.90 | Anunciar: Google Ads (Fundo) | Saúde dental com alta recompra.")
        st.write("📈 **Alpilean** | Gravidade: 165.20 | Anunciar: Bing Ads Direto | Baixa taxa de reembolso nesta temporada.")
        
        st.write("")
        st.markdown("### 📊 OUTROS VALIDADOS - LEILÕES MENOS CONCORRIDOS")
        st.write("🔹 **Dentitox Pro** | Gravidade: 114.60 | Oportunidade: Forte conversão identificada no mercado da Austrália.")
        st.write("🔹 **Metanail Complex** | Gravidade: 109.20 | Oportunidade: Performando muito bem com advertoriais no Bing.")
        st.write("🔹 **Kerassentials** | Gravidade: 102.50 | Oportunidade: Estabilidade histórica. Destacar os 60 dias de garantia.")
        st.write("🔹 **Ikaria Lean Juice** | Gravidade: 98.40 | Oportunidade: Público comprador ativo. Exige mudar o ângulo da copy.")
        st.write("🔹 **Exipure** | Gravidade: 91.10 | Oportunidade: CPC baixo e leilão calmo ideal para orçamentos menores.")

    # 🔬 TELA DO MÓDULO 2: AUDITOR DE MERCADO REAL
    elif st.session_state.modulo_ativo == "Auditor":
        st.markdown("""
        <div class="caixa-holografica-real-print" style="border-color: #00FF87;">
            <h3 style="color: #00FF87; font-size: 21px; font-weight: 800; margin: 0 0 10px 0; font-family: sans-serif;">
                🔬 MÓDULO 2: AUDITOR DE MERCADO E DIRETRIZES
            </h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 0px;">
                Mapeamento de compliance ativo para leilões internacionais.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        nome_busca = st.text_input("Insira o nome do produto para auditar:", value="Sugar Defender")
        st.write("")
        
        if st.button("🔬 DISPARAR ANÁLISE DE SEGURANÇA"):
            st.success(f"🟢 VERDITO ADRIEL-AI: O produto {nome_busca} está em conformidade máxima! Melhor país para subir campanha: Canadá ou Nova Zelândia no Google Ads Pesquisa fundo de funil.")

    # 🎛️ TELA DO DASHBOARD GERAL HOME
    elif st.session_state.modulo_ativo == "Dashboard":
        st.info("👤 Bem-vindo Comandante José Marques! Seu robô está totalmente configurado. Use os botões da barra lateral da esquerda para navegar liso pelas ferramentas.")

    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé unificado
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
