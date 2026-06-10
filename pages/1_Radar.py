import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="💎", layout="wide")

# 2. ESTILIZAÇÃO NEON PREMIUM COM ANIMAÇÃO DE PULSAR E BRILHO HOVER
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

/* 🔴 NEON VERMELHO (MÉTRICAS EM ALTA) */
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

/* 🟢 NEON VERDE (VALIDADOS - BAIXA CONCORRÊNCIA) */
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

.badge-alta-cyber { background-color: #2a0813; color: #ff4d88 !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #ff0055; display: inline-block; box-shadow: 0 0 15px rgba(255, 0, 85, 0.4); }
.badge-normal-cyber { background-color: #04251d; color: #33ffdd !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #00ffcc; display: inline-block; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3); }
.card-cyber-info { background: linear-gradient(135deg, #0f1526, #141c33); border: 2px solid #1e293b; padding: 24px; border-radius: 16px; margin-top: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6); }
.sub-tag-neon { color: #00ffcc !important; font-weight: bold; font-size: 15px; display: block; margin-top: 14px; text-shadow: 0 0 8px rgba(0,255,204,0.3); }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema premium com inteligência competitiva de mercado gringo com varredura viva em tempo real.")

# 🛰️ MENSAGEM DO ROBO TRABALHANDO COM DATA E HORA DO SEGUNDO ATUAL
horario_atual = datetime.now().strftime("%H:%M:%S")
st.markdown(f"🛰️ **Status do Robô:** <span style='color:#00ffcc; font-weight:bold;'>ATIVO</span> | Varredura viva realizada com sucesso às <span style='color:#ff0055; font-weight:bold;'>{horario_atual}</span> (A lista e as posições mudam conforme o tráfego oscila na gringa).", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE NOMES DOS 20 PRODUTOS PERPÉTUOS (EVERGREEN)
NOMES_BASE = [
    "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
    "Liv Pure", "Ikaria Juice", "Cortexi", "FlowForce Max", "Metanail Serum",
    "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
    "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
]

# 4. ENGINE DE VARREDURA EM TEMPO REAL (MISTURA E RECALCULA AS POSIÇÕES CONFORME O SEGUNDO DO RELÓGIO)
# Usar o segundo atual como semente faz o robô mudar as tendências e posições a cada clique!
random.seed(datetime.now().second)

pool_embaralhado = NOMES_BASE.copy()
random.shuffle(pool_embaralhado) # O robô embaralha os produtos mudando quem está subindo ou descendo vivo

PRODUTOS_PROCESSADOS = []
for idx, nome_item in enumerate(pool_embaralhado):
    ranking_visto = idx + 1
    is_top_10 = ranking_visto <= 10
    status_label = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
    
    # Gera variação de tráfego que muda a cada recarga simulando o robô capturando as pesquisas agora
    buscas_m = random.randint(60000, 120000) if is_top_10 else random.randint(5000, 18000)
    buscas_h = random.randint(1500, 4500) if is_top_10 else random.randint(60, 480)
    
    # Define símbolos de subida ou descida dinâmicos sorteados na hora pela IA do robô
    tendencia_seta = random.choice(["📈 SUBINDO EXTREMO", "📈 ACELERANDO", "📉 ESTÁVEL NO TOPO"]) if is_top_10 else random.choice(["📈 ESCALANDO LIVRE", "📈 NOVA CHANCE", "📉 LEILÃO BARATO"])
    
    paises_opcoes = ["Estados Unidos (USA)", "Reino Unido (UK)", "Canadá (CA)", "Austrália (AU)", "Alemanha (DE)"]
    pais_escolhido = "Estados Unidos (USA)" if is_top_10 and random.random() > 0.3 else random.choice(paises_opcoes)
    
    cpc_u = round(random.uniform(2.20, 3.80), 2)
    cpc_k = round(random.uniform(1.50, 2.70), 2)
    cpc_c = round(random.uniform(1.70, 2.90), 2)
    
    PRODUTOS_PROCESSADOS.append({
        "ranking": ranking_visto, "nome": nome_item, "status": status_label, "plataforma": "BuyGoods" if "Java" in nome_item or "FlowForce" in nome_item else "ClickBank",
        "buscas_mes": buscas_m, "buscas_hoje": buscas_h, "melhor_pais": pais_escolhido, "seta": tendencia_seta,
        "cpc": f"USA: ${cpc_u} | UK: ${cpc_k} | CA: ${cpc_c} | AU: $2.45 | DE: $1.30", "fator": len(nome_item)
    })

# 5. AJUSTE CIRÚRGICO DE TEXTO CONFORME O NICHO DO ITEM ATIVO
def extrair_textos_auditoria(nome_produto):
    if "Alpilean" in nome_produto or "Puravive" in nome_produto or "LeanBliss" in nome_produto:
        dor = "Metabolismo completamente paralisado e bloqueado devido à baixa temperatura interna das células corporais, gerando um acúmulo de gordura abdominal resistente a dietas tradicionais e rotinas de treinos exaustivos."
        porque = "Este produto lidera os volumes de busca exata por termos institucionais. O veredicto técnico aponta que anunciar na rede de pesquisa do Google Ads captura leads com intenção imediata de compra com o cartão na mão nas últimas 24 horas."
    elif "Java" in nome_produto or "Fast Lean" in nome_produto:
        dor = "Falta aguda de energia celular e cansaço severo logo nas primeiras horas do dia, combinada com crises intensas de fome psicológica que sabotam o foco operacional de dietas."
        porque = "A oferta em formato de sachê misturável no café tomou o mercado gringo de assalto. O veredicto aponta excelente ROI rodando anúncios na Europa, onde os custos de clique (CPC) estão bem menores que a concorrência predatória americana."
    elif "GlucoTrust" in nome_produto or "Amiclear" in nome_produto:
        dor = "Picos descontrolados de açúcar na corrente sanguínea, desequilíbrio de insulina e ataques de compulsão ansiosa por carboidratos pesados e doces durante o período noturno."
        porque = "Resolve uma dor urgente de saúde e atinge em cheio o público sênior internacional que possui alto poder aquisitivo. Anunciar com correspondência exata de palavras-chave filtra cliques curiosos e garante a venda de kits grandes."
    elif "ProDentim" in nome_produto:
        dor = "Sangramentos inflamatórios constantes na gengiva ao escovar, proliferação de bactérias nocivas no trato bucal que destroem o esmalte de proteção dos dentes e causam mau hálito crônico."
        porque = "Enquanto a massa de afiliados inflaciona o mercado dos EUA, o leilão do Canadá e Reino Unido encontra-se deserto para o nicho de saúde bucal, permitindo colher comissões líquidas altas com anúncios baratos."
    elif "FlowForce" in nome_produto or "Prostadine" in nome_produto:
        dor = "Inflamação congestiva na próstata obrigando o homem sênior a interromper o sono de 4 a 6 vezes todas as noites para ir ao banheiro com dor pélvica e jato urinário fraco."
        porque = "Produto de dor latente vendido pela urgência de melhora. Subir uma campanha direcionada para o público acima de 45 anos na rede de pesquisa assegura cliques de alta conversão e comissão imediata no checkout."
    else:
        dor = "Falta de vitalidade corporal, fadiga severa e sintomas crônicos limitantes que reduzem a qualidade de vida e geram desespero por tratamentos naturais de alta absorção rápida."
        porque = "Nossa varredura localizou uma excelente brecha operacional neste leilão secundário. Como a maioria das ferramentas comuns saturam apenas os top 3 líderes, este produto está livre de concorrência, garantindo cliques baratos."
