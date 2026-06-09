import streamlit as st
import random

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

# 3. BASE DE DADOS COMPLETA COM AUDITORIA ULTRA PROFISSONAL DE 20 PRODUTOS
PRODUTOS_DADOS = [
    # ---- TOP 10 (SÍMBOLO DE ALTA - PISCANDO EM VERMELHO) ----
    {
        "ranking": 1, "nome": "Alpilean", "plataforma": "ClickBank", "tipo": "Nutracêutico", "status": "🔥 ALTA", 
        "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Metabolismo travado e baixa temperatura interna celular que impede o emagrecimento.", 
        "publico": "Mulheres e Homens de 35 a 65 anos", "concorrencia": "Alta (Escala agressiva)", 
        "estrategia": "Rede de Pesquisa do Google Ads (Fundo de funil) + Pre-sell Blindada.",
        "porque": "Volume massivo de buscas institucionais quentes com alta intenção de compra imediata.", 
        "grafico": [45, 50, 65, 70, 85, 90, 95, 100, 98, 92, 88, 94]
    },
    {
        "ranking": 2, "nome": "Puravive", "plataforma": "ClickBank", "tipo": "Emagrecimento", "status": "🔥 ALTA", 
        "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Falta de ativação do tecido adiposo marrom, acumulando gordura profunda resistente.", 
        "publico": "Mulheres de 25 a 55 anos preocupadas com estética e saúde", "concorrencia": "Média-Alta",
        "estrategia": "Facebook Ads + Página de Advertorial nativo focado em storytelling.",
        "porque": "Baixo índice de reembolso nas plataformas gringas e alta comissão por pacotes grandes.", 
        "grafico": [30, 42, 55, 68, 72, 80, 85, 89, 95, 98, 91, 96]
    },
    {
        "ranking": 3, "nome": "Java Burn", "plataforma": "BuyGoods", "tipo": "Suplemento", "status": "🔥 ALTA", 
        "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", 
        "dor_principal": "Falta de energia logo pela manhã e lentidão crônica na queima de gordura diária.", 
        "publico": "Profissionais e rotinas exaustivas, 30 a 50 anos", "concorrencia": "Média (Excelente ROI)",
        "estrategia": "YouTube Ads (Vídeos review detalhados) + Campanhas do Bing Ads.",
        "porque": "Excelente aceitação no mercado europeu com leilão de CPC menor que os EUA.", 
        "grafico": [50, 52, 58, 62, 70, 75, 82, 85, 84, 89, 87, 91]
    },
    {
        "ranking": 4, "nome": "GlucoTrust", "plataforma": "ClickBank", "tipo": "Diabetes", "status": "🔥 ALTA", 
        "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Picos elevados de açúcar na corrente sanguínea e desejo incontrolável por doces à noite.", 
        "publico": "Homens e Mulheres de 45 a 70 anos", "concorrencia": "Média-Alta",
        "estrategia": "Google Ads (Rede de Pesquisa) mirando termos exatos do produto.",
        "porque": "Público comprador muito qualificado acima de 45 anos com alto poder aquisitivo para pacotes de 6 potes.", 
        "grafico": [60, 64, 62, 68, 71, 74, 73, 79, 81, 85, 80, 84]
    },
    {
        "ranking": 5, "nome": "ProDentim", "plataforma": "ClickBank", "tipo": "Saúde Bucal", "status": "🔥 ALTA", 
        "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", 
        "dor_principal": "Mau hálito insuportável, cáries frequentes e sangramentos sérios na gengiva.", 
        "publico": "Público geral, 40 a 65 anos preocupados com hálito e dentição", "concorrencia": "Baixa-Média",
        "estrategia": "Google Ads (Rede de Display posicionada em blogs de saúde) + Pesquisa.",
        "porque": "Nicho com concorrência absurdamente baixa e comissões robustas por venda realizada.", 
        "grafico": [40, 45, 52, 58, 60, 64, 69, 72, 75, 80, 81, 85]
    },
    {
        "ranking": 6, "nome": "Liv Pure", "plataforma": "ClickBank", "tipo": "Detox Hepático", "status": "🔥 ALTA", 
        "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Fígado intoxicado por gordura que paralisa o funcionamento natural do metabolismo.", 
        "publico": "Homens e Mulheres, 40 a 60 anos com padrão alimentar ocidental", "concorrencia": "Alta",
        "estrategia": "Native Ads (Taboola/Outbrain) direcionado para páginas de Quiz qualificadoras.",
        "porque": "Funil de vendas agressivo do produtor que gera muitos upsells na mesma jornada de compra.", 
        "grafico": [35, 41, 48, 52, 59, 63, 67, 70, 72, 76, 74, 79]
    },
    {
        "ranking": 7, "nome": "Ikaria Lean Belly", "plataforma": "ClickBank", "tipo": "Suplemento Pó", "status": "🔥 ALTA", 
        "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", 
        "dor_principal": "Altas concentrações de ácido úrico que inflamam as articulações e causam inchaço abdominal.", 
        "publico": "Homens e Mulheres de 35 a 55 anos focados em bem-estar integrado", "concorrencia": "Média",
        "estrategia": "Facebook Ads (Criativos em formato de notícia ou quebra de padrão) + Instagram.",
        "porque": "Formato inovador em pó que gera alta curiosidade e cliques muito qualificados nos anúncios.", 
        "grafico": [42, 46, 50, 55, 58, 61, 64, 68, 70, 73, 71, 75]
    },
    {
        "ranking": 8, "nome": "Cortexi", "plataforma": "ClickBank", "tipo": "Audição", "status": "🔥 ALTA", 
        "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)", 
        "dor_principal": "Zumbido estridente no ouvido que impede o sono e causa extrema perda de foco.", 
        "publico": "Idosos e profissionais expostos a ruídos, 50 a 75 anos", "concorrencia": "Média",
        "estrategia": "Google Ads Rede de Pesquisa focando em termos de 'revisão' e 'onde comprar'.",
        "porque": "Nicho de dor latente urgente, onde o cliente compra de forma imediata para aliviar o sofrimento.", 
