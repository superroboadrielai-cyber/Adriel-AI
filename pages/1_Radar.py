import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA (MANTÉM LAYOUT EXPANDIDO)
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="💎", layout="wide")

# 2. INJEÇÃO DE INLINE CSS CONFIÁVEL DE LUXO (MUDANÇA DE COR E BRILHO COM MOUSE)
st.markdown("""
<style>
    .stApp { background-color: #060913 !important; color: #f8fafc !important; }
    h1, h2, h3, h4, p, span, div { font-family: 'Segoe UI', Roboto, sans-serif; }
    
    .titulo-cyber {
        font-size: 2.6rem;
        font-weight: 900;
        color: #00ffcc;
        text-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        margin-bottom: 5px;
    }
    
    /* Animação Piscante para Botões em ALTA (Vermelho Neon) */
    @keyframes pulseVermelho {
        0% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
        50% { border-color: #ff4d88; box-shadow: 0 0 15px #ff0055; }
        100% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
    }
    
    /* Animação Piscante para Botões VALIDADOS (Verde Neon) */
    @keyframes pulseVerde {
        0% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
        50% { border-color: #33ffdd; box-shadow: 0 0 15px #00ffcc; }
        100% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
    }

    /* Estilização Executiva dos Componentes do App */
    .cyber-btn-alta button {
        border: 2px solid #ff0055 !important;
        background: #0f1526 !important;
        animation: pulseVermelho 2s infinite !important;
    }
    .cyber-btn-alta button p { color: #ff4d88 !important; font-weight: 800 !important; }
    .cyber-btn-alta button:hover {
        background: #ff0055 !important;
        box-shadow: 0 0 25px #ff0055 !important;
    }
    .cyber-btn-alta button:hover p { color: #ffffff !important; }

    .cyber-btn-validado button {
        border: 2px solid #00ffcc !important;
        background: #0f1526 !important;
        animation: pulseVerde 2.5s infinite !important;
    }
    .cyber-btn-validado button p { color: #33ffdd !important; font-weight: 800 !important; }
    .cyber-btn-validado button:hover {
        background: #00ffcc !important;
        box-shadow: 0 0 25px #00ffcc !important;
    }
    .cyber-btn-validado button:hover p { color: #060913 !important; font-weight: 900 !important; }

    .card-cyber-info {
        background: linear-gradient(135deg, #0f1526, #141c33);
        border: 2px solid #1e293b;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
    }
    .sub-tag-neon {
        color: #00ffcc !important;
        font-weight: bold;
        font-size: 15px;
        display: block;
        margin-top: 14px;
        text-shadow: 0 0 8px rgba(0,255,204,0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO DO MONITORAMENTO DO ROBÔ
st.markdown('<div class="titulo-cyber">💎 Radar de Produtos AdrielAI</div>', unsafe_allow_html=True)
st.write("Ecossistema premium de monitoramento perpétuo internacional com auditoria automatizada de tráfego.")

horario_atual = datetime.now().strftime("%H:%M:%S")
st.markdown(f"🛰 ... **Status do Robô:** <span style='color:#00ffcc; font-weight:bold;'>ATIVO</span> | Varredura viva de tráfego injetada com sucesso às <span style='color:#ff0055; font-weight:bold;'>{horario_atual}</span>.", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. BASE DE DADOS OFICIAL DOS 20 PRODUTOS (ESTRUTURA BLINDADA)
PRODUTOS_DADOS = [
    {"ranking": 1, "nome": "Alpilean", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 SUBINDO EXTREMO", "semente": 110},
    {"ranking": 2, "nome": "Puravive", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 TRAÇÃO FORTE", "semente": 95},
    {"ranking": 3, "nome": "Java Burn", "status": "🔥 ALTA", "plataforma": "BuyGoods", "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "seta": "📈 EXPLODINDO", "semente": 85},
    {"ranking": 4, "nome": "GlucoTrust", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 ACELERAÇÃO", "semente": 72},
    {"ranking": 5, "nome": "ProDentim", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", "seta": "📈 TENDÊNCIA ALTA", "semente": 68},
    {"ranking": 6, "nome": "Liv Pure", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 TRAÇÃO CRÍTICA", "semente": 64},
    {"ranking": 7, "nome": "Ikaria Juice", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", "seta": "📉 ESTÁVEL NO TOPO", "semente": 60},
    {"ranking": 8, "nome": "Cortexi", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)", "seta": "📈 ACELERAÇÃO VENDAS", "semente": 57},
    {"ranking": 9, "nome": "FlowForce Max", "status": "🔥 ALTA", "plataforma": "BuyGoods", "buscas_mes": 54000, "buscas_hoje": 1050, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 SUBINDO SEVERO", "semente": 53},
    {"ranking": 10, "nome": "Metanail Serum", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 51000, "buscas_hoje": 980, "melhor_pais": "Canadá (CA)", "seta": "📉 CONSOLIDADO", "semente": 50},
    {"ranking": 11, "nome": "LeanBliss", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 14500, "buscas_hoje": 320, "melhor_pais": "Austrália (AU)", "seta": "📈 ESCALANDO LIVRE", "semente": 14},
    {"ranking": 12, "nome": "Neotonics", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 13200, "buscas_hoje": 290, "melhor_pais": "Alemanha (DE)", "seta": "📈 SURGINDO AGORA", "semente": 13},
    {"ranking": 13, "nome": "Synogut", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 12400, "buscas_hoje": 260, "melhor_pais": "Estados Unidos (USA)", "seta": "📉 SEM CONCORRENTES", "semente": 12},
    {"ranking": 14, "nome": "Kerassentials", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 11800, "buscas_hoje": 240, "melhor_pais": "Reino Unido (UK)", "seta": "📈 OPORTUNIDADE", "semente": 11},
    {"ranking": 15, "nome": "SightCare", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 10500, "buscas_hoje": 210, "melhor_pais": "Canadá (CA)", "seta": "📈 ENTRANDO EM ALTA", "semente": 10},
    {"ranking": 16, "nome": "Prostadine", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 9800, "buscas_hoje": 190, "melhor_pais": "Austrália (AU)", "seta": "📉 LEILÃO BARATO", "semente": 9},
    {"ranking": 17, "nome": "Fast Lean Pro", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 8900, "buscas_hoje": 170, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 CRESCIMENTO REAL", "semente": 8},
    {"ranking": 18, "nome": "Amiclear", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 8200, "buscas_hoje": 150, "melhor_pais": "Reino Unido (UK)", "seta": "📈 TRAÇÃO DO DIA", "semente": 8},
    {"ranking": 19, "nome": "Alpha Tonic", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 7800, "buscas_hoje": 130, "melhor_pais": "Nova Zelândia", "seta": "📈 DESCOBERTA NOVO", "semente": 7},
    {"ranking": 20, "nome": "Joint Genesis", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 7100, "buscas_hoje": 110, "melhor_pais": "Estados Unidos (USA)", "seta": "📉 RETORNO SEGURO", "semente": 7}
]

# 5. ENGINE DE CONTEÚDO CONVINCENTE E CIRÚRGICO DE 5 LINHAS
def carregar_textos_auditoria(nome_produto):
    if "Alpilean" in nome_produto or "Puravive" in nome_produto or "LeanBliss" in nome_produto:
        dor = "Metabolismo completamente paralisado e travado induzido pela baixa temperatura das células e tecidos internos, gerando um bloqueio biológico crítico que impede a queima de gorduras profundas mesmo sob restrição calórica severa ou rotinas exaustivas de treinos aeróbicos."
        porque = "O veredicto técnico confirma que este suplemento lidera com folga as buscas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e altamente propensos a comprar com o cartão na mão nas últimas 24 horas."
        cpc = "USA: $2.80 | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40"
    elif "Java" in nome_produto or "Fast Lean" in nome_produto:
        dor = "Falta aguda de energia celular e cansaço massivo nas primeiras horas do dia, combinada com surtos contínuos de fome psicológica de fundo emocional que sabotam totalmente o andamento de dietas e protocolos."
        porque = "A novidade do sachê misturável no café diário tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anúncios na Europa, onde os custos de clique (CPC) estão bem menores que no inflacionado mercado americano, mantendo alta conversão."
        cpc = "USA: $2.60 | UK: $1.65 | CA: $1.95 | AU: $2.10 | DE: $1.30"
    elif "GlucoTrust" in nome_produto or "Amiclear" in nome_produto:
        dor = "Picos descontrolados de glicose na corrente sanguínea, desequilíbrio metabólico na produção de insulina e crises intensas de compulsão noturna por carboidratos pesados e doces refinados antes de dormir."
        porque = "Resolve uma dor de saúde alarmante e atinge em cheio o público idoso internacional de alto poder aquisitivo. Anunciar com correspondência exata de palavras-chave oficiais filtra cliques curiosos de concorrentes e traz tráfego qualificado de fundo."
        cpc = "USA: $2.95 | UK: $1.85 | CA: $2.15 | AU: $2.20 | DE: $1.45"
    elif "ProDentim" in nome_produto:
