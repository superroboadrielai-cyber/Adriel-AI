import streamlit as st

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 🚨 COMANDO CIRÚRGICO: EXTERMINA A BARRA BRANCA DO TOPO SEM TOCAR NA SUA INTERFACE
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Premium Cyber Onyx Fiel ao seu Print */
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
    
    /* Ajusta o espaçamento do teto absoluto */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta de forma definitiva as abas nativas cinzas padrão dos servidores */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* CORREÇÃO DO BUG DOS QUADRADOS BRANCOS: FORÇA OS BOTÕES LATERAIS A SEREM CARBONO PREMIUM POR EXTENSO */
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
    
    /* CONSERTO DA CAIXA CENTRAL: RETORNA A MOLDURA HOLOGRÁFICA DO SEU PRINT CAMPEÃO */
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2.5px solid #00E5FF !important;
        border-radius: 14px !important;
        padding: 26px !important;
        margin-bottom: 25px !important;
    }

    /* RESTAURAÇÃO DO SEU LINDO BOTÃO VERDE ORIGINAL DE ÁUDIO DO INÍCIO */
    .btn-voz-modelo-print div.stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #10b981 100%) !important;
        color: #0b111e !important;
        font-weight: 800 !important;
        text-align: center !important;
        width: auto !important;
        padding: 12px 26px !important;
        border-radius: 30px !important;
        font-size: 13px !important;
        border: none !important;
        letter-spacing: 0.5px;
        cursor: pointer !important;
    }
    .btn-voz-modelo-print div.stButton > button:hover {
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA EXATAMENTE O SEU TEXTO DO PRINT)
# =============================================================================================================
texto_boas_vindas = "Seja muito bem-vindo, Comandante José Marques da Silva! A estrutura mestre está calibrada. Observe que as bordas da central alternam de cor e o meu Chassi Digitalizado está navegando em patrulha e flutuando na parte inferior do software. Clique na tela para ativar os alto-falantes."

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
# MONTAGEM RIGOROSA DE DUAS COLUNAS VERTICAIS PARALELAS SÍNCRONAS
# =============================================================================================================
col_esquerda, col_centro = st.columns([0.25, 0.75])

# 🏢 COLUNA 1: RETORNO DOS SEUS BOTÕES POR EXTENSO (FIM DOS QUADRADOS EM BRANCO)
with col_esquerda:
    st.write("")
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    st.button("🎛️ Dashboard", key="btn_app_final")
    st.button("🛰️ 1. Radar", key="btn_rad_final")
    st.button("🔬 2. Auditor", key="btn_aud_final")
    st.button("📝 3. Anúncios", key="btn_ger_final")
    st.button("🏹 4. Caçador", key="btn_cac_final")
    st.button("🌐 5. Pre-Cell", key="btn_pre_final")
    st.button("🚀 6. API Ads", key="btn_ati_final")
    st.button("💎 7. Painel", key="btn_ass_final")
    st.markdown('</div>', unsafe_allow_html=True)

# 🏢 COLUNA 2: SUA CAIXA DO PRINT INTACTA E RECHEADA
with col_centro:
    st.write("")
    st.markdown("""
    <div class="caixa-holografica-real-print">
        <h3 style="color: #00FF87; font-size: 21px; font-weight: 800; margin: 0 0 16px 0; font-family: sans-serif;">
            🌲 CENTRAL DE INTELIGÊNCIA: ADRIEL AI
        </h3>
        <p style="color: #cbd5e1; font-size: 15px; line-height: 1.7; margin-bottom: 0px; font-family: sans-serif; font-weight: 500;">
            "Seja muito bem-vindo, Comandante José Marques da Silva! A estrutura mestre está calibrada. 
            Observe que as bordas da central alternam de cor e o meu Chassi Digitalizado está navegando em patrulha e 
            flutuando na parte inferior do software. Clique na tela para ativar os alto-falantes."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🟢 SEU LINDO BOTÃO VERDE ORIGINAL COMPACTADO NO LUGAR DA CAIXINHA CINZA FEIA
    st.markdown('<div class="btn-voz-modelo-print">', unsafe_allow_html=True)
    st.button("SISTEMA COM ÁUDIO DE VOZ ATIVO 🔊", key="btn_voz_print_vibrante")
    st.markdown('</div>', unsafe_allow_html=True)
