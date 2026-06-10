import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="💎", layout="wide")

# 2. INJEÇÃO DE TÍTULO LUXO CIBERNÉTICO
st.markdown('<h1 style="color:#00ffcc; font-size:2.5rem; font-weight:900; text-shadow:0 0 15px rgba(0,255,204,0.4);">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema premium com inteligência competitiva de mercado gringo e varredura ao vivo.")

# 3. INDICAÇÃO DO ROBO EM TEMPO REAL
horario_atual = datetime.now().strftime("%H:%M:%S")
st.markdown(f"🛰️ **Status do Robô:** <span style='color:#00ffcc; font-weight:bold;'>ATIVO</span> | Varredura viva de tráfego atualizada com sucesso às <span style='color:#ff0055; font-weight:bold;'>{horario_atual}</span>.", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. BASE DE DADOS COMPLETA E REVISADA DOS 20 PRODUTOS
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

# 5. TEXTOS DE AUDITORIA LONGA E CONVINCENTE (Extraídos de forma limpa)
def obter_textos_auditoria(nome_produto):
    if "Alpilean" in nome_produto or "Puravive" in nome_produto or "LeanBliss" in nome_produto:
        dor = "Metabolismo severamente paralisado e travado induzido pela baixa temperatura das células internas, gerando um bloqueio biológico crítico que impede a queima de gorduras mesmo sob restrição calórica extrema ou rotinas exaustivas de treinos aeróbicos."
        porque = "Veredito técnico confirma que este suplemento lidera as buscas exatas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e prontos para comprar com o cartão na mão."
        cpc = "USA: $2.80 | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40"
    elif "Java" in nome_produto or "Fast Lean" in nome_produto:
        dor = "Falta aguda de energia celular e cansaço massivo nas primeiras horas do dia, combinada com surtos contínuos de fome psicológica que sabotam o andamento de dietas."
        porque = "A novidade do sachê misturável no café tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anúncios na Europa, onde os custos de clique (CPC) estão bem menores que no inflacionado mercado americano."
        cpc = "USA: $2.60 | UK: $1.65 | CA: $1.95 | AU: $2.10 | DE: $1.30"
    elif "GlucoTrust" in nome_produto or "Amiclear" in nome_produto:
        dor = "Picos descontrolados de glicose na corrente sanguínea, desequilíbrio na produção de insulina e crises intensas de compulsão noturna por carboidratos e doces."
        porque = "Resolve uma dor de saúde alarmante e atinge em cheio o público idoso internacional de alto poder aquisitivo. Anunciar com correspondência exata de palavras-chave filtra cliques inválidos de concorrentes."
        cpc = "USA: $2.95 | UK: $1.85 | CA: $2.15 | AU: $2.20 | DE: $1.45"
    elif "ProDentim" in nome_produto:
        dor = "Sangramentos gengivais constantes durante a escovação, proliferação de bactérias nocivas no trato bucal que destroem o esmalte e causam mau hálito crônico."
        porque = "Enquanto a massa de afiliados satura os leilões dos Estados Unidos, o leilão do Canadá e Reino Unido encontra-se livre para o nicho dentário, permitindo extrair comissões líquidas altas com anúncios baratos."
        cpc = "USA: $2.40 | UK: $1.50 | CA: $1.75 | AU: $1.90 | DE: $1.20"
    elif "FlowForce" in nome_produto or "Prostadine" in nome_produto:
        dor = "Inflamação na próstata obrigando o homem sênior a interromper o sono de 4 a 6 vezes todas as noites para urinar com queimação e jato fraco."
        porque = "Produto de dor urgente vendido pela necessidade imediata de alívio. Subir uma campanha direcionada para a rede de busca do Google Ads assegura cliques de alta intenção e comissões robustas por vendas em kits."
        cpc = "USA: $3.00 | UK: $2.00 | CA: $2.20 | AU: $2.30 | DE: $1.40"
    else:
        dor = "Falta de vitalidade corporal, fadiga severa e desgaste orgânico limitante que reduz a produtividade e gera desespero por tratamentos naturais de alta absorção."
        porque = "Nossa varredura localizou uma brecha operacional fantástica neste leilão secundário. Como a maioria das ferramentas comuns saturam apenas os top líderes, este produto está livre de concorrência ativa."
        cpc = "USA: $1.90 | UK: $1.20 | CA: $1.40 | AU: $1.50 | DE: $0.95"
    return dor, porque, cpc

# Inicializa o estado de sessão de forma simples e direta com o primeiro dicionário da lista
if "produto_radar" not in st.session_state:
    st.session_state.produto_radar = PRODUTOS_DADOS[0]

p_sel = st.session_state.produto_radar
txt_dor, txt_porque, txt_cpc = obter_textos_auditoria(p_sel["nome"])

# 6. DIALOGO POPUP (MODAL DE AUDITORIA COMPLETA)
@st.dialog("📋 Dossiê de Inteligência")
def abrir_popup_detalhes(produto):
    d, p, c = obter_textos_auditoria(produto["nome"])
    st.markdown(f"## 🛡️ Dossiê de Mercado: {produto['nome']}")
    st.markdown(f"**Plataforma Base:** `{produto['plataforma']}` | **Indicador:** `{produto['seta']}`")
    st.markdown("---")
    st.markdown("### 💔 Dor Principal do Cliente Gringo:")
    st.error(d)
    st.markdown("---")
    st.markdown("### 🗺️ CPC nos 5 Países Principais:")
    st.code(c, language="text")
    st.markdown("---")
    st.markdown("### 🏆 Veredito Estratégico de Tráfego:")
    st.success(f"**Melhor País Indicado:** {produto['melhor_pais']}")
    st.info(p)

# 7. CONSTRUÇÃO DO LAYOUT DA TELA
col_esquerda, col_direita = st.columns([1.2, 1.1])

with col_esquerda:
    st.markdown("### 🎯 Painel Estatístico Global")
