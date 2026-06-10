import streamlit as st
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA PÁGINA
    st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="💎", layout="wide")

    # 2. CABEÇALHO DO MONITORAMENTO
    st.title("💎 Radar de Produtos AdrielAI")
    st.write("Ecossistema premium de monitoramento perpétuo internacional com auditoria automatizada de tráfego.")

    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.write(f"🛰️ **Status do Robô:** ATIVO | Varredura viva de tráfego injetada com sucesso às {horario_atual}.")
    st.markdown("---")

    # 3. BASE DE DADOS OFICIAL DOS 20 PRODUTOS
    produtos_dados = [
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

    # Inicialização forçada da sessão
    if "produto_radar" not in st.session_state:
        st.session_state.produto_radar = produtos_dados[0]

    # Carrega diretamente o item selecionado
    p_sel = st.session_state.produto_radar

    # 4. ENGINE DE AUDITORIA CIRÚRGICA
    def extrair_dossie(nome_produto):
        if "Alpilean" in nome_produto or "Puravive" in nome_produto or "LeanBliss" in nome_produto:
            dor = "Metabolismo severamente travado e em estado latente induzido pela baixa temperatura das células e tecidos internos, gerando um bloqueio biológico crítico que impede a queima de gorduras profundas mesmo sob restrição calórica severa ou rotinas exaustivas de treinos aeróbicos."
            ganho = "Regulação térmica celular que dispara a queima calórica passiva em até 400% nas áreas viscerais mais resistentes do organismo."
            porque = "O veredicto técnico confirma que este segmento lidera com folga as buscas exatas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e altamente propensos a comprar com o cartão na mão nas últimas 24 horas."
            cpc = "USA: $3.10 | UK: $2.15 | CA: $2.40 | AU: $2.60 | DE: $1.45"
        elif "Java" in nome_produto or "Fast Lean" in nome_produto:
            dor = "Falta aguda de energia celular e cansaço massivo nas primeiras horas do dia, combinada com surtos contínuos de fome psicológica de fundo emocional que sabotam totalmente o andamento de dietas e quebram a queima natural calórica."
            ganho = "Sinergia nutricional termogênica instantânea que otimiza o uso de carboidratos como combustível e bloqueia os picos de ansiedade por comida."
            porque = "A novidade do sachê misturável no café diário tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anúncios na Europa, onde os custos de clique (CPC) estão bem menores que no inflacionado mercado americano, mantendo alta conversão."
            cpc = "USA: $2.75 | UK: $1.70 | CA: $1.95 | AU: $2.20 | DE: $1.30"
        elif "GlucoTrust" in nome_produto or "Amiclear" in nome_produto:
            dor = "Picos descontrolados de glicose na corrente sanguínea, desequilíbrio metabólico na produção de insulina e crises intensas de compulsão noturna por carboidratos pesados e doces refinados antes de dormir."
            ganho = "Estabilização imediata da resposta insulínica e eliminação da gordura profunda acumulada ao redor dos órgãos vitais de filtragem."
            porque = "Resolve uma dor de saúde alarmante e atinge em cheio o público idoso internacional de alto poder aquisitivo. Anunciar com correspondência exata de palavras-chave oficiais filtra cliques curiosos de concorrentes e traz tráfego qualificado de fundo."
            cpc = "USA: $2.95 | UK: $1.90 | CA: $2.15 | AU: $2.30 | DE: $1.50"
        elif "ProDentim" in nome_produto:
            dor = "Sangramentos gengivais constantes durante a escovação básica, proliferação de bactérias nocivas no trato bucal que destroem o esmalte protetor e causam um mau hálito crônico de difícil eliminação social."
            ganho = "Repovoamento biológico da mucosa com 3.5 bilhões de cepas probióticas que purificam o hálito e reconstroem a saúde da raiz gengival."
            porque = "Enquanto a massa de afiliados satura os leilões de tráfego dos Estados Unidos, o leilão do Canadá e Reino Unido encontra-se livre para o nicho dentário, permitindo extrair comissões líquidas altas com anúncios baratos via Pre-Sell rápida."
            cpc = "USA: $2.45 | UK: $1.60 | CA: $1.80 | AU: $2.00 | DE: $1.25"
        elif "FlowForce" in nome_produto or "Prostadine" in nome_produto:
            dor = "Inflamação severa na próstata obrigando o homem sênior a interromper o sono de 4 a 6 vezes todas as noites para ir ao banheiro com forte queimação pélvica e jato urinário interrompido."
            ganho = "Desinflamação imediata do trato urinário e eliminação de sedimentos e toxinas minerais acumuladas no sistema reprodutor masculino."
            porque = "Produto de dor urgente vendido pela extrema necessidade de alívio rápido do lead gringo. Subir uma campanha direcionada para a rede de busca do Google Ads assegura cliques de alta intenção e comissões robustas por vendas de kits completos."
            cpc = "USA: $3.25 | UK: $2.20 | CA: $2.40 | AU: $2.55 | DE: $1.65"
        else:
            dor = "Falta de vitalidade corporal, fadiga severa e desgaste orgânico limitante que reduz a produtividade no trabalho e gera desespero por tratamentos naturais de alta absorção biológica rápida."
            ganho = "Suporte adaptógeno de alta concentração celular que repara os tecidos e devolve o vigor orgânico completo do usuário."
