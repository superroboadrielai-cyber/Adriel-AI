import streamlit as st

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 🚨 COMANDO INVISÍVEL COORDENADO: DELETA A BARRA BRANCA DO TOPO SEM TOCAR NA SUA ESTRUTURA
# =============================================================================================================
st.markdown("""
<style>
    /* Fundo Escuro Original do seu Print */
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
    
    /* Puxa todo o seu conteúdo original e cola no teto absoluto do monitor */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta de forma definitiva as abas nativas cinzas padrão dos servidores */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }
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
# REPLICAÇÃO CIRÚRGICA DA ESTRUTURA DO SEU PRINT ORIGINAL DO MARCO ZERO
# =============================================================================================================

# Injeção de CSS interno para manter os seus blocos e os seus botões laterais originais intactos
st.markdown("""
<style>
    /* Estilo das duas colunas originais do print */
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
    }
    
    /* Animação contínua da sua moldura holográfica ciano do print */
    @keyframes pulso-holografico-original {
        0% { border-color: #00E5FF; box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); }
        50% { border-color: #00FF87; box-shadow: 0 0 20px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); }
    }
    
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2.5px solid #00E5FF !important;
        border-radius: 14px !important;
        padding: 26px !important;
        margin-bottom: 25px !important;
        animation: pulso-holografico-original 4s infinite ease-in-out !important;
    }
    
    /* Botão verde oval original de áudio colocado embaixo da caixa */
    .btn-voz-modelo-print div.stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #10b981 100%) !important;
        color: #0b111e !important;
        font-weight: 800 !important;
        text-align: center !important;
        width: auto !important;
        padding: 10px 22px !important;
        border-radius: 20px !important;
        font-size: 11px !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Separação exata das duas colunas (Menu Esquerdo + Conteúdo Amplo)
col_esquerda, col_centro = st.columns([0.25, 0.75])

# 🏢 COLUNA 1: SEUS BOTÕES ORIGINAIS DO PRINT
with col_esquerda:
    st.write("")
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    st.button("app", key="btn_app_orig")
    st.button("Radar", key="btn_rad_orig")
    st.button("Auditor", key="btn_aud_orig")
    st.button("Gerador", key="btn_ger_orig")
    st.button("Cacador", key="btn_cac_orig")
    st.button("Presell", key="btn_pre_orig")
    st.button("Ativador", key="btn_ati_orig")
    st.button("Assinantes", key="btn_ass_orig")
    st.markdown('</div>', unsafe_allow_html=True)

# 🏢 COLUNA 2: SUA CAIXA DO PRINT INTACTA E COPIADA LINHA POR LINHA
with col_centro:
    st.markdown(f"""
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
    
    # Seu botão oval verde original colocado abaixo da caixa
    st.markdown('<div class="btn-voz-modelo-print">', unsafe_allow_html=True)
    st.button("SISTEMA COM ÁUDIO DE VOZ ATIVO ⬪", key="btn_voz_print_fiel")
    st.markdown('</div>', unsafe_allow_html=True)
