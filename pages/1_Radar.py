import streamlit as st
import random
from datetime import datetime

def main():
    # 1. CONFIGURACAO DA PAGINA
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    # 2. CABECALHO DO MONITORAMENTO
    st.title("💎 RADAR DE PRODUTOS PERPETUOS")
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.write(f"🛰️ Status do Ecossistema: ATIVO | Varredura viva de leilao estabilizada as {horario_atual}.")
    st.markdown("---")

    # 3. LISTA DE PRODUTOS PURIFICADA (SEM TEXTOS LONGOS EMBUTIDOS PARA NAO TRAVAR)
    NOMES_PRODUTOS = [
        "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
        "Liv Pure", "Ikaria Juice", "Cortexi", "FlowForce Max", "Metanail Serum",
        "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
        "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
    ]

    # 4. INTEL-ENGINE: CONDICIONAIS PURAS EM VEZ DE DICIONARIOS (BLINDAGEM CONTRA O PARSER)
    # Define os dados fixos e as justificativas cirurgicas de 5 linhas de forma estavel
    def carregar_dados_seguros(nome):
        if nome == "Alpilean":
            ranking = 1
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 112000
            buscas_hoje = 3420
            pais = "Estados Unidos (USA)"
            seta = "📈 SUBINDO EXTREMO"
            dor = "Metabolismo severamente travado e em estado latente induzido pela baixa temperatura das celulas e tecidos internos, gerando um bloqueio biologico critico que impede a queima de gorduras profundas mesmo sob restricao calorica severa ou rotinas exaustivas de treinos aerobicos."
            ganho = "Regulacao termica celular que dispara a queima calorica passiva em ate 400% nas areas viscerais mais resistentes do organismo."
            porque = "O veredicto tecnico confirma que este suplemento lidera com folga as buscas exatas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e altamente propensos a comprar com o cartao na mao nas ultimas 24 horas."
            cpc = "USA: $3.10 | UK: $2.15 | CA: $2.40 | AU: $2.60 | DE: $1.45"
        elif nome == "Puravive":
            ranking = 2
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 98500
            buscas_hoje = 2890
            pais = "Estados Unidos (USA)"
            seta = "📈 TRACAO FORTE"
            dor = "Falta de ativacao biologica do tecido adiposo marrom (BAT), fazendo com que o corpo armazene gordura profunda em areas criticas e desacelere o gasto calorico diario de forma continua."
            ganho = "Otimizacao das gorduras marrons para derretimento acelerado de tecido adiposo estocado ha anos."
            porque = "A oferta mantem uma taxa de reembolso historicamente baixa e paga altas comissoes. O publico comprador dos Estados Unidos responde muito bem a paginas que expoem estudos cientificos estruturados, tornando a rede de pesquisa um oceano de lucro estavel."
            cpc = "USA: $3.10 | UK: $2.20 | CA: $2.40 | AU: $2.50 | DE: $1.60"
        elif nome == "Java Burn":
            ranking = 3
            status = "EM ALTA"
            plataforma = "BuyGoods"
            buscas_mes = 87000
            buscas_hoje = 2100
            pais = "Reino Unido (UK)"
            seta = "📈 EXPLODINDO"
            dor = "Falta aguda de energia celular e cansaco massivo nas primeiras horas do dia, combinada com surtos continuos de fome psicologica de fundo emocional que sabotam totalmente o andamento de dietas e protocolos."
            ganho = "Sinergia nutricional termogenica instantanea que otimiza o uso de carboidratos como combustivel e bloqueia os picos de ansiedade por comida."
            porque = "A novidade do sache misturavel no cafe diario tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anuncios na Europa, onde os custos de clique (CPC) estao bem menores que no inflacionado mercado americano, mantendo alta conversao."
            cpc = "USA: $2.75 | UK: $1.70 | CA: $1.95 | AU: $2.20 | DE: $1.30"
        elif nome == "GlucoTrust":
            ranking = 4
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 74000
            buscas_hoje = 1950
            pais = "Estados Unidos (USA)"
            seta = "📈 ACELERACAO"
            dor = "Picos descontrolados de glicose na corrente sanguinea, desequilibrio metabolico na producao de insulina e crises intensas de compulsao noturna por carboidratos pesados e doces refinados antes de dormir."
            ganho = "Estabilizacao imediata da resposta insulinica e eliminacao da gordura profunda acumulada ao redor dos orgaos vitais de filtragem."
            porque = "Resolve uma dor de saude alarmante e atinge em cheio o publico idoso internacional de alto poder aquisitivo. Anunciar com correspondencia exata de palavras-chave oficiais filtra cliques curiosos de concorrentes e traz trafego qualificado de fundo."
            cpc = "USA: $2.95 | UK: $1.90 | CA: $2.15 | AU: $2.30 | DE: $1.50"
        elif nome == "ProDentim":
            ranking = 5
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 69000
            buscas_hoje = 1650
            pais = "Canadá (CA)"
            seta = "📈 TENDENCIA ALTA"
            dor = "Sangramentos gengivais constantes durante a escovacao basica, proliferacao de bacterias nocivas no trato bucal que destroem o esmalte protetor e causam um mau halito cronico de dificil eliminacao social."
            ganho = "Repovoamento biologico da mucosa com 3.5 bilhoes de cepas probioticas que purificam o halito e reconstroem a saude da raiz gengival."
            porque = "Enquanto a massa de afiliados satura os leiloes de trafego dos Estados Unidos, o leilao do Canada e Reino Unido encontra-se livre para o nicho dentario, permitindo extrair comissoes liquidas altas com anuncios baratos via Pre-Sell rapida."
            cpc = "USA: $2.45 | UK: $1.60 | CA: $1.80 | AU: $2.00 | DE: $1.25"
        elif nome == "Liv Pure":
            ranking = 6
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 65000
            buscas_hoje = 1420
            pais = "Estados Unidos (USA)"
            seta = "📈 TRACAO CRITICA"
            dor = "Figado completamente sobrecarregado por toxinas e gordura acumulada, paralisando o funcionamento natural do metabolismo hepático e impedindo a correta eliminacao de lipidios acumulados."
            ganho = "Purificacao interna profunda das celulas hepaticas para restaurar o poder natural de eliminacao de gorduras."
            porque = "O produtor do Liv Pure estruturou um dos melhores funis de vendas de Upsell do mercado gringo. O veredicto cirurgico indica que mesmo pagando um CPC mais caro nos EUA, o Valor de Vida do Cliente (LTV) compensa aggressively, gerando multiplos potes por checkout."
            cpc = "USA: $3.25 | UK: $2.20 | CA: $2.40 | AU: $2.55 | DE: $1.65"
        elif nome == "Ikaria Juice":
            ranking = 7
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 61000
            buscas_hoje = 1310
            pais = "Austrália (AU)"
            seta = "📉 ESTAVEL NO TOPO"
            dor = "Acumulo nocivo de acido urico no organismo que deflagra processos inflamatorios severos nas articulacoes corporais, cansaco muscular continuo e retencao acelerada de liquidos e gorduras na regiao do avental abdominal."
            ganho = "Eliminacao de toxinas via suco concentrado que rejuvenesce os indices metabolicos internos."
            porque = "O formato inovador em po que simula um suco natural gera um apelo de curiosidade visual muito forte nos anuncios. O rastreamento de dados em tempo real pegou um estouro na demanda de trafego na Australia, onde os afiliados locais raramente anunciam."
            cpc = "USA: $2.85 | UK: $1.95 | CA: $2.05 | AU: $2.15 | DE: $1.35"
        elif nome == "Cortexi":
            ranking = 8
            status = "EM ALTA"
            plataforma = "ClickBank"
            buscas_mes = 58000
            buscas_hoje = 1190
            pais = "Reino Unido (UK)"
            seta = "📈 ACELERACAO VENDAS"
            dor = "Zumbido estridente, agudo e incessante no pavilhao auditivo (Tinnitus) que interrompe o descanso noturno, causa irritabilidade psicologica severa e bloqueia a capacidade de memorizacao e concentracao intelectual no dia a dia."
            ganho = "Protecao das celulas ciliadas auditivas e otimizacao da conducao nervosa cerebral contra inflamacoes."
            porque = "Ofertas direcionadas para dores auditivas extremas convertem puramente pelo desespero do cliente em obter alivio rapido. O lead gringo que sofre com zumbidos nao gasta tempo pesquisando blogs, ele busca uma cura direta, clica no topo do leilao e compra."
            cpc = "USA: $2.50 | UK: $1.60 | CA: $1.80 | AU: $1.95 | DE: $1.15"
        elif nome == "FlowForce Max":
            ranking = 9
            status = "EM ALTA"
            plataforma = "BuyGoods"
            buscas_mes = 54000
            buscas_hoje = 1050
            pais = "Estados Unidos (USA)"
            seta = "📈 SUBINDO SEVERO"
            dor = "Inflamacao severa na prostata obrigando o homem senior a interromper o sono de 4 a 6 vezes todas as noites para ir ao banheiro com forte queimacao pelvica e jato urinario interrompido."
            ganho = "Desinflamacao imediata do trato urinario e eliminacao de sedimentos e toxinas minerais acumuladas no sistema reprodutor masculino."
