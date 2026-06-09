import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO LUXO COM ANIMAÇÃO NEON CONTINUA (PISCANDO)
st.markdown("""
    <style>
    .stApp { background-color: #060913; color: #f8fafc; }
    h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
    
    .titulo-cyber {
        font-size: 2.5rem;
        font-weight: 900;
        color: #00ffcc;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
    }

    div[data-testid="stHorizontalBlock"] { gap: 14px !important; }
    
    /* Configuração de Luxo dos Botões */
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
    
    /* Animação Neon Pulsar para botões em ALTA (Vermelho) */
    @keyframes pulseVermelho {
        0% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
        50% { border-color: #ff4d88; box-shadow: 0 0 15px #ff0055; }
        100% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
    }
    .btn-alta button {
        border: 2px solid #ff0055 !important;
        animation: pulseVermelho 2s infinite !important;
    }
    .btn-alta button p { color: #ff4d88 !important; }
    .btn-alta button:hover { background: #ff0055 !important; }
    .btn-alta button:hover p { color: #ffffff !important; }

    /* Animação Neon Pulsar para botões VALIDADOS (Verde) */
    @keyframes pulseVerde {
        0% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
        50% { border-color: #33ffdd; box-shadow: 0 0 15px #00ffcc; }
        100% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
    }
    .btn-validado button {
        border: 2px solid #00ffcc !important;
        animation: pulseVerde 2.5s infinite !important;
    }
    .btn-validado button p { color: #33ffdd !important; }
    .btn-validado button:hover { background: #00ffcc !important; }
    .btn-validado button:hover p { color: #060913 !important; }

    /* Botão de Info Roxo */
    .btn-info button {
        border: 2px solid #9900ff !important;
    }
    .btn-info button p { color: #cc66ff !important; }
    .btn-info button:hover { background: #9900ff !important; }
    .btn-info button:hover p { color: #ffffff !important; }
    
    .badge-alta-cyber {
        background-color: #2a0813; color: #ff4d88 !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #ff0055; display: inline-block;
    }
    .badge-normal-cyber {
        background-color: #04251d; color: #33ffdd !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #00ffcc; display: inline-block;
    }
    .card-cyber-info {
        background: #0f1526; border: 2px solid #1e293b;
        padding: 24px; border-radius: 16px; margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema premium de monitoramento contínuo com auditoria detalhada de mercado gringo.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE DADOS COMPLETA COM EXATAMENTE 20 PRODUTOS VALIDADOS (SINTAXE LIMPA E FIXA)
PRODUTOS_DADOS = [
    {
        "ranking": 1, "nome": "Alpilean", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Nutracêutico",
        "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)",
        "dor": "Metabolismo travado por baixa temperatura interna celular.",
        "porque": "Volume alto de tráfego qualificado de fundo de funil.",
        "cpc": "USA: $2.80 | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40",
        "grafico": [45, 55, 60, 65, 75, 80, 85, 90, 95, 100, 110, 112]
    },
    {
        "ranking": 2, "nome": "Puravive", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Emagrecimento",
        "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)",
        "dor": "Falta de ativação do tecido adiposo marrom (BAT).",
        "porque": "Baixa taxa de reembolso e comissões altas por potes.",
        "cpc": "USA: $3.10 | UK: $2.20 | CA: $2.40 | AU: $2.50 | DE: $1.60",
        "grafico": [35, 42, 50, 58, 62, 70, 75, 83, 89, 92, 95, 98]
    },
    {
        "ranking": 3, "nome": "Java Burn", "status": "🔥 ALTA", "plataforma": "BuyGoods", "nicho": "Suplemento Café",
        "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)",
        "dor": "Falta de energia matinal e metabolismo lento no dia.",
        "porque": "Grande aceitação na Europa com leilão de levedura baixo.",
        "cpc": "USA: $2.60 | UK: $1.65 | CA: $1.95 | AU: $2.10 | DE: $1.30",
        "grafico": [20, 28, 35, 45, 50, 58, 62, 70, 74, 80, 83, 87]
    },
    {
        "ranking": 4, "nome": "GlucoTrust", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Diabetes",
        "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)",
        "dor": "Picos de açúcar no sangue e compulsão noturna por doces.",
        "porque": "Público alvo sênior acima de 45 anos com alto poder de compra.",
        "cpc": "USA: $2.95 | UK: $1.85 | CA: $2.15 | AU: $2.20 | DE: $1.45",
        "grafico": [50, 52, 55, 58, 60, 62, 65, 68, 70, 71, 73, 74]
    },
    {
        "ranking": 5, "nome": "ProDentim", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Saúde Bucal",
        "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)",
        "dor": "Mau hálito constante e inflamação crônica na gengiva.",
        "porque": "Concorrência controlada e excelente ROI em anúncios Bing.",
        "cpc": "USA: $2.40 | UK: $1.50 | CA: $1.75 | AU: $1.90 | DE: $1.20",
        "grafico": [30, 35, 38, 42, 48, 52, 55, 59, 61, 64, 66, 69]
    },
    {
        "ranking": 6, "nome": "Liv Pure", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Detox Fígado",
        "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)",
        "dor": "Fígado sobrecarregado impedindo queima natural de gordura.",
        "porque": "Funil de vendas forte do produtor gerando upsells recorrentes.",
        "cpc": "USA: $3.20 | UK: $2.10 | CA: $2.30 | AU: $2.40 | DE: $1.50",
        "grafico": [25, 30, 34, 40, 45, 49, 52, 56, 58, 60, 63, 65]
    },
    {
        "ranking": 7, "nome": "Ikaria Juice", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Suplemento Pó",
        "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)",
        "dor": "Altos níveis de ácido úrico gerando inchaço abdominal.",
        "porque": "Formato em pó inovador com ótima conversão visual.",
        "cpc": "USA: $2.85 | UK: $1.95 | CA: $2.05 | AU: $2.15 | DE: $1.35",
        "grafico": [15, 22, 28, 32, 38, 42, 45, 49, 53, 56, 59, 61]
    },
    {
        "ranking": 8, "nome": "Cortexi", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Audição",
        "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)",
        "dor": "Zumbido chato no ouvido tirando o sono e a paciência.",
        "porque": "Mercado focado em dor latente de resolução imediata.",
        "cpc": "USA: $2.50 | UK: $1.60 | CA: $1.80 | AU: $1.95 | DE: $1.15",
        "grafico": [40, 42, 44, 46, 48, 50, 52, 53, 55, 56, 57, 58]
    },
    {
        "ranking": 9, "nome": "FlowForce Max", "status": "🔥 ALTA", "plataforma": "BuyGoods", "nicho": "Saúde Homem",
        "buscas_mes": 54000, "buscas_hoje": 1050, "melhor_pais": "Estados Unidos (USA)",
        "dor": "Problemas de próstata forçando idas ao banheiro à noite.",
        "porque": "Excelente público comprador fundo de funil estruturado.",
        "cpc": "USA: $3.00 | UK: $2.00 | CA: $2.20 | AU: $2.30 | DE: $1.40",
        "grafico": [18, 23, 27, 31, 35, 39, 42, 45, 48, 50, 52, 54]
    },
    {
        "ranking": 10, "nome": "Metanail Serum", "status": "🔥 ALTA", "plataforma": "ClickBank", "nicho": "Unhas/Estética",
        "buscas_mes": 51000, "buscas_hoje": 980, "melhor_pais": "Canadá (CA)",
        "dor": "Fungos e micoses persistentes amarelas destruindo as unhas.",
        "porque": "Apelo visual incrível e excelente para rodar no YouTube Ads.",
        "cpc": "USA: $2.35 | UK: $1.45 | CA: $1.65 | AU: $1.80 | DE: $1.10",
        "grafico": [10, 15, 19, 23, 28, 32, 35, 39, 42, 45, 48, 51]
    },
    {
        "ranking": 11, "nome": "LeanBliss", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "nicho": "Suplemento",
        "buscas_mes": 14500, "buscas_hoje": 320, "melhor_pais": "Austrália (AU)",
        "dor": "Ganho rápido de peso associado a picos de ansiedade.",
        "porque": "Poucos afiliados anunciando, leilões vazios de CPC.",
        "cpc": "USA: $1.90 | UK: $1.20 | CA: $1.40 | AU: $1.50 | DE: $0.95",
        "grafico": [5, 7, 9, 10, 11, 12, 12, 13, 13, 14, 14, 14]
    },
    {
        "ranking": 12, "nome": "Neotonics", "status": "✅ VALIDADO", "plataforma": "ClickBank", "nicho": "Pele/Estômago",
        "buscas_mes": 13200, "buscas_hoje": 290, "melhor_pais": "Alemanha (DE)",
        "dor": "Flacidez e rugas causadas por envelhecimento celular interno.",
        "porque": "Perfeito para criar artigos de Review de alta conversão.",
        "cpc": "USA: $2.10 | UK: $1.30 | CA: $1.50 | AU: $1.60 | DE: $1.10",
        "grafico": [4, 5, 6, 7, 8, 9, 9, 10, 11, 11, 12, 13]
    },
    {
        "ranking": 13, "nome": "Synogut", "status": "✅ VALIDADO", "plataforma": "ClickBank", "nicho": "Digestão",
