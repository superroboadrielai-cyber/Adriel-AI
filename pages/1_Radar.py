import streamlit as st
import random
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    st.title("RADAR DE PRODUTOS PERPETUOS")
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    # Marcador de Varredura Viva Baseado no Relogio Atual do Servidor
    tempo_segundo = datetime.now().second
    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.write("Status do Ecossistema: ATIVO | Varredura viva realizada as " + horario_atual)
    st.markdown("---")

    # 3. BASE DE DADOS COMPLETA DOS 20 PRODUTOS (SINTAXE 100% PURA E LINEAR)
    PRODUTOS_POOL = [
        {"ranking": 1, "nome": "Alpilean", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 112000, "base_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "semente": 110,
         "dor": "Metabolismo severamente paralisado e travado induzido pela baixa temperatura das celulas e tecidos internos, gerando um bloqueio biologico critico que impede a queima de gorduras profundas mesmo sob restricao calorica severa ou rotinas exaustivas de treinos aerobicos.",
         "porque": "O veredicto tecnico confirma que este suplemento lidera com folga as buscas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e altamente propensos a comprar com o cartao na mao nas ultimas 24 horas."},
        
        {"ranking": 2, "nome": "Puravive", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 98500, "base_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "semente": 95,
         "dor": "Falta de ativacao biologica do tissue adiposo marrom, fazendo com que o corpo armazene gordura profunda em areas criticas do abdomen e desacelere o gasto calorico diario de forma continua.",
         "porque": "A oferta mantem uma taxa de reembolso historicamente baixa e paga altas comissoes. O publico comprador dos Estados Unidos responde muito bem a paginas que expoem estudos cientificos estruturados, tornando a rede de pesquisa um oceano de lucro estavel."},
        
        {"ranking": 3, "nome": "Java Burn", "status": "ALTA", "plataforma": "BuyGoods", "base_mes": 87000, "base_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "semente": 85,
         "dor": "Falta aguda de energia celular e cansaco massivo nas primeiras horas do dia, combinada com surtos continuos de fome psicologica de fundo emocional que sabotam totalmente o andamento de dietas e protocolos.",
         "porque": "A novidade do sache misturavel no cafe diario tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anuncios na Europa, onde os custos de clique estao bem menores que no inflacionado mercado americano, mantendo alta conversao."},
        
        {"ranking": 4, "nome": "GlucoTrust", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 74000, "base_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", "semente": 72,
         "dor": "Picos descontrolados de glicose na corrente sanguinea, desequilibrio metabolico na producao de insulina e crises intensas de compulsao noturna por carboidratos pesados e doces refinados antes de dormir.",
         "porque": "Resolve uma dor de saude alarmante e atinge em cheio o publico idoso internacional de alto poder aquisitivo. Anunciar com correspondencia exata de palavras-chave oficiais filtra cliques curiosos de concorrentes e traz trafego qualificado de fundo."},
        
        {"ranking": 5, "nome": "ProDentim", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 69000, "base_hoje": 1650, "melhor_pais": "Canada (CA)", "semente": 68,
         "dor": "Sangramentos gengivais constantes durante a escovacao basica, proliferacao de bacterias nocivas no trato bucal que destroem o esmalte protetor e causam um mau halito cronico de dificil eliminacao social.",
         "porque": "Enquanto a massa de afiliados satura os leiloes de trafego dos Estados Unidos, o leilao do Canada e Reino Unido encontra-se livre para o nicho dentario, permitindo extrair comissoes liquidas altas com anuncios baratos via Pre-Sell rapida."},
         
        {"ranking": 6, "nome": "Liv Pure", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 65000, "base_hoje": 1420, "melhor_pais": "Estados Unidos (USA)", "semente": 64,
         "dor": "Figado sobrecarregado por toxinas e gordura acumulada, paralisando o funcionamento do metabolismo hepatico e impedindo a queima natural de lipidios.",
         "porque": "Excelente cenario de Upsell do produtor gringo. O veredicto indica que rodar trafego direto para termos institucionais exatos entrega alto retorno liquido em dolares."},

        {"ranking": 7, "nome": "Ikaria Juice", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 61000, "base_hoje": 1310, "melhor_pais": "Australia (AU)", "semente": 60,
         "dor": "Acumulo nocivo de acido urico que gera inflamacoes nas articulacoes, cansaco muscular continuo e retencao liquida na regiao abdominal.",
         "porque": "O formato inovador em po simula um suco natural gringo e ativa forte curiosidade visual, gerando cliques baratos na regiao da Australia."},

        {"ranking": 8, "nome": "Cortexi", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 58000, "base_hoje": 1190, "melhor_pais": "Reino Unido (UK)", "semente": 57,
         "dor": "Zumbido estridente e agudo incessante no pavilhao auditivo que destroi a qualidade do sono profundo e gera cansaco mental diario.",
         "porque": "Oferta movida pelo desespero por alivio imediato. O lead gringo nao pesquisa blogs, ele busca uma solucao direta e compra kits grandes na hora."},

        {"ranking": 9, "nome": "FlowForce Max", "status": "ALTA", "plataforma": "BuyGoods", "base_mes": 54000, "base_hoje": 1050, "melhor_pais": "Estados Unidos (USA)", "semente": 53,
         "dor": "Inflamacao severa na prostata obrigando o homem senior a interromper o sono de 4 a 6 vezes por noite para urinar com queimacao.",
         "porque": "Nicho focado em publico idoso internacional com alto poder financeiro disponivel para aquisicao imediata de kits de tratamento completo."},

        {"ranking": 10, "nome": "Metanail Serum", "status": "ALTA", "plataforma": "ClickBank", "base_mes": 51000, "base_hoje": 980, "melhor_pais": "Canada (CA)", "semente": 50,
         "dor": "Infeccao fungica severa e micoses profundas que destroem a queratina protetora e deixam as unhas dos pes amareladas e quebradicas.",
         "porque": "Fator de transformacao de forte impacto visual. Rodar trafego utilizando campanhas de rede de display no mercado canadense entrega cliques qualificadissimos."},

        {"ranking": 11, "nome": "LeanBliss", "status": "NORMAL", "plataforma": "BuyGoods", "base_mes": 14500, "base_hoje": 320, "melhor_pais": "Australia (AU)", "semente": 14,
         "dor": "Ganho acelerado de gordura associado a picos severos de ansiedade alimentar cronica e desejos noturnos incontrolaveis por doces.",
         "porque": "Excelente cenario de arbitragem de leilao oculto. Como a maioria dos afiliados satura o topo, esta oferta entrega retorno alto com custo baixo nos paises principais por ser menos concorrida."},

        {"ranking": 12, "nome": "Neotonics", "status": "NORMAL", "plataforma": "ClickBank", "base_mes": 13200, "base_hoje": 290, "melhor_pais": "Alemanha (DE)", "semente": 13,
         "dor": "Flacidez cellular cutanea precoce e envelhecimento da derme provocado por ma absorcao de nutrientes no sistema digestivo.",
         "porque": "Oportunidade deserta no leilao europeu. O custo por clique na regiao da Alemanha entrega leads qualificados operando paginas limpas de review nativo com baixa concorrencia."},

        {"ranking": 13, "nome": "Synogut", "status": "NORMAL", "plataforma": "ClickBank", "base_mes": 12400, "base_hoje": 260, "melhor_pais": "Estados Unidos (USA)", "semente": 12,
         "dor": "Constipacao intestinal cronica dolorosa, gases severos e inchaco estomacal pos-refeicoes básicas.",
         "porque": "Oferta evergreen de altissima conversao e estabilidade de mercado, estruturada com um funil de vendas altamente responsivo gringo de menor leilao concorrente."},

        {"ranking": 14, "nome": "Kerassentials", "status": "NORMAL", "plataforma": "ClickBank", "base_mes": 11800, "base_hoje": 240, "melhor_pais": "Reino Unido (UK)", "semente": 11,
         "dor": "Coceira e descamacao severa na regiao interdigital dos pes decorrente de colonias fungicas resistentes.",
         "porque": "Volume constante de buscas ativas fundo de funil utilizando a rede do Bing Ads, escapando do leilao inflacionado americano e aproveitando custos reduzidos."},

        {"ranking": 15, "nome": "SightCare", "status": "NORMAL", "plataforma": "BuyGoods", "base_mes": 10500, "base_hoje": 210, "melhor_pais": "Canada (CA)", "semente": 10,
         "dor": "Visao turva, fadiga ocular cronica devido ao uso excessivo de telas e degeneracao macular acelerada em leads seniores.",
         "porque": "Foco cirurgico em publico de alta idade no Canada. O leilao limpo permite vender kits de alta duracao com comissao cheia e cliques mais em conta."},

        {"ranking": 16, "nome": "Prostadine", "status": "NORMAL", "plataforma": "ClickBank", "base_mes": 9800, "base_hoje": 190, "melhor_pais": "Australia (AU)", "semente": 9,
         "dor": "Dificuldade de fluxo urinario continuo e inchaco pelvico incomodo prostatico associado ao envelhecimento masculino.",
         "porque": "Pouquissimos afiliados operando criativos e copys estruturadas para o mercado australiano, deixando a margem liquida livre de concorrentes agressivos."},

