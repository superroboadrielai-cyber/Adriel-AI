import streamlit as st

# 🚨 REGRA MESTRE: set_page_config precisa ser a PRIMEIRA instrução do código das páginas!
st.set_page_config(page_title="Adriel-AI Pro - Área Comercial", layout="wide", initial_sidebar_state="collapsed")

# Injeção de CSS Premium Black da família Adriel AI PRO (Mantém o padrão de luxo tridimensional)
st.markdown("""
<style>
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 14px 20px !important; margin-bottom: 15px !important; }
    .subtitulo-bloco-real { font-size: 13px !important; font-weight: bold !important; color: #60a5fa !important; margin-bottom: 15px; text-transform: uppercase; }
    .kpi-box { background: #0f172a; padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important; font-weight: bold !important; font-size: 14px !important;
        border: 2px solid #1e293b !important; padding: 12px 15px !important; border-radius: 6px !important; width: 100% !important; cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #60a5fa; font-size: 26px; font-weight: 800; margin-bottom:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
st.write("---")

col_centro, col_direita = st.columns([1.4, 1.0])

with col_centro:
    st.markdown('<div class="header-box-real">💎 Checkout e Controle Administrativo de Licenças SaaS</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">🔑 AUTENTICAÇÃO DO PROPRIETÁRIO</p>', unsafe_allow_html=True)
    
    # Campo secreto real com máscara de senha
    senha = st.text_input("Insira a Chave Secreta do Comandante José para liberar os logs:", type="password")
    st.write("")
    
    if st.button("🔓 ACESSAR PAINEL FINANCEIRO DE LICENÇAS", key="btn_run_assinantes_real"):
        if senha == "jose123": # Você pode mudar essa senha quando quiser!
            st.success("🔓 HANDSHAKE CONCLUÍDO! Acesso concedido aos cofres do SaaS.")
            st.markdown("### 📊 Faturamento e Planos Ativos:")
            st.write("• **Plano Start (R$ 97/mês):** 142 Usuários Ativos")
            st.write("• **Plano Elite (R$ 147/mês):** 89 Usuários Ativos")
            st.write("• **Plano Black PRO (R$ 297/mês):** 34 Usuários Ativos")
        elif senha == "":
            st.warning("⚠️ Aguardando digitação da Chave Secreta Master.")
        else:
            st.error("❌ CHAVE INCORRETA! Acesso negado aos dados comerciais do José.")

with col_direita:
    st.markdown('<div class="header-box-real" style="text-align: right;">Gateway de Pagamentos: <span style="color:#00E5FF;">Ativo</span></div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">👥 MÉTRICAS DA COMUNIDADE ELITE</p>', unsafe_allow_html=True)
    
    col_mini1, col_mini2 = st.columns(2)
    with col_mini1: st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;">👥 USUÁRIOS</span><br><span style="font-size:20px;color:#ffffff;font-weight:800;">265 Ativos</span></div>', unsafe_allow_html=True)
    with col_mini2: st.markdown('<div class="kpi-box" style="border-color:#00FF87;"><span style="font-size:11px;color:#64748b;font-weight:bold;">💸 FATURAMENTO</span><br><span style="font-size:20px;color:#00FF87;font-weight:800;">R$ 48.750</span></div>', unsafe_allow_html=True)

# Rodapé unificado
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 45px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
