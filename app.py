import streamlit as st
import pandas as pd
import time

# Configuração premium de layout amplo (Ocupa 100% da largura da tela)
st.set_page_config(page_title="Adriel-AI Pro - Control Center", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA EXATAMENTE O TEXTO DO SEU PRINT)
# =============================================================================================================
texto_boas_vindas = "Seja muito bem-vindo, Comandante José Marques da Silva! O cenário operacional está fixado em 3D. Observe que as bordas flutuantes alternam de cor continuamente entre Ciano e Verde Neon, reproduzindo o mesmo estilo requintado da interface do robô inteligente. Clique em qualquer lugar da tela para ativar os alto-falantes."

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
# INJEÇÃO DE CSS DE ALTO LUXO (OCULTA A BARRA BRANCA DO TOPO E MODELA O DESIGN EXATO DO PRINT)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Premium Cyber Onyx Fiel ao seu Print */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* 🚨 SUMIDOURO DA BARRA BRANCA SUPERIOR DO STREAMLIT (ELIMINA ESTRELA, LÁPIS E LOGO DO GITHUB) */
    [data-testid="stHeader"] { 
        display: none !important; 
        height: 0px !important;
        background: transparent !important;
    }
    .stHeader { display: none !important; }
    
    /* Ajusta e cola as caixas no teto absoluto agora que a barra branca morreu */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta as amarras cinzas nativas padrão */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* 🧱 DIVISÃO EXATA DE DUAS COLUNAS LARGAS DO SEU PRINT (LATERAL ESQUERDA + CENTRAL AMPLA) */
    .coluna-menu-lateral {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        min-height: 85vh;
    }
    
    .coluna-conteudo-central {
        background-color: transparent;
        padding-left: 20px;
        min-height: 85vh;
    }

    /* 🟢 A CAIXA HOLOGRÁFICA DO SEU PRINT COM AS BORDAS EM DEGRADÊ PISCANTE MÁXIMO */
    @keyframes borda-holografica-ativa {
        0% { border-color: #00E5FF; box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); }
        50% { border-color: #00FF87; box-shadow: 0 0 25px rgba(0, 255, 135, 0.5); }
        100% { border-color: #00E5FF; box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); }
    }
    
    .caixa-holografica-print {
        background-color: #080f1d !important;
        border: 2.5px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 28px !important;
        margin-bottom: 30px !important;
        animation: borda-holografica-ativa 4s infinite ease-in-out !important;
    }
    
    /* Estilo das caixas de status de baixo */
    .header-box-real {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 16px 20px !important;
        margin-bottom: 20px !important;
    }
    
    .kpi-card-real {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    /* 💎 DESIGN DOS BOTÕES DE CARBONO EXECUTIVO DA COLUNA 1 (FIM DA APARÊNCIA FEIA) */
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
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* 🔥 HOVER EXECUTIVO NEON: PISCA E DESLIZA SUAVEMENTE */
    .menu-lateral-container div.stButton > button:hover {
        animation: borda-holografica-ativa 1.5s infinite ease-in-out !important;
        background: #1e293b !important;
        color: #00FF87 !important; 
        transform: translateX(4px) !important; 
    }
    
    /* Botão de voz redondo do seu modelo */
    .btn-voz-modelo div.stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #10b981 100%) !important;
        color: #0b111e !important;
        font-weight: 800 !important;
        text-align: center !important;
        width: auto !important;
        padding: 10px 22px !important;
        border-radius: 20px !important;
        font-size: 11px !important;
        border: none !important;
        letter-spacing: 0.5px;
    }
    
    .btn-acao-real div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important; font-weight: bold !important; border: none !important; text-align: center !important; padding: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# Memória de navegação limpa do SaaS
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Dashboard"

# =============================================================================================================
# ESTRUTURA HORIZONTAL DE 2 COLUNAS (0.25 LATERAL MENU + 0.75 CENTRAL INTEIRA DO PRINT)
# =============================================================================================================
col_esquerda, col_centro = st.columns([0.25, 0.75])

# 🏢 COLUNA 1 (FIXA): LOGO + BOTÕES OPERACIONAIS SUTIS NA LATERAL ESQUERDA
with col_esquerda:
    st.markdown('<div class="coluna-menu-lateral">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>ENTERPRISE CONTROL CENTER</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    if st.button("📝 3. Gerador de Anúncios", key="m_gerador"): st.session_state.modulo_ativo = "Gerador"; st.rerun()
    if st.button("🏹 4. Caçador de Ofertas", key="m_cacador"): st.session_state.modulo_ativo = "Cacador"; st.rerun()
    if st.button("🌐 5. Construtor Pre-Cell", key="m_presell"): st.session_state.modulo_ativo = "PreCell"; st.rerun()
    if st.button("🚀 6. Ativador Google API", key="m_google"): st.session_state.modulo_ativo = "GoogleAds"; st.rerun()
    if st.button("💎 7. Área de Assinantes", key="m_assinantes"): st.session_state.modulo_ativo = "Assinantes"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 🏢 COLUNA 2 (AMPLA): A ÁREA CENTRAL TOTALMENTE COPIADA DO SEU MODELO CAMPEÃO
with col_centro:
    st.markdown('<div class="coluna-conteudo-central">', unsafe_allow_html=True)
    
    # 🟢 CLONE EXATO DA SUA CAIXA DO PRINT LINHA POR LINHA COM BORDAS EM DEGRADÊ NEON COORDENADO
    st.markdown("""
    <div class="caixa-holografica-print">
        <h3 style="color: #00FF87; font-size: 22px; font-weight: 800; margin: 0 0 20px 0; display: flex; align-items: center; font-family: sans-serif;">
            <span style="margin-right: 12px;">🛸</span> PLATAFORMA HOLOGRÁFICA: ADRIEL AI
        </h3>
        <p style="color: #cbd5e1; font-size: 15px; line-height: 1.7; margin-bottom: 25px; font-family: sans-serif; font-weight: 500;">
            "Seja muito bem-vindo, Comandante José Marques da Silva! O cenário operacional está fixado em 3D. 
            Observe que as bordas flutuantes alternam de cor continuamente entre Ciano e Verde Neon, reproduzindo o 
            mesmo estilo requintado da interface do robô inteligente. Clique em qualquer lugar da tela para ativar os 
            alto-falantes."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ROTEADOR DE TRÁFEGO OPERANDO ABAIXO DA CAIXA GIGANTE
    if st.session_state.modulo_ativo == "Dashboard":
        st.markdown("### 📊 STATUS DA INFRAESTRUTURA EM TEMPO REAL")
        st.write("")
        col_m1, col_m2, col_m3 = st.columns(3)
