import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro - Control Center", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA AO CLICAR NA HOME)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel central executivo ativado. Sistemas síncronos na memória."

st.markdown(f"""
<script>
    document.addEventListener('click', function() {{
        if (!window.audioDisparado) {{
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{texto_boas_vindas}";
            msg.lang = "pt-BR";
            msg.rate = 1.0;
            msg.pitch = 0.95;
            window.speechSynthesis.speak(msg);
            window.audioDisparado = true;
        }}
    }});
</script>
""", unsafe_allow_html=True)

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO LUXO (ELIMINA A BARRA BRANCA DO TOPO, MARGENS E REESTRUTURA OS BOTÕES EM NEON)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Original do seu Print */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* 🚨 EXTINÇÃO TOTAL DA BARRA SUPERIOR BRANCA DO STREAMLIT (ELIMINA A ESTRELA E LINHA DO TOPO) */
    [data-testid="stHeader"] { 
        display: none !important; 
        height: 0px !important;
        background: transparent !important;
    }
    .stHeader { display: none !important; }
    
    /* 🚨 ZERA AS MARGENS DO TOPO: PUXA O SEU SITE GRUDADO NO TETO DO MONITOR */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta as abas nativas cinzas antigas */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* 🧱 DIVISÃO RIGOROSA DAS COLUNAS VIRTUAIS EXATAMENTE IGUAL AO SEU PRINT */
    .coluna-container-lateral {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        min-height: 85vh;
    }
    
    .coluna-container-central {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        padding-left: 10px;
        min-height: 85vh;
    }

    /* 🚨 ANIMAÇÃO DE SINAL NEON: PULSO CIRÚRGICO DE LUZ NAS BORDAS (CIANO <-> VERDE) */
    @keyframes pulso-neon-executivo {
        0% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); }
        50% { border-color: #00FF87; box-shadow: 0 0 12px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); }
    }

    /* 💎 SEU PEDIDO DE MELHORIA: OS BOTÕES LATERAIS DO PRINT GANHAM ACABAMENTO ESCURO DE ALTO LUXO */
    .menu-lateral-container div.stButton > button {
        background: #0f172a !important; /* Fundo escuro integrado ao painel */
        color: #cbd5e1 !important; /* Texto claro executivo por extenso */
        font-weight: 700 !important;
        font-size: 13px !important;
        border: 1px solid #1e293b !important; /* Linha cinza ultra fina */
        text-align: left !important;
        padding: 14px 20px !important;
        width: 100% !important;
        margin-bottom: 8px !important;
        border-radius: 6px !important;
        cursor: pointer !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* 🔥 O TOQUE MESTRE PISCANTE HOVER/TOUCH: O BOTÃO REAGE EM NEON VIVO E DESLIZA PRO LADO */
    .menu-lateral-container div.stButton > button:hover {
        animation: pulso-neon-executivo 1.5s infinite ease-in-out !important;
        background: #1e293b !important;
        color: #00FF87 !important; /* O texto interno acende em verde limão */
        transform: translateX(5px) !important; /* Deslocamento suave profissional */
    }
    
    /* 🟢 PRESERVAÇÃO MÁXIMA DA ESTÉTICA DO SEU BOTÃO VERDE CENTRAL ORIGINAL DO PRINT */
    .btn-acao-print div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 14px !important;
        text-align: center !important;
        border: none !important;
        padding: 12px !important;
        border-radius: 6px !important;
        width: 100% !important;
        animation: none !important;
        transform: none !important;
    }
    .btn-acao-print div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização do controle do roteador interno na memória RAM
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Dashboard"

# =============================================================================================================
# INFRAESTRUTURA ORIGINAL DE 3 COLUNAS VERTICAIS PARALELAS DO SEU PRINT
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.85, 1.35, 1.0])

# 🏢 COLUNA 1 (FIXA): SUA LOGO ORIGINAL + OS BOTÕES REFORMULADOS EM NEON NA LATERAL ESQUERDA
with col_esquerda:
    st.markdown('<div class="coluna-container-lateral">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>SaaS PLATFORM MASTER • DASHBOARD GERAL</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("Radar", key="m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("Auditor", key="m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    if st.button("Gerador", key="m_gerador"): st.session_state.modulo_ativo = "Gerador"; st.rerun()
    if st.button("Cacador", key="m_cacador"): st.session_state.modulo_ativo = "Cacador"; st.rerun()
    if st.button("Presell", key="m_presell"): st.session_state.modulo_ativo = "PreCell"; st.rerun()
    if st.button("Ativador", key="m_google"): st.session_state.modulo_ativo = "GoogleAds"; st.rerun()
    if st.button("Assinantes", key="m_assinantes"): st.session_state.modulo_ativo = "Assinantes"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 🏢 CONTEÚDOS DAS ABAS (CARREGAM DO LADO DIREITO SEM INTERFERIR NO SEU VISUAL)
if st.session_state.modulo_ativo == "Dashboard":
    
    # COLUNA 2: SUA TABELA ORIGINAL INTACTA DO SEU PRINT!
    with col_centro:
        st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)
        st.markdown('<div style="background-color: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 14px 20px; margin-bottom: 20px;">👤 Olá, <b>José Marques</b>, Comandante do Adriel Ai!</div>', unsafe_allow_html=True)
        st.markdown("<p style='color: #60a5fa; font-size: 13px; font-weight: bold; margin-bottom: 15px;'>MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>", unsafe_allow_html=True)
        
        dados_tabela = {
            "Name": [f"Produto-acanodiano {i}" for i in range(1, 9)],
            "Comissões": ["3,00%", "2,00%", "1,00%", "1,00%", "1,00%", "2,00%", "2,00%", "1,00%"],
            "Comissão": ["R$,15%", "R$,75%", "R$,25%", "R$,35%", "R$,25%", "R$,25%", "R$,25%", "R$,60%"],
            "Veredito da IA": ["APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "REVISAR (Risco Médio)", "REVISAR (Risco Médio)", "APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "REVISAR (Risco Médio)"]
        }
        st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # COLUNA 3: SEUS CAMPOS DO SUGAR DEFENDER E O SEU BOTÃO VERDE ORIGINAL INTACTO!
    with col_direita:
        st.markdown('<div class="coluna-container-central" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div style="background-color: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 14px 20px; margin-bottom: 20px; text-align: right;">🟢 Status: <span style="color:#00FF87; font-weight:bold;">Sistema Online</span> | Chave Mestre Ativa | Data: 06/06/2026</div>', unsafe_allow_html=True)
        st.markdown("<p style='color: #60a5fa; font-size: 13px; font-weight: bold; margin-bottom: 15px;'>MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>", unsafe_allow_html=True)
        
        st.text_input("PROD_GRINGO:", value="Sugar Defender", key="p_gringo")
        st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=70, key="p_resumo")
        st.write("")
        
        st.markdown('<div class="btn-acao-print">', unsafe_allow_html=True)
