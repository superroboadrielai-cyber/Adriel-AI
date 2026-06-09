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
        font-size: 14px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    
    /* Animação Piscante para os Botões em ALTA */
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

    /* Animação Piscante para os Botões VALIDADOS */
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

    /* Botão de Informações Roxo Premium */
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

# 3. BASE DE DADOS COMPLETA COM AUDITORIA PROFISSIONAL (20 PRODUTOS VALIDADOS)
PRODUTOS_DADOS = [
    # ---- TOP 10 (SÍMBOLO DE ALTA - VERMELHO PISCANTE) ----
    {
        "ranking": 1, "nome": "Alpilean", "plataforma": "ClickBank", "tipo": "Nutracêutico", "status": "🔥 ALTA", 
        "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Metabolismo travado e baixa temperatura interna celular que impede totalmente o emagrecimento.", 
        "porque": "Volume massivo de buscas de fundo de funil e criativos de alta conversão para público sênior.", 
        "concorrencia": "Alta (Leilão disputado)", "cpc_medio": "$2.80 - $3.90", "funil": "Google Ads (Fundo de Funil)", 
        "avatar": "Mulheres e Homens acima de 45 anos focados em saúde e perda de peso sem dietas radicais.",
        "grafico": 
    },
    {
        "ranking": 2, "nome": "Puravive", "plataforma": "ClickBank", "tipo": "Emagrecimento", "status": "🔥 ALTA", 
        "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Falta de ativação do tecido adiposo marrom (BAT), acumulando gordura profunda e resistente.", 
        "porque": "Baixo índice de reembolso nas plataformas gringas e alta comissão por pacotes de potes.", 
        "concorrencia": "Média-Alta", "cpc_medio": "$2.30 - $3.40", "funil": "YouTube Ads + Pre-Sell de Quiz", 
        "avatar": "Mulheres de 35 a 60 anos que buscam soluções baseadas em ingredientes naturais e exóticos.",
        "grafico": 
    },
    {
        "ranking": 3, "nome": "Java Burn", "plataforma": "BuyGoods", "tipo": "Suplemento", "status": "🔥 ALTA", 
        "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", 
        "dor_principal": "Falta de energia logo pela manhã e lentidão crônica na queima calórica diária.", 
        "porque": "Excelente aceitação em massa no mercado europeu com leilão de CPC menor que os Estados Unidos.", 
        "concorrencia": "Média", "cpc_medio": "$1.80 - $2.70", "funil": "Google Ads ou Bing Ads (Fundo de Funil)", 
        "avatar": "Trabalhadores e entusiastas de café (30 a 55 anos) que querem emagrecer adicionando o produto na rotina diária.",
        "grafico": 
    },
    {
        "ranking": 4, "nome": "GlucoTrust", "plataforma": "ClickBank", "tipo": "Diabetes", "status": "🔥 ALTA", 
        "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Picos elevados de açúcar na corrente sanguínea e desejo incontrolável por doces no período da noite.", 
        "porque": "Público comprador altamente qualificado acima de 50 anos e com alta recorrência de compra.", 
        "concorrencia": "Alta (Leilão aquecido)", "cpc_medio": "$3.10 - $4.50", "funil": "Google Ads (Rede de Pesquisa)", 
        "avatar": "Pessoas de meia-idade e idosos pré-diabéticos que buscam controle de glicose natural.",
        "grafico": 
    },
    {
        "ranking": 5, "nome": "ProDentim", "plataforma": "ClickBank", "tipo": "Saúde Bucal", "status": "🔥 ALTA", 
        "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", 
        "dor_principal": "Mau hálito crônico embaraçoso, cáries recorrentes e sangramentos sérios na gengiva.", 
        "porque": "Nicho com concorrência limpa e ótimos custos por clique na rede de pesquisa internacional.", 
        "concorrencia": "Média-Baixa", "cpc_medio": "$1.40 - $2.20", "funil": "Google Ads + Advertorial Clínico", 
        "avatar": "Pessoas de 40 a 70 anos sofrendo com cáries ou sensibilidade dentária severa.",
        "grafico": 
    },
    {
        "ranking": 6, "nome": "Liv Pure", "plataforma": "ClickBank", "tipo": "Detox Hepático", "status": "🔥 ALTA", 
        "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", 
        "dor_principal": "Fígado sobrecarregado por toxinas alimentares que paralisam o funcionamento do metabolismo.", 
        "porque": "Funil do produtor altamente otimizado com ofertas de upsell que disparam o valor da comissão.", 
        "concorrencia": "Alta", "cpc_medio": "$2.50 - $3.80", "funil": "YouTube Ads / Tráfego de Review", 
        "avatar": "Adultos acima do peso (40-65 anos) com cansaço crônico e dificuldades metabólicas.",
        "grafico": 
    },
    {
        "ranking": 7, "nome": "Ikaria Lean Belly", "plataforma": "ClickBank", "tipo": "Suplemento Pó", "status": "🔥 ALTA", 
        "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", 
        "dor_principal": "Altas concentrações de ácido úrico que inflamam o organismo e geram acúmulo de gordura abdominal.", 
        "porque": "Formato inovador em pó que gera alta curiosidade, cliques rápidos e conversão acelerada.", 
        "concorrencia": "Média-Alta", "cpc_medio": "$2.10 - $3.20", "funil": "Bing Ads + Pre-Sell Blindada", 
        "avatar": "Homens e mulheres focados em desinflamar o corpo e reduzir medidas na região da barriga.",
        "grafico": 
    },
    {
        "ranking": 8, "nome": "Cortexi", "plataforma": "ClickBank", "tipo": "Audição", "status": "🔥 ALTA", 
        "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)", 
        "dor_principal": "Zumbido estridente permanente no ouvido (Tinnitus) que tira o sono e destrói o foco mental.", 
        "porque": "Nicho focado em uma dor extrema, onde o cliente compra de forma imediata e prefere pacotes grandes.", 
        "concorrencia": "Média", "cpc_medio": "$1.70 - $2.50", "funil": "Google Ads (Fundo de Funil)", 
        "avatar": "Idosos e profissionais expostos a ruídos (45+ anos) desesperados para silenciar o zumbido auditivo.",
        "grafico": 
    },
    {
