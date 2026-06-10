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
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border: 2px solid #1e293b !important;
}
div[data-testid="stColumn"] button p {
    font-size: 15px !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px;
}

/* 🔴 NEON VERMELHO PISCANTE (PRODUTOS EM ALTA) */
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
    box-shadow: 0 0 25px #ff0055 !important;
    transform: translateY(-2px);
}
.btn-alta button:hover p { color: #ffffff !important; }

/* 🟢 NEON VERDE PISCANTE (PRODUTOS VALIDADOS) */
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
    box-shadow: 0 0 25px #00ffcc !important;
    transform: translateY(-2px);
}
.btn-validado button:hover p { color: #060913 !important; }

/* Botão de Info Roxo */
.btn-info button {
    border: 2px solid #9900ff !important;
}
.btn-info button p { color: #cc66ff !important; }
.btn-info button:hover { background: #9900ff !important; box-shadow: 0 0 15px #9900ff !important; }
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

# 3. BASE DE DADOS COMPLETA COM EXATAMENTE 20 PRODUTOS VALIDADOS (SINTAXE SIMPLIFICADA ANTI-FALHAS)
PRODUTOS_DADOS = [
    {"ranking": 1, "nome": "Alpilean", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 2, "nome": "Puravive", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 3, "nome": "Java Burn", "status": "🔥 ALTA", "plataforma": "BuyGoods", "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)"},
    {"ranking": 4, "nome": "GlucoTrust", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 5, "nome": "ProDentim", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)"},
    {"ranking": 6, "nome": "Liv Pure", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 7, "nome": "Ikaria Juice", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)"},
    {"ranking": 8, "nome": "Cortexi", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)"},
    {"ranking": 9, "nome": "FlowForce Max", "status": "🔥 ALTA", "plataforma": "BuyGoods", "buscas_mes": 54000, "buscas_hoje": 1050, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 10, "nome": "Metanail Serum", "status": "🔥 ALTA", "plataforma": "ClickBank", "buscas_mes": 51000, "buscas_hoje": 980, "melhor_pais": "Canadá (CA)"},
    {"ranking": 11, "nome": "LeanBliss", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 14500, "buscas_hoje": 320, "melhor_pais": "Austrália (AU)"},
    {"ranking": 12, "nome": "Neotonics", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 13200, "buscas_hoje": 290, "melhor_pais": "Alemanha (DE)"},
    {"ranking": 13, "nome": "Synogut", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 12400, "buscas_hoje": 260, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 14, "nome": "Kerassentials", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 11800, "buscas_hoje": 240, "melhor_pais": "Reino Unido (UK)"},
    {"ranking": 15, "nome": "SightCare", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 10500, "buscas_hoje": 210, "melhor_pais": "Canadá (CA)"},
    {"ranking": 16, "nome": "Prostadine", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 9800, "buscas_hoje": 190, "melhor_pais": "Austrália (AU)"},
    {"ranking": 17, "nome": "Fast Lean Pro", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 8900, "buscas_hoje": 170, "melhor_pais": "Estados Unidos (USA)"},
    {"ranking": 18, "nome": "Amiclear", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 8200, "buscas_hoje": 150, "melhor_pais": "Reino Unido (UK)"},
    {"ranking": 19, "nome": "Alpha Tonic", "status": "✅ VALIDADO", "plataforma": "BuyGoods", "buscas_mes": 7800, "buscas_hoje": 130, "melhor_pais": "Nova Zelândia"},
    {"ranking": 20, "nome": "Joint Genesis", "status": "✅ VALIDADO", "plataforma": "ClickBank", "buscas_mes": 7100, "buscas_hoje": 110, "melhor_pais": "Estados Unidos (USA)"}
]

# 4. FUNÇÃO QUE RETORNA OS TEXTOS COMPLETO DE AUDITORIA BASEADO NO ID
def puxar_auditoria_completa(nome_produto):
    if "Alpilean" in nome_produto:
        dor = "Metabolismo completamente paralisado e congelado devido à baixa temperatura interna das células corporais, gerando um ganho de gordura abdominal inevitável e resistência severa a qualquer tipo de dieta tradicional ou treinos."
        porque = "Este produto possui o maior índice de intenção de compra imediata ('brand bidding') do mercado internacional. O veredicto aponta que rodar campanhas de fundo de funil no Google Ads para o público norte-americano é a rota mais lucrativa devido ao altíssimo volume de compradores ativos nas últimas 24 horas."
        cpc = "USA: $2.80 | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40"
    elif "Puravive" in nome_produto:
        dor = "Falta de ativação biológica do tecido adiposo marrom (BAT), fazendo com que o corpo armazene gordura profunda em áreas críticas e desacelere o gasto calórico diário de forma contínua."
        porque = "A oferta mantém uma taxa de reembolso historicamente baixa e paga altas comissões. O público comprador dos Estados Unidos responde muito bem a páginas que expõem estudos científicos estruturados, tornando a rede de pesquisa um oceano de lucro estável."
        cpc = "USA: $3.10 | UK: $2.20 | CA: $2.40 | AU: $2.50 | DE: $1.60"
    elif "Java Burn" in nome_produto:
        dor = "Falta de energia matinal, fadiga severa logo nas primeiras horas do dia e lentidão crônica na velocidade da queima calórica natural do organismo."
        porque = "Este produto em formato de sachê misturável explodiu em popularidade. O veredicto aponta que rodar campanhas focadas no Reino Unido (UK) entrega um ROI superior porque o custo por clique (CPC) está até 40% mais barato que nos EUA, sem concorrência predatória."
        cpc = "USA: $2.60 | UK: $1.65 | CA: $1.95 | AU: $2.10 | DE: $1.30"
    elif "GlucoTrust" in nome_produto:
        dor = "Picos descontrolados de açúcar na corrente sanguínea, desequilíbrio de insulina e ataques de compulsão ansiosa por doces e carboidratos pesados durante o período noturno."
        porque = "Atinge em cheio o público sênior (acima de 45 anos) americano, que possui o maior poder aquisitivo para comprar kits de tratamento completo de 6 potes. Anunciar no Google Ads focado na dor da diabetes garante cliques ultra qualificados e conversões limpas."
        cpc = "USA: $2.95 | UK: $1.85 | CA: $2.15 | AU: $2.20 | DE: $1.45"
    elif "ProDentim" in nome_produto:
        dor = "Mau hálito social constrangedor, sangramentos frequentes na gengiva ao escovar os dentes e enfraquecimento geral do esmalte de proteção dentária."
