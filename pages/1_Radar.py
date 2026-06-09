import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO ULTRA LUXO E ANIMAÇÕES NEON PISCANTES (CSS INJETADO)
st.markdown("""
    <style>
    .stApp { background-color: #060913; color: #f8fafc; }
    h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
    
    .titulo-cyber {
        font-size: 2.7rem;
        font-weight: 900;
        background: linear-gradient(45deg, #ff0055, #00ffcc, #9900ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }

    div[data-testid="stHorizontalBlock"] { gap: 14px !important; }
    
    /* Configuração Base dos Botões de Luxo */
    div[data-testid="stColumn"] button {
        background: #0f1526 !important;
        border-radius: 12px !important;
        padding: 14px 10px !important;
        min-height: 52px !important;
        width: 100% !important;
        display: block !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stColumn"] button p {
        font-size: 15px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    
    /* 🔴 Animação Piscante para os Botões em ALTA */
    @keyframes pulseVermelho {
        0% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055, inset 0 0 2px #ff0055; }
        50% { border-color: #ff4d88; box-shadow: 0 0 18px #ff0055, inset 0 0 8px #ff0055; }
        100% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055, inset 0 0 2px #ff0055; }
    }
    .btn-alta button {
        border: 2px solid #ff0055 !important;
        animation: pulseVermelho 2s infinite !important;
    }
    .btn-alta button p { color: #ff4d88 !important; }
    .btn-alta button:hover { background: #ff0055 !important; transform: scale(1.02); }
    .btn-alta button:hover p { color: #ffffff !important; }

    /* 🟢 Animação Piscante para os Botões VALIDADOS */
    @keyframes pulseVerde {
        0% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc, inset 0 0 2px #00ffcc; }
        50% { border-color: #33ffdd; box-shadow: 0 0 18px #00ffcc, inset 0 0 8px #00ffcc; }
        100% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc, inset 0 0 2px #00ffcc; }
    }
    .btn-validado button {
        border: 2px solid #00ffcc !important;
        animation: pulseVerde 2.5s infinite !important;
    }
    .btn-validado button p { color: #33ffdd !important; }
    .btn-validado button:hover { background: #00ffcc !important; transform: scale(1.02); }
    .btn-validado button:hover p { color: #060913 !important; }

    /* 🔵 Botão de Informações Roxo Premium */
    .btn-info button {
        border: 2px solid #9900ff !important;
        box-shadow: 0 0 8px rgba(153, 0, 255, 0.3) !important;
    }
    .btn-info button p { color: #cc66ff !important; }
    .btn-info button:hover { background: #9900ff !important; box-shadow: 0 0 18px #9900ff !important; }
    .btn-info button:hover p { color: #ffffff !important; }
    
    /* Badges e Cards */
    .badge-alta-cyber {
        background-color: #2a0813; color: #ff4d88 !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #ff0055; display: inline-block;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
    }
    .badge-normal-cyber {
        background-color: #04251d; color: #33ffdd !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #00ffcc; display: inline-block;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
    }
    .card-cyber-info {
        background: #0f1526; border: 2px solid #1e293b;
        padding: 24px; border-radius: 16px; margin-top: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Acompanhe o maior ecossistema de monitoramento perpétuo da gringa com atualização em tempo real.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE DADOS COMPLETA COM EXATAMENTE 20 PRODUTOS VALIDADOS (EVERGREEN)
PRODUTOS_DADOS = [
    # ---- TOP 10 (SÍMBOLO DE ALTA - PISCANDO EM VERMELHO) ----
    {"ranking": 1, "nome": "Alpilean", "plataforma": "ClickBank", "tipo": "Nutracêutico", "status": "🔥 ALTA", "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "dor_principal": "Metabolismo travado e baixa temperatura interna celular que impede o emagrecimento.", "porque": "Volume massivo de buscas de fundo de funil e criativos de alta conversão.", "grafico": [45, 55, 62, 70, 68, 75, 85, 90, 95, 110, 105, 112]},
    {"ranking": 2, "nome": "Puravive", "plataforma": "ClickBank", "tipo": "Emagrecimento", "status": "🔥 ALTA", "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "dor_principal": "Falta de ativação do tecido adiposo marrom, acumulando gordura profunda e resistente.", "porque": "Baixo índice de reembolso nas plataformas gringas e alta comissão por pote vendido.", "grafico": [30, 42, 50, 58, 61, 70, 78, 83, 89, 92, 95, 98]},
    {"ranking": 3, "nome": "Java Burn", "plataforma": "BuyGoods", "tipo": "Suplemento", "status": "🔥 ALTA", "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "dor_principal": "Falta de energia logo pela manhã e lentidão crônica na queima de gordura diária.", "porque": "Excelente aceitação em massa no mercado europeu com leilão de CPC menor que os EUA.", "grafico": [50, 48, 55, 60, 65, 72, 70, 74, 80, 85, 83, 87]},
    {"ranking": 4, "nome": "GlucoTrust", "platform": "ClickBank", "tipo": "Diabetes", "status": "🔥 ALTA", "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", "dor_principal": "Picos elevados de açúcar na corrente sanguínea e desejo incontrolável por doces à noite.", "porque": "Público comprador muito qualificado acima de 45 anos e com alto poder aquisitivo.", "grafico": [60, 62, 59, 64, 68, 70, 73, 71, 75, 78, 72, 74]},
    {"ranking": 5, "nome": "ProDentim", "platform": "ClickBank", "tipo": "Saúde Bucal", "status": "🔥 ALTA", "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", "dor_principal": "Mau hálito insuportável, cáries frequentes e sangramentos sérios na gengiva.", "porque": "Nicho com concorrência absurdamente baixa em rede de pesquisa do Google Ads.", "grafico": [40, 43, 47, 51, 56, 54, 59, 63, 61, 65, 67, 69]},
    {"ranking": 6, "nome": "Liv Pure", "platform": "ClickBank", "tipo": "Detox Hepático", "status": "🔥 ALTA", "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", "dor_principal": "Fígado intoxicado por gordura que paralisa o funcionamento natural do metabolismo.", "porque": "Funil de vendas agressivo do produtor que gera muitos upsells na mesma compra.", "grafico": [35, 38, 42, 48, 52, 50, 55, 58, 60, 62, 61, 65]},
    {"ranking": 7, "nome": "Ikaria Lean Belly", "platform": "ClickBank", "tipo": "Suplemento Pó", "status": "🔥 ALTA", "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", "dor_principal": "Altas concentrações de ácido úrico que inflamam as articulações e inflamam o abdômen.", "porque": "Formato inovador em pó que gera alta curiosidade e cliques qualificados nos anúncios.", "grafico": [25, 29, 34, 40, 45, 48, 52, 55, 53, 58, 60, 61]},
    {"ranking": 8, "nome": "Cortexi", "platform": "ClickBank", "tipo": "Audição", "status": "🔥 ALTA", "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)", "dor_principal": "Zumbido estridente no ouvido que impede o sono e causa extrema perda de foco.", "porque": "Nicho de dor latente onde o cliente compra no desespero para resolver o problema.", "grafico": [20, 24, 28, 35, 41, 45, 49, 52, 50, 54, 56, 58]},
    {"ranking": 9, "nome": "FlowForce Max", "platform": "BuyGoods", "tipo": "Saúde Masculina", "status": "🔥 ALTA", "buscas_mes": 54000, "buscas_hoje": 1050, "melhor_pais": "Estados Unidos (USA)", "dor_principal": "Próstata inflamada forçando idas dolorosas e constantes ao banheiro durante as noites.", "porque": "OFERTA Fundo de Funil excelente para vender na rede de pesquisa do Google Ads.", "grafico": [15, 22, 26, 31, 37, 40, 44, 48, 47, 51, 52, 54]},
    {"ranking": 10, "nome": "Metanail Serum", "platform": "ClickBank", "tipo": "Unhas/Estética", "status": "🔥 ALTA", "buscas_mes": 51000, "buscas_hoje": 980, "melhor_pais": "Canadá (CA)", "dor_principal": "Fungos severos amarelos que destroem, quebram e deixam as unhas feias.", "porque": "Apelo visual fortíssimo, ideal para vender escalando com tráfego no Youtube Ads.", "grafico": [18, 20, 25, 28, 33, 36, 40, 43, 42, 46, 48, 51]},
    # ---- OUTROS 10 VALIDADOS (SÍMBOLO NORMAL - PISCANDO EM VERDE COM BAIXA CONCORRÊNCIA) ----
    {"ranking": 11, "nome": "LeanBliss", "platform": "BuyGoods", "tipo": "Nutracêutico", "status": "✅ VALIDADO", "buscas_mes": 14500, "buscas_hoje": 320, "melhor_pais": "Austrália (AU)", "dor_principal": "Ganho rápido de peso associado a picos de ansiedade por comida e descontrole de açúcar.", "porque": "Pouquíssimos afiliados anunciando na Austrália, gerando leilões vazios de CPC.", "grafico": [10, 12, 11, 13, 14, 15, 14, 16, 15, 17, 16, 14]},
    {"ranking": 12, "nome": "Neotonics", "platform": "ClickBank", "tipo": "Pele e Intestino", "status": "✅ VALIDADO", "buscas_mes": 13200, "buscas_hoje": 290, "melhor_pais": "Alemanha (DE)", "dor_principal": "Flacidez cutânea e rugas geradas por envelhecimento celular precoce do estômago.", "porque": "Perfeito para criar artigos Review de alta conversão em blogs nativos na Europa.", "grafico": [9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 13]},
