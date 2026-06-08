import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro - Control Center", layout="wide", initial_sidebar_state="collapsed")

# INJEÇÃO DE CSS DE ALTO PADRÃO (MATANÇA DA BARRA CINZA E CRIAÇÃO DO MENU NEON)
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Premium Cyber Onyx */
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1.2rem !important; padding-bottom: 0rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
    
    /* 🚨 DELETO TOTAL DA BARRA LATERAL CINZA NATIVA DO STREAMLIT */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }
    [data-testid="stHeader"] { display: none !important; }

    /* LINHAS DIVISÓRIAS DAS COLUNAS VIRTUAIS DO NOVO MENU */
    .coluna-container-lateral { background-color: transparent; border-right: 1px solid #1e293b; padding-right: 20px; min-height: 85vh; }
    .coluna-container-central { background-color: transparent; border-right: 1px solid #1e293b; padding-right: 20px; padding-left: 10px; min-height: 85vh; }
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 16px 20px !important; margin-bottom: 20px !important; }
    .kpi-card-real { background-color: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 18px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }

    /* 🚨 ANIMAÇÃO DE SINAL NEON: PULSO CIRÚRGICO (CIANO <-> VERDE) */
    @keyframes pulso-neon-executivo {
        0% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); }
        50% { border-color: #00FF87; box-shadow: 0 0 12px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); }
    }

    /* 💎 DESIGN EXECUTIVO DOS BOTÕES FLUTUANTES DA COLUNA 1 */
    .menu-lateral-container div.stButton > button {
        background: #0f172a !important; color: #cbd5e1 !important; font-weight: 700 !important; font-size: 13px !important; border: 1px solid #1e293b !important;
        text-align: left !important; padding: 14px 20px !important; width: 100% !important; margin-bottom: 8px !important; border-radius: 6px !important; cursor: pointer !important; transition: all 0.2s ease-in-out !important; text-transform: uppercase; letter-spacing: 0.5px;
    }
    
    /* 🔥 HOVER MAGNÉTICO: PISCA EM NEON E DESLIZA PARA A DIREITA */
    .menu-lateral-container div.stButton > button:hover {
        animation: pulso-neon-executivo 1.5s infinite ease-in-out !important; background: #1e293b !important; color: #00FF87 !important; transform: translateX(4px) !important;
    }
    
    .btn-acao-real div.stButton > button { background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important; color: white !important; font-weight: bold !important; border: none !important; text-align: center !important; padding: 12px !important; }
    .btn-acao-real div.stButton > button:hover { background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important; color: #050811 !important; }
</style>
""", unsafe_allow_html=True)

if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "Dashboard"

# 3 COLUNAS VERTICAIS PARALELAS EXEC
col_esquerda, col_centro, col_direita = st.columns([0.9, 1.35, 0.95])

# 🏢 COLUNA 1 (FIXA): MENU LATERAL PRO DE LUXO
with col_esquerda:
    st.markdown('<div class="coluna-container-lateral">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>ENTERPRISE CONTROL CENTER</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 🎛️ CONTEÚDO DINÂMICO
if st.session_state.modulo_ativo == "Dashboard":
    with col_centro:
        st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel-AI Pro!</div>', unsafe_allow_html=True)
        st.write("O passado infectado foi destruído. O novo ecossistema purificado e sem erros está ativo. Use os botões da barra executiva ao lado para navegar de forma rápida e segura.")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_direita:
        st.markdown('<div class="coluna-container-central" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color:#00FF87; font-weight:bold;">ONLINE</span></div>', unsafe_allow_html=True)
        col_m1, col_m2 = st.columns(2)
        with col_m1: st.markdown('<div class="kpi-card-real"><span style="font-size:10px;color:#64748b;font-weight:bold;">👥 ELITE AFILIADOS</span><br><span style="font-size:18px;color:#ffffff;font-weight:800;">265 Ativos</span></div>', unsafe_allow_html=True)
        with col_m2: st.markdown('<div class="kpi-card-real" style="border-color:#1e293b;"><span style="font-size:10px;color:#64748b;font-weight:bold;">💸 RECORRÊNCIA</span><br><span style="font-size:18px;color:#00FF87;font-weight:800;">R$ 48.750</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modulo_ativo == "Radar":
    with col_centro:
        st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)
        st.markdown("### 🛰️ MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
        st.write("Pronto para receber a tabela de extração real limpa.")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_direita:
        st.markdown('<div class="coluna-container-central" style="border-right: none;">', unsafe_allow_html=True)
        st.info("Scanner operando.")
        st.markdown('</div>', unsafe_allow_html=True)

# Rodapé unificado e institucional
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
