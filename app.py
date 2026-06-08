import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA EXATAMENTE O TEXTO DO SEU MODELO)
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
# INJEÇÃO DE CSS DE ALTO LUXO (ELIMINA 100% DA BARRA BRANCA, MARGENS DO TOPO E FIXA O DESIGN BLACK)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print do seu Modelo */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* 🚨 DELETO ABSOLUTO DA BARRA BRANCA DO TOPO DO STREAMLIT (ESTRELA, LÁPIS E ITENS) */
    [data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
    .stHeader { display: none !important; }
    
    /* 🚨 ZERA AS MARGENS DO TOPO: PUXA TODO O CONTEÚDO GRUDADO NO TETO DO MONITOR */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta as abas e amarras nativas antigas */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* 🧱 CONFIGURAÇÃO DAS DUAS COLUNAS PARALELAS SEM QUEBRAS EXECUTIVAS */
    .coluna-menu-lateral-preta {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        min-height: 85vh;
    }
    
    .coluna-conteudo-ampla {
        background-color: transparent;
        padding-left: 20px;
        min-height: 85vh;
    }

    /* 🟢 A MOLDURA HOLOGRÁFICA DO SEU MODELO CAMPEÃO COM BRILHO EM DEGRADÊ PISCANTE */
    @keyframes pulso-holografico-neon {
        0% { border-color: #00E5FF; box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); }
        50% { border-color: #00FF87; box-shadow: 0 0 25px rgba(0, 255, 135, 0.5); }
        100% { border-color: #00E5FF; box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); }
    }
    
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2.5px solid #00E5FF !important;
        border-radius: 14px !important;
        padding: 26px !important;
        margin-bottom: 25px !important;
        animation: pulso-holografico-neon 4s infinite ease-in-out !important;
    }
    
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

    /* 💎 DESTRANCAMENTO DOS BOTÕES LATERAIS: DEIXAM DE SER BRANCOS E VIRAM CARBONO EXECUTIVO */
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
    
    /* 🔥 HOVER EXECUTIVO NEON DA LATERAL: PISCA E ACENDE AO PASSAR O MOUSE */
    .menu-lateral-container div.stButton > button:hover {
        animation: pulso-holografico-neon 1.5s infinite ease-in-out !important;
        background: #1e293b !important;
        color: #00FF87 !important; 
        transform: translateX(4px) !important; 
    }
    
    /* Botões operacionais internos */
    .btn-acao-real div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important; font-weight: bold !important; border: none !important; text-align: center !important; padding: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do roteador de abas na memória RAM
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Dashboard"

# =============================================================================================================
# MONTAGEM PARALELA FIEL (ESQUERDA: MENU ONYX + DIREITA: MOLDURA GIGANTE HOLOGRÁFICA)
# =============================================================================================================
col_esquerda, col_centro = st.columns([0.25, 0.75])

# 🏢 COLUNA 1 (FIXA): MENU LATERAL DE BOTÕES EXECUTIVOS DE CARBONO QUE AGORA FUNCIONAM
with col_esquerda:
    st.markdown('<div class="coluna-menu-lateral-preta">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>ENTERPRISE CONTROL CENTER</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="btn_m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="btn_m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="btn_m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    if st.button("📝 3. Gerador de Anúncios", key="btn_m_gerador"): st.session_state.modulo_ativo = "Gerador"; st.rerun()
    if st.button("🏹 4. Caçador de Ofertas", key="btn_m_cacador"): st.session_state.modulo_ativo = "Cacador"; st.rerun()
    if st.button("🌐 5. Construtor Pre-Cell", key="btn_m_presell"): st.session_state.modulo_ativo = "PreCell"; st.rerun()
    if st.button("🚀 6. Ativador Google API", key="btn_m_google"): st.session_state.modulo_ativo = "GoogleAds"; st.rerun()
    if st.button("💎 7. Área de Assinantes", key="btn_m_assinantes"): st.session_state.modulo_ativo = "Assinantes"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 🏢 COLUNA 2 (AMPLA): A AREA CENTRAL EXATA DO SEU PRINT RESTAURADA
with col_centro:
    st.markdown('<div class="coluna-conteudo-ampla">', unsafe_allow_html=True)
    
    # 🟢 COPIA INTEGRAL E DESINFETADA DA SUA CAIXA DO PRINT (SEM DISCO VOADOR E COLADO NO TETO)
    st.markdown("""
    <div class="caixa-holografica-real-print">
        <h3 style="color: #00FF87; font-size: 22px; font-weight: 800; margin: 0 0 18px 0; font-family: sans-serif;">
            PLATAFORMA HOLOGRÁFICA: ADRIEL AI
        </h3>
        <p style="color: #cbd5e1; font-size: 15px; line-height: 1.7; margin-bottom: 10px; font-family: sans-serif; font-weight: 500;">
            "Seja muito bem-vindo, Comandante José Marques da Silva! O cenário operacional está fixado em 3D. 
            Observe que as bordas flutuantes alternam de cor continuamente entre Ciano e Verde Neon, reproduzindo o 
            mesmo estilo requintado da interface do robô inteligente. Clique em qualquer lugar da tela para ativar os 
            alto-falantes."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ROTEADOR DE RECURSOS ABAIXO DA MOLDURA GIGANTE
    if st.session_state.modulo_ativo == "Dashboard":
        st.markdown("### 📊 STATUS DA INFRAESTRUTURA EM TEMPO REAL")
        st.write("")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1: st.markdown('<div class="kpi-card-real"><span style="font-size:11px;color:#64748b;font-weight:bold;">👥 ELITE AFILIADOS</span><br><span style="font-size:22px;color:#ffffff;font-weight:800;">265 Ativos</span></div>', unsafe_allow_html=True)
        with col_m2: st.markdown('<div class="kpi-card-real"><span style="font-size:11px;color:#64748b;font-weight:bold;">🔥 CLIQUES MONITORADOS</span><br><span style="font-size:22px;color:#00FF87;font-weight:800;">14.250 mil</span></div>', unsafe_allow_html=True)
