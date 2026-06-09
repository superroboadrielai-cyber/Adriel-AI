import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO LUXO CYBERPUNK COM BOTOES PISCANDO EM NEON CONTINUO
st.markdown("""
    <style>
    .stApp { background-color: #050811; color: #f8fafc; }
    h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
    
    .titulo-luxury {
        font-size: 2.6rem;
        font-weight: 900;
        background: linear-gradient(45deg, #ff0055, #00ffcc, #9900ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }

    div[data-testid="stHorizontalBlock"] { gap: 14px !important; }
    
    /* Customização Estrutural dos Botões */
    div[data-testid="stColumn"] button {
        background: #0d1222 !important;
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
    
    /* 🔴 Botão Neon Piscante para Produtos em ALTA */
    @keyframes pulseVermelho {
        0% { border-color: #ff0055; box-shadow: 0 0 4px #ff0055, inset 0 0 2px #ff0055; }
        50% { border-color: #ff4d88; box-shadow: 0 0 16px #ff0055, inset 0 0 6px #ff0055; }
        100% { border-color: #ff0055; box-shadow: 0 0 4px #ff0055, inset 0 0 2px #ff0055; }
    }
    .btn-alta button {
        border: 2px solid #ff0055 !important;
        animation: pulseVermelho 2s infinite !important;
    }
    .btn-alta button p { color: #ff4d88 !important; }
    .btn-alta button:hover { background: #ff0055 !important; transform: scale(1.02); }
    .btn-alta button:hover p { color: #ffffff !important; }

    /* 🟢 Botão Neon Piscante para Produtos VALIDADOS */
    @keyframes pulseVerde {
        0% { border-color: #00ffcc; box-shadow: 0 0 4px #00ffcc, inset 0 0 2px #00ffcc; }
        50% { border-color: #33ffdd; box-shadow: 0 0 16px #00ffcc, inset 0 0 6px #00ffcc; }
        100% { border-color: #00ffcc; box-shadow: 0 0 4px #00ffcc, inset 0 0 2px #00ffcc; }
    }
    .btn-validado button {
        border: 2px solid #00ffcc !important;
        animation: pulseVerde 2.5s infinite !important;
    }
    .btn-validado button p { color: #33ffdd !important; }
    .btn-validado button:hover { background: #00ffcc !important; transform: scale(1.02); }
    .btn-validado button:hover p { color: #050811 !important; }

    /* 🔵 Botão de Info Premium */
    .btn-info button {
        border: 2px solid #9900ff !important;
        box-shadow: 0 0 8px rgba(153, 0, 255, 0.2) !important;
    }
    .btn-info button p { color: #cc66ff !important; }
    .btn-info button:hover { background: #9900ff !important; box-shadow: 0 0 16px #9900ff !important; }
    .btn-info button:hover p { color: #ffffff !important; }
    
    /* Central de Inteligência de Auditoria */
    .badge-alta-cyber {
        background-color: #25050f; color: #ff4d88 !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #ff0055; display: inline-block;
    }
    .badge-normal-cyber {
        background-color: #021e17; color: #33ffdd !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #00ffcc; display: inline-block;
    }
    .card-luxury {
        background: #0d1222; border: 2px solid #1e293b;
        padding: 24px; border-radius: 16px; margin-top: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }
    .cpc-box {
        background: #070a14; border: 1px solid #1e293b;
        padding: 8px 12px; border-radius: 8px; margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-luxury">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Estratégia avançada de inteligência competitiva e auditoria em tempo real para a gringa.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE DADOS COMPLETA E VALIDADA COM 20 PRODUTOS (SEM LINHAS INCOMPLETAS)
PRODUTOS_DADOS = [
    # ==== TOP 10 EM ALTA ====
    {
        "ranking": 1, "nome": "Alpilean", "platform": "ClickBank", "tipo": "Nutracêutico", "status": "🔥 ALTA",
        "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Metabolismo completamente paralisado devido à baixa temperatura interna do corpo.",
        "beneficios": "Aceleração térmica celular, derretimento de gordura profunda e ganho drástico de energia diária.",
        "cpc_paises": {"USA": "$2.80", "UK": "$1.90", "CA": "$2.10", "AU": "$2.30", "DE": "$1.45"},
        "porque": "Volume gigante de intenções de compra exatas. Audiência qualificada pronta para pacotes recorrentes.",
        "grafico": [45, 52, 60, 58, 65, 72, 80, 85, 92, 90, 98, 100]
    },
    {
        "ranking": 2, "nome": "Puravive", "platform": "ClickBank", "tipo": "Emagrecimento", "status": "🔥 ALTA",
        "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Falta de ativação do tecido adiposo marrom (BAT), acumulando gordura tóxica resistente.",
        "beneficios": "Multiplicação do tecido adiposo marrom, conversão energética limpa e queima calórica 24 horas.",
        "cpc_paises": {"USA": "$3.10", "UK": "$2.20", "CA": "$2.40", "AU": "$2.50", "DE": "$1.60"},
        "porque": "Baixíssimo índice de estorno no gateway e excelente material de criativos fornecido pelo produtor.",
        "grafico": [30, 42, 48, 55, 60, 68, 75, 79, 84, 88, 92, 98]
    },
    {
        "ranking": 3, "nome": "Java Burn", "platform": "BuyGoods", "tipo": "Suplemento", "status": "🔥 ALTA",
        "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)",
        "dor_principal": "Fadiga crônica logo ao acordar e lentidão extrema na oxidação de gorduras.",
        "beneficios": "Sinergia termogênica instantânea ao misturar no café, regulação hormonal e foco cognitivo.",
        "cpc_paises": {"USA": "$2.60", "UK": "$1.65", "CA": "$1.95", "AU": "$2.10", "DE": "$1.20"},
        "porque": "Forte aceitação cultural no Reino Unido. Mercado consumidor com leilão de CPC menor que os EUA.",
        "grafico": [50, 48, 55, 52, 63, 70, 68, 74, 81, 80, 85, 87]
    },
    {
        "ranking": 4, "nome": "GlucoTrust", "platform": "ClickBank", "tipo": "Diabetes", "status": "🔥 ALTA",
        "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Descontrole de açúcar sanguíneo e compulsão noturna por carboidratos simples.",
        "beneficios": "Estabilização da glicose, sono profundo reparador e redução da resistência à insulina.",
        "cpc_paises": {"USA": "$2.90", "UK": "$1.95", "CA": "$2.20", "AU": "$2.40", "DE": "$1.50"},
        "porque": "Público comprador sênior maduro com alto poder de compra para tratamentos de 6 meses.",
        "grafico": [40, 45, 50, 48, 55, 62, 60, 67, 72, 70, 74, 74]
    },
    {
        "ranking": 5, "nome": "ProDentim", "platform": "ClickBank", "tipo": "Saúde Bucal", "status": "🔥 ALTA",
        "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)",
        "dor_principal": "Deterioração das gengivas, mau hálito persistente e dentes enfraquecidos.",
        "beneficios": "Repovoamento de bactérias boas na boca, hálito fresco e reconstrução do esmalte dentário.",
        "cpc_paises": {"USA": "$3.40", "UK": "$2.40", "CA": "$2.25", "AU": "$2.60", "DE": "$1.80"},
        "porque": "Nicho premium de altíssima conversão rodando anúncios diretos na rede de pesquisa do Google.",
        "grafico": [35, 40, 45, 52, 50, 58, 64, 62, 69, 73, 70, 69]
    },
    {
        "ranking": 6, "nome": "Liv Pure", "platform": "ClickBank", "tipo": "Detox Hepático", "status": "🔥 ALTA",
        "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Sobrecarga de toxinas no fígado que bloqueia a capacidade do corpo de queimar calorias.",
        "beneficios": "Purificação total das células hepáticas e ativação do modo de queima rápida de gordura.",
        "cpc_paises": {"USA": "$2.75", "UK": "$1.80", "CA": "$2.00", "AU": "$2.15", "DE": "$1.35"},
        "porque": "Páginas de vendas altamente persuasivas com excelentes taxas de upsell integradas.",
        "grafico": [20, 25, 32, 40, 45, 52, 58, 60, 65, 63, 68, 65]
    },
    {
        "ranking": 7, "nome": "Ikaria Lean Belly", "platform": "ClickBank", "tipo": "Suplemento Pó", "status": "🔥 ALTA",
        "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)",
        "dor_principal": "Acúmulo de ceramidas e ácido úrico que inflamam os órgãos e geram gordura visceral.",
        "beneficios": "Bloqueio de toxinas inflamatórias, varredura de ácido úrico e perda de medidas abdominais.",
        "cpc_paises": {"USA": "$3.00", "UK": "$2.10", "CA": "$2.30", "AU": "$2.10", "DE": "$1.55"},
        "porque": "Formato inovador em pó que gera alta curiosidade e excelentes CTRs nos criativos.",
        "grafico": [30, 35, 33, 42, 48, 50, 55, 59, 62, 60, 64, 61]
    },
    {
        "ranking": 8, "nome": "Cortexi", "platform": "ClickBank", "tipo": "Audição", "status": "🔥 ALTA",
        "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)",
        "dor_principal": "Zumbido infernal contínuo no ouvido (Tinnitus) causando estresse e insônia crônica.",
        "beneficios": "Alívio dos ruídos, blindagem das células auditivas e nitidez de foco mental de curto prazo.",
        "cpc_paises": {"USA": "$2.50", "UK": "$1.55", "CA": "$1.80", "AU": "$1.95", "DE": "$1.15"},
