import streamlit as st

# Configuração executiva de tela cheia (A barra cinza nativa nasce fechada)
st.set_page_config(page_title="Adriel-AI Pro - Core", layout="wide", initial_sidebar_state="expanded")

# CSS Executivo Black para limpar o fundo e deixar o texto grande no teto
st.markdown("""
<style>
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 2rem !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Customização elegante dos links nativos da barra lateral cinza */
    [data-testid="stSidebarNav"] ul li a span { color: #ffffff !important; font-weight: bold !important; font-size: 15px !important; }
    [data-testid="stSidebarNav"] ul li a { background-color: #0f172a !important; border: 1px solid #1e293b !important; margin-bottom: 8px !important; padding: 12px !important; border-radius: 6px !important; }
</style>
""", unsafe_allow_html=True)

# Área Central da Home
st.markdown("<h1 style='color: #60a5fa; font-size: 32px; font-weight: 800;'>🤖 Adriel-AI PRO</h1>", unsafe_allow_html=True)
st.write("---")
st.markdown("### 🎛️ CENTRAL OPERACIONAL DE TRÁFEGO")
st.write("Olá, José Marques! Sua infraestrutura baseada em páginas limpas está ativa. Use o menu lateral esquerdo para alternar entre as ferramentas de verdade.")
