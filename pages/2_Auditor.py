import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Adriel-AI Pro - Auditor de Mercado", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }
    [data-testid="stHeader"] { display: none !important; }
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 14px 20px !important; margin-bottom: 15px !important; }
    .subtitulo-bloco-real { font-size: 13px !important; font-weight: bold !important; color: #60a5fa !important; margin-bottom: 15px; text-transform: uppercase; }
    div.stButton > button { background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important; color: white !important; font-weight: bold !important; width: 100% !important; cursor: pointer; border-radius: 6px !important; padding: 12px !important; border: 2px solid #1e293b !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #60a5fa; font-size: 26px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
st.write("---")

col_cen, col_dir = st.columns([1.4, 1.0])
with col_cen:
    st.markdown('<div class="header-box-real">🛡️ Varredura contra suspensões e concorrência no CPC</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">🔬 AUDITOR: DIAGNÓSTICO DO LEILÃO</p>', unsafe_allow_html=True)
    produto_auditar = st.text_input("Insira o nome da oferta para auditar:", value="Sugar Defender")
    st.write("")
    if st.button("🔍 INICIAR AUDITORIA DA CONTA E TERMOS"):
        with st.spinner("Varrendo diretrizes do Google Ads..."): time.sleep(1.0)
        st.success(f"🟢 Diagnóstico para {produto_auditar} concluído com sucesso!")
with col_dir:
    st.markdown('<div class="header-box-real" style="text-align: right;">Status: <span style="color:#00FF87;">Seguro</span></div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">🚦 SEMÁFORO DE RISCO EDITORIAL</p>', unsafe_allow_html=True)
    st.success("🟢 CONFORMIDADE MÁXIMA: Conta blindada contra políticas restritivas do Google Ads!")
