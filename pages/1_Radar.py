import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO LUXO CYBERPUNK (CSS INJETADO)
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
        margin-bottom: 5px;
    }

    div[data-testid="stHorizontalBlock"] { gap: 14px !important; }
    
    /* Configuração dos Botões Gerais */
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
    
    /* 🔴 Botões Piscando em Vermelho (ALTA) */
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

    /* 🟢 Botões Piscando em Verde (VALIDADO) */
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

    /* 🔵 Botão de Info */
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
st.write("Ecosistema completo de monitoramento e auditoria estruturada da gringa em tempo real.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE DADOS GLOBAL COM EXATAMENTE 20 PRODUTOS (AUDITORIA AVANÇADA COMPLETA)
PRODUTOS_DADOS = [
    # ---- TOP 10 (SÍMBOLO DE ALTA - PISCANDO EM VERMELHO) ----
    {
        "ranking": 1, "nome": "Alpilean", "plataforma": "ClickBank", "tipo": "Nutracêutico", "status": "🔥 ALTA", 
        "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Baixa temperatura interna que desacelera o metabolismo e impede a queima calórica mesmo com dietas severas.", 
        "beneficios": ["Aumento da queima calórica em repouso", "Regulação da temperatura interna celular", "Energia limpa sustentada sem picos"],
        "paises": {"USA": {"cpc": "$2.80", "int": "Extremo"}, "UK": {"cpc": "$1.90", "int": "Alto"}, "CA": {"cpc": "$2.10", "int": "Médio"}, "AU": {"cpc": "$2.30", "int": "Alto"}, "DE": {"cpc": "$1.40", "int": "Médio"}},
        "porque": "Volume imbatível de pesquisas exatas fundo de funil na rede de pesquisa do Google Ads.", "grafico": [30, 45, 40, 60, 55, 70, 65, 85, 80, 95, 90, 100]
    },
    {
        "ranking": 2, "nome": "Puravive", "plataforma": "ClickBank", "tipo": "Emagrecimento", "status": "🔥 ALTA", 
        "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Falta de ativação do tecido adiposo marrom (BAT), gerando acúmulo crônico de gordura abdominal difícil de eliminar.", 
        "beneficios": ["Multiplicação do tecido adiposo marrom", "Queima acelerada de gordura localizada", "Desintoxicação corporal total"],
        "paises": {"USA": {"cpc": "$3.10", "int": "Muito Alto"}, "UK": {"cpc": "$2.20", "int": "Alto"}, "CA": {"cpc": "$2.40", "int": "Alto"}, "AU": {"cpc": "$2.50", "int": "Alto"}, "DE": {"cpc": "$1.60", "int": "Baixo"}},
        "porque": "Baixa concorrência de afiliados e alto valor de comissão por checkout internacional.", "grafico": [20, 35, 30, 50, 45, 65, 60, 75, 70, 85, 80, 95]
    },
    {
        "ranking": 3, "nome": "Java Burn", "plataforma": "BuyGoods", "tipo": "Suplemento", "status": "🔥 ALTA", 
        "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", 
        "dor_principal": "Lentidão metabólica diária e indisposição física e mental logo no início da manhã.", 
        "beneficios": ["Aceleração instantânea do metabolismo", "Foco cognitivo ampliado", "Sem crises de ansiedade comuns do café"],
        "paises": {"USA": {"cpc": "$2.90", "int": "Alto"}, "UK": {"cpc": "$1.85", "int": "Muito Alto"}, "CA": {"cpc": "$2.05", "int": "Médio"}, "AU": {"cpc": "$2.15", "int": "Alto"}, "DE": {"cpc": "$1.35", "int": "Médio"}},
        "porque": "Desempenho massivo no tráfego do mercado do Reino Unido, gerando leilões mais baratos que nos EUA.", "grafico": [40, 50, 45, 55, 60, 70, 65, 75, 80, 85, 90, 95]
    },
    {
        "ranking": 4, "nome": "GlucoTrust", "plataforma": "ClickBank", "tipo": "Diabetes", "status": "🔥 ALTA", 
        "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Picos elevados e perigosos de açúcar no sangue associados a ataques de fome por doces durante a madrugada.", 
        "beneficios": ["Estabilização da glicose natural", "Redução de ansiedade por carboidratos", "Melhoria profunda da qualidade do sono"],
        "paises": {"USA": {"cpc": "$3.40", "int": "Extremo"}, "UK": {"cpc": "$2.40", "int": "Médio"}, "CA": {"cpc": "$2.60", "int": "Alto"}, "AU": {"cpc": "$2.80", "int": "Alto"}, "DE": {"cpc": "$1.80", "int": "Médio"}},
        "porque": "Público comprador sênior qualificado com facilidade de comprar pacotes com múltiplos potes.", "grafico": [15, 25, 35, 45, 40, 55, 50, 65, 60, 75, 70, 85]
    },
    {
        "ranking": 5, "nome": "ProDentim", "plataforma": "ClickBank", "tipo": "Saúde Bucal", "status": "🔥 ALTA", 
        "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", 
        "dor_principal": "Mau hálito crônico persistente, sangramento na gengiva ao escovar e enfraquecimento precoce do esmalte.", 
        "beneficios": ["Repovoamento de bactérias boas na boca", "Clareamento natural e hálito fresco", "Fortalecimento gengival imediato"],
        "paises": {"USA": {"cpc": "$2.60", "int": "Alto"}, "UK": {"cpc": "$1.70", "int": "Médio"}, "CA": {"cpc": "$1.95", "int": "Muito Alto"}, "AU": {"cpc": "$2.10", "int": "Alto"}, "DE": {"cpc": "$1.20", "int": "Baixo"}},
        "porque": "Nicho premium de altíssima conversão em campanhas focadas no Google Search.", "grafico": [50, 55, 60, 65, 70, 75, 80, 85, 90, 92, 95, 98]
    },
    {
        "ranking": 6, "nome": "Liv Pure", "plataforma": "ClickBank", "tipo": "Detox Hepático", "status": "🔥 ALTA", 
        "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Fígado sobrecarregado por toxinas alimentares que bloqueiam a queima de gordura pelo organismo.", 
        "beneficios": ["Purificação celular do fígado", "Otimização da queima lipídica", "Aumento drástico de energia diária"],
        "paises": {"USA": {"cpc": "$3.20", "int": "Muito Alto"}, "UK": {"cpc": "$2.10", "int": "Médio"}, "CA": {"cpc": "$2.35", "int": "Alto"}, "AU": {"cpc": "$2.45", "int": "Alto"}, "DE": {"cpc": "$1.55", "int": "Baixo"}},
        "porque": "VSL altamente persuasiva estruturada pelo produtor gringo que explode as vendas no tráfego.", "grafico": [25, 30, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90]
    },
    {
        "ranking": 7, "nome": "Ikaria Lean Belly", "plataforma": "ClickBank", "tipo": "Suplemento Pó", "status": "🔥 ALTA", 
        "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", 
        "dor_principal": "Inflamação corporal generalizada e altos níveis de ceramidas nocivas bloqueando as artérias.", 
