import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO NEON PREMIUM COM ANIMAÇÃO DE PULSAR E BRILHO HOVER (ANTI-TRAVAMENTO)
st.markdown("""
<style>
.stApp { background-color: #060913; color: #f8fafc; }
h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }

.titulo-cyber {
    font-size: 2.6rem;
    font-weight: 900;
    color: #00ffcc;
    text-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
    letter-spacing: 1px;
}

div[data-testid="stHorizontalBlock"] { gap: 14px !important; }

/* Configuração Base dos Botões de Luxo */
div[data-testid="stColumn"] button {
    background: #0f1526 !important;
    border-radius: 12px !important;
    padding: 14px 10px !important;
    min-height: 56px !important;
    width: 100% !important;
    display: block !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border: 2px solid #1e293b !important;
}
div[data-testid="stColumn"] button p {
    font-size: 15px !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px;
}

/* 🔴 NEON VERMELHO (MÉTRICAS EM ALTA - TENDÊNCIA ANIMAL) */
@keyframes pulseVermelho {
    0% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
    50% { border-color: #ff4d88; box-shadow: 0 0 18px #ff0055; }
    100% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
}
.btn-alta button {
    border: 2px solid #ff0055 !important;
    animation: pulseVermelho 2s infinite !important;
}
.btn-alta button p { color: #ff4d88 !important; }
.btn-alta button:hover {
    background: #ff0055 !important;
    box-shadow: 0 0 30px #ff0055, inset 0 0 10px rgba(255,255,255,0.4) !important;
    transform: translateY(-2px) scale(1.02);
}
.btn-alta button:hover p { color: #ffffff !important; text-shadow: 0 0 8px #ffffff !important; }

/* 🟢 NEON VERDE (VALIDADOS - BAIXA CONCORRÊNCIA SUBINDO) */
@keyframes pulseVerde {
    0% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
    50% { border-color: #33ffdd; box-shadow: 0 0 18px #00ffcc; }
    100% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
}
.btn-validado button {
    border: 2px solid #00ffcc !important;
    animation: pulseVerde 2.5s infinite !important;
}
.btn-validado button p { color: #33ffdd !important; }
.btn-validado button:hover {
    background: #00ffcc !important;
    box-shadow: 0 0 30px #00ffcc, inset 0 0 10px rgba(255,255,255,0.4) !important;
    transform: translateY(-2px) scale(1.02);
}
.btn-validado button:hover p { color: #060913 !important; font-weight: 900 !important; }

/* 🔵 NEON ROXO (INFORMAÇÕES) */
.btn-info button { border: 2px solid #9900ff !important; }
.btn-info button p { color: #cc66ff !important; }
.btn-info button:hover { background: #9900ff !important; box-shadow: 0 0 20px #9900ff !important; }
.btn-info button:hover p { color: #ffffff !important; }

/* Badges e Cards Centrais */
.badge-alta-cyber { background-color: #2a0813; color: #ff4d88 !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #ff0055; display: inline-block; box-shadow: 0 0 15px rgba(255, 0, 85, 0.4); }
.badge-normal-cyber { background-color: #04251d; color: #33ffdd !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #00ffcc; display: inline-block; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3); }
.card-cyber-info { background: linear-gradient(135deg, #0f1526, #141c33); border: 2px solid #1e293b; padding: 24px; border-radius: 16px; margin-top: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6); }
.sub-tag-neon { color: #00ffcc !important; font-weight: bold; font-size: 15px; display: block; margin-top: 14px; text-shadow: 0 0 8px rgba(0,255,204,0.3); }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema premium com inteligência competitiva de mercado gringo e monitoramento de tendências.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE DADOS ESTRUTURADA DOS 20 PRODUTOS (SINTAXE SIMPLIFICADA SEM LISTAS EM EMBUTIDOS)
PRODUTOS_LISTA = [
    {"ranking": 1, "nome": "Alpilean", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 SUBINDO SEVERO"},
    {"ranking": 2, "nome": "Puravive", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 TRAÇÃO FORTE"},
    {"ranking": 3, "nome": "Java Burn", "status": "🔥 ALTA", "plataforma": "BuyGoods", "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "seta": "📈 EXPLODINDO"},
    {"ranking": 4, "nome": "GlucoTrust", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", "seta": "📉 ESTÁVEL NO TOPO"},
    {"ranking": 5, "nome": "ProDentim", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", "seta": "📈 SUBINDO"},
    {"ranking": 6, "nome": "Liv Pure", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 TRAÇÃO EXTREMA"},
    {"ranking": 7, "nome": "Ikaria Juice", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", "seta": "📉 RECORDE ATUAL"},
    {"ranking": 8, "nome": "Cortexi", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)", "seta": "📈 ACELERAÇÃO VENDAS"},
    {"ranking": 9, "nome": "FlowForce Max", "status": "🔥 ALTA", "plataforma": "BuyGoods", "buscas_mes": 54000, "buscas_hoje": 1050, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 SUBINDO"},
    {"ranking": 10, "nome": "Metanail Serum", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 51000, "buscas_hoje": 980, "melhor_pais": "Canadá (CA)", "seta": "📉 CONSOLIDADO"},
    {"ranking": 11, "nome": "LeanBliss", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 14500, "buscas_hoje": 320, "melhor_pais": "Austrália (AU)", "seta": "📈 ESCALANDO LIVRE"},
    {"ranking": 12, "nome": "Neotonics", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 13200, "buscas_hoje": 290, "melhor_pais": "Alemanha (DE)", "seta": "📈 SURGINDO AGORA"},
    {"ranking": 13, "nome": "Synogut", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 12400, "buscas_hoje": 260, "melhor_pais": "Estados Unidos (USA)", "seta": "📉 SEM CONCORRENTES"},
    {"ranking": 14, "nome": "Kerassentials", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 11800, "buscas_hoje": 240, "melhor_pais": "Reino Unido (UK)", "seta": "📈 OPORTUNIDADE"},
    {"ranking": 15, "nome": "SightCare", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 10500, "buscas_hoje": 210, "melhor_pais": "Canadá (CA)", "seta": "📈 ENTRANDO EM ALTA"},
    {"ranking": 16, "nome": "Prostadine", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 9800, "buscas_hoje": 190, "melhor_pais": "Austrália (AU)", "seta": "📉 LEILÃO BARATO"},
    {"ranking": 17, "nome": "Fast Lean Pro", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 8900, "buscas_hoje": 170, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 CRESCIMENTO REAL"},
    {"ranking": 18, "nome": "Amiclear", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 8200, "buscas_hoje": 150, "melhor_pais": "Reino Unido (UK)", "seta": "📈 TRAÇÃO DO DIA"},
    {"ranking": 19, "nome": "Alpha Tonic", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 7800, "buscas_hoje": 130, "melhor_pais": "Nova Zelândia", "seta": "📈 DESCOBERTA NOVO"},
    {"ranking": 20, "nome": "Joint Genesis", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 7100, "buscas_hoje": 110, "melhor_pais": "Estados Unidos (USA)", "seta": "📉 RETORNO SEGURO"}
]

# 4. ENGINE DE AUDITORIA COMPLETA (Gera textos convincentes de 5 linhas de forma isolada)
def carregar_auditoria_convincente(nome):
    if "Alpilean" in nome:
        dor = "Metabolismo gravemente paralisado e em estado latente induzido pela baixa temperatura das células e tecidos internos, gerando um bloqueio biológico severo que impede a queima de gorduras mesmo sob restrição calórica extrema ou rotinas exaustivas de treinos cardiorrespiratórios diários."
        justificativa = "O veredicto operacional confirma que este suplemento lidera as intenções de busca internacional fundo de funil por termos de marca exatos. Anunciar no tráfego dos Estados Unidos é a decisão perfeita porque o volume de cliques convertidos nas últimas 24 horas garante vendas com retorno em dólar escalável e comissão acumulada direto na conta."
        cpc = "USA: $2.80 | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40"
    elif "Puravive" in nome:
        dor = "Inabilidade sistêmica do organismo em ativar as taxas corretas do tecido adiposo marrom (BAT), resultando no acúmulo denso e ininterrupto de gorduras brancas perigosas nas camadas profundas do abdômen, que resistem fortemente a métodos tradicionais de emagrecimento."
        justificativa = "Esta oferta apresenta os maiores níveis de satisfação e a menor taxa de reembolso de todo o mercado gringo atual. O público americano responde massivamente a copys que integram comprovações científicas e exames clínicos, tornando a sua estrutura própria de Pre-Sell um verdadeiro ímã de conversões com alto lucro por clique."
        cpc = "USA: $3.10 | UK: $2.20 | CA: $2.40 | AU: $2.50 | DE: $1.60"
    elif "Java Burn" in nome:
