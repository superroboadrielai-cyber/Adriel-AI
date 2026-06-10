import streamlit as st
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO HIGH-END DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    # 2. INJEÇÃO VISUAL CYBER-NEON EM LINHA (FORMATO ANTI-MAGIC ULTRA PURIFICADO)
    st.markdown('<style>.stApp {background-color: #040814 !important; color: #f3f4f6 !important;} h1,h2,h3,h4 {color: #00ffcc !important; text-shadow: 0 0 12px rgba(0,255,204,0.3);}</style>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 12px rgba(0, 255, 204, 0.3); margin-bottom: 5px;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"🛰️ **Status do Ecossistema:** <span style='color:#00ffcc; font-weight:bold;'>ATIVO</span> | Varredura viva de leilão estabilizada às <span style='color:#ff0055; font-weight:bold;'>{horario_atual}</span>.", unsafe_allow_html=True)
    st.markdown("---")

    # 3. BASE DE DADOS COMPLETA DOS 20 PRODUTOS OBLIGATÓRIOS (REVISADA E BLINDADA)
    produtos_dados = [
        {"ranking": 1, "nome": "Alpilean", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 SUBINDO EXTREMO", "semente": 110,
         "dor": "Metabolismo severamente travado e em estado latente induzido pela baixa temperatura das células e tecidos internos, gerando um bloqueio biológico crítico que impede a queima de gorduras profundas mesmo sob restrição calórica severa ou rotinas exaustivas de treinos aeróbicos.",
         "ganho": "Regulação térmica celular que dispara a queima calórica passiva em até 400% nas áreas viscerais mais resistentes do organismo.",
         "porque": "O veredicto técnico confirma que este suplemento lidera com folga as buscas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e altamente propensos a comprar com o cartão na mão nas últimas 24 horas.",
         "cpc": "USA: $3.10 | UK: $2.15 | CA: $2.40 | AU: $2.60 | DE: $1.45"},
        
        {"ranking": 2, "nome": "Puravive", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 TRAÇÃO FORTE", "semente": 95,
         "dor": "Falta de ativação biológica do tecido adiposo marrom (BAT), fazendo com que o corpo armazene gordura profunda em áreas críticas e desacelere o gasto calórico diário de forma contínua.",
         "ganho": "Otimização das gorduras marrons para derretimento acelerado de tecido adiposo estocado há anos.",
         "porque": "A oferta mantém uma taxa de reembolso historicamente baixa e paga altas comissões. O público comprador dos Estados Unidos responde muito bem a páginas que expõem estudos científicos estruturados, tornando a rede de pesquisa um oceano de lucro estável.",
         "cpc": "USA: $3.10 | UK: $2.20 | CA: $2.40 | AU: $2.50 | DE: $1.60"},
        
        {"ranking": 3, "nome": "Java Burn", "status": "🔥 TOP COMPRA", "plataforma": "BuyGoods", "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "seta": "📈 EXPLODINDO", "semente": 85,
         "dor": "Falta aguda de energia celular e cansaço massivo nas primeiras horas do dia, combinada com surtos contínuos de fome psicológica de fundo emocional que sabotam totalmente o andamento de dietas e protocolos.",
         "ganho": "Sinergia nutricional termogênica instantânea que otimiza o uso de carboidratos como combustível e bloqueia os picos de ansiedade por comida.",
         "porque": "A novidade do sachê misturável no café diário tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anúncios na Europa, onde os custos de clique (CPC) estão bem menores que no inflacionado mercado americano, mantendo alta conversão.",
         "cpc": "USA: $2.75 | UK: $1.70 | CA: $1.95 | AU: $2.20 | DE: $1.30"},
        
        {"ranking": 4, "nome": "GlucoTrust", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 ACELERAÇÃO", "semente": 72,
         "dor": "Picos descontrolados de glicose na corrente sanguínea, desequilíbrio metabólico na produção de insulina e crises intensas de compulsão noturna por carboidratos pesados e doces refinados antes de dormir.",
         "ganho": "Estabilização imediata da resposta insulínica e eliminação da gordura profunda acumulada ao redor dos órgãos vitais de filtragem.",
         "porque": "Resolve uma dor de saúde alarmante e atinge em cheio o público idoso internacional de alto poder aquisitivo. Anunciar com correspondência exata de palavras-chave oficiais filtra cliques curiosos de concorrentes e traz tráfego qualificado de fundo.",
         "cpc": "USA: $2.95 | UK: $1.90 | CA: $2.15 | AU: $2.30 | DE: $1.50"},
        
        {"ranking": 5, "nome": "ProDentim", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)", "seta": "📈 TENDÊNCIA ALTA", "semente": 68,
         "dor": "Sangramentos gengivais constantes durante a escovação básica, proliferação de bactérias nocivas no trato bucal que destroem o esmalte protetor e causam um mau hálito crônico de difícil eliminação social.",
         "ganho": "Repovoamento biológico da mucosa com 3.5 bilhões de cepas probióticas que purificam o hálito e reconstroem a saúde da raiz gengival.",
         "porque": "Enquanto a massa de afiliados satura os leilões de tráfego dos Estados Unidos, o leilão do Canadá e Reino Unido encontra-se livre para o nicho dentário, permitindo extrair comissões líquidas altas com anúncios baratos via Pre-Sell rápida.",
         "cpc": "USA: $2.45 | UK: $1.60 | CA: $1.80 | AU: $2.00 | DE: $1.25"},
        
        {"ranking": 6, "nome": "Liv Pure", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 65000, "buscas_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 TRAÇÃO CRÍTICA", "semente": 64,
         "dor": "Fígado completamente sobrecarregado por toxinas e gordura acumulada, paralisando o funcionamento natural do metabolismo hepático e impedindo a correta eliminação de lipídios acumulados.",
         "ganho": "Purificação interna profunda das células hepáticas para restaurar o poder natural de eliminação de gorduras.",
         "porque": "O produtor do Liv Pure estruturou um dos melhores funis de vendas de Upsell do mercado gringo. O veredicto cirúrgico indica que mesmo pagando um CPC mais caro nos EUA, o Valor de Vida do Cliente (LTV) compensa aggressively, gerando múltiplos potes por checkout.",
         "cpc": "USA: $3.25 | UK: $2.20 | CA: $2.40 | AU: $2.55 | DE: $1.65"},
        
        {"ranking": 7, "nome": "Ikaria Juice", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 61000, "buscas_hoje": 1310, "melhor_pais": "Austrália (AU)", "seta": "📉 ESTÁVEL NO TOPO", "semente": 60,
         "dor": "Acúmulo nocivo de ácido úrico no organismo que deflagra processos inflamatórios severos nas articulações corporais, cansaço muscular contínuo e retenção acelerada de líquidos e gorduras na região do avental abdominal.",
         "porque": "O formato inovador em pó que simula um suco natural gera um apelo de curiosidade visual muito forte nos anúncios. O rastreamento de dados em tempo real pegou um estouro na demanda de tráfego na Austrália, onde os afiliados locais raramente anunciam.",
         "cpc": "USA: $2.85 | UK: $1.95 | CA: $2.05 | AU: $2.15 | DE: $1.35"},
        
        {"ranking": 8, "nome": "Cortexi", "status": "🔥 TOP COMPRA", "plataforma": "ClickBank", "buscas_mes": 58000, "buscas_hoje": 1190, "melhor_pais": "Reino Unido (UK)", "seta": "📈 ACELERAÇÃO VENDAS", "semente": 57,
         "dor": "Zumbido estridente, agudo e incessante no pavilhão auditivo (Tinnitus) que interrompe o descanso noturno, causa irritabilidade psicológica severa e bloqueia a capacidade de memorização e concentração intelectual no dia a dia.",
         "ganho": "Proteção das células ciliadas auditivas e otimização da conducao nervosa cerebral contra inflamacoes.",
         "porque": "Ofertas direcionadas para dores auditivas extremas convertem puramente pelo desespero do cliente em obter alívio rápido. O lead gringo que sofre com zumbidos não gasta tempo pesquisando blogs, ele busca uma cura direta, clica no topo do leilão e compra.",
         "cpc": "USA: $2.50 | UK: $1.60 | CA: $1.80 | AU: $1.95 | DE: $1.15"},
        
        {"ranking": 9, "nome": "FlowForce Max", "status": "🔥 TOP COMPRA", "plataforma": "BuyGoods", "buscas_mes": 54000, "buscas_hoje": 1050, "melhor_pais": "Estados Unidos (USA)", "seta": "📈 SUBINDO SEVERO", "semente": 53,
         "dor": "Inflamação severa na próstata obrigando o homem sênior a interromper o sono de 4 a 6 vezes todas as noites para ir ao banheiro com forte queimação pélvica e jato urinário interrompido.",
         "ganho": "Desinflamação imediata do trato urinário e eliminação de sedimentos e toxinas minerais acumuladas no sistema reprodutor masculino.",
         "porque": "Produto de dor urgente vendido pela extrema necessidade de alívio rápido do lead gringo. Subir uma campanha direcionada para a rede de busca do Google Ads assegura cliques de alta intenção e comissões robustas por vendas de kits completos.",
         "cpc": "USA: $3.25 | UK: $2.20 | CA: $2.40 | AU: $2.55 | DE: $1.65"},
        
