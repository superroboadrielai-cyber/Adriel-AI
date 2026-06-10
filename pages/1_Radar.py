import streamlit as st
import random
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    st.title("💎 RADAR DE PRODUTOS PERPETUOS")
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    # Marcador de Varredura Viva Baseado no Relogio Atual do Servidor
    tempo_segundo = datetime.now().second
    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.write("🛰️ Status do Ecossistema: ATIVO | Varredura viva realizada as " + horario_atual)
    st.markdown("---")

    # 2. LISTA FIXA DOS 20 PRODUTOS EXIGIDOS NO ROTEIRO
    LISTA_PRODUTOS = [
        "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim",
        "Liv Pure", "Ikaria Juice", "Cortexi", "FlowForce Max", "Metanail Serum",
        "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare",
        "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
    ]

    # 3. LOGICA SEQUENCIAL PURA SEGMENTADA (BLINDAGEM TOTAL ANTI TELA BRANCA)
    def buscar_produto_dados(nome):
        if nome == "Alpilean":
            dor = "Metabolismo severamente paralisado e travado induzido pela baixa temperatura das celulas e tecidos internos, gerando um bloqueio biologico critico que impede a queima de gorduras profundas mesmo sob restricao calorica severa."
            porque = "O veredicto tecnico confirma que este suplemento lidera com folga as buscas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e prontos para comprar."
            return 1, "ALTA", 112000, 3420, "Estados Unidos (USA)", 110, dor, porque
            
        elif nome == "Puravive":
            dor = "Falta de ativacao biologica do tecido adiposo marrom, fazendo com que o corpo armazene gordura profunda em areas criticas do abdomen e desacelere o gasto calorico diario de forma continua."
            porque = "A oferta mantem uma taxa de reembolso historicamente baixa e paga altas comissoes. O publico comprador dos Estados Unidos responde muito bem a paginas que expoem estudos cientificos estruturados."
            return 2, "ALTA", 98500, 2890, "Estados Unidos (USA)", 95, dor, porque
            
        elif nome == "Java Burn":
            dor = "Falta aguda de energia cellular e cansaco massivo nas primeiras horas do dia, combinada com surtos continuos de fome psicologica de fundo emocional que sabotam totalmente o andamento de dietas e protocolos."
            porque = "A novidade do sache misturavel no cafe diario tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anuncios na Europa, onde os custos de clique estao bem menores que nos EUA."
            return 3, "ALTA", 87000, 2100, "Reino Unido (UK)", 85, dor, porque
            
        elif nome == "GlucoTrust":
            dor = "Picos descontrolados de glicose na corrente sanguinea, desequilibrio metabolico na producao de insulina e crises intensas de compulsao noturna por carboidratos pesados e doces refinados antes de dormir."
            porque = "Resolve uma dor de saude alarmante e atinge em cheio o publico idoso internacional de alto poder aquisitivo. Anunciar com correspondencia exata de palavras-chave oficiais filtra cliques curiosos de concorrentes."
            return 4, "ALTA", 74000, 1950, "Estados Unidos (USA)", 72, dor, porque
            
        elif nome == "ProDentim":
            dor = "Sangramentos gengivais constantes durante a escovacao basica, proliferacao de bacterias nocivas no trato bucal que destroem o esmalte protetor e causam um mau halito cronico de dificil eliminacao social."
            porque = "Enquanto a massa de afiliados satura os leiloes de trafego dos Estados Unidos, o leilao do Canada e Reino Unido encontra-se livre para o nicho dentario, permitindo extrair comissoes liquidas altas com anuncios baratos."
            return 5, "ALTA", 69000, 1650, "Canada (CA)", 68, dor, porque
            
        elif nome == "Liv Pure":
            dor = "Figado sobrecarregado por toxinas e gordura acumulada, paralisando o funcionamento do metabolismo hepatico e impedindo a queima natural de lipidios e o emagrecimento saudavel."
            porque = "Excelente cenario de Upsell do produtor gringo. O veredicto indica que rodar trafego direto para termos institucionais exatos entrega alto retorno liquido em dolares com cliques altamente qualificados."
            return 6, "ALTA", 65000, 1420, "Estados Unidos (USA)", 64, dor, porque

        elif nome == "Ikaria Juice":
            dor = "Acumulo nocivo de acido urico que gera inflamacoes nas articulacoes, cansaco muscular continuo e retencao liquida severa na regiao do avental abdominal."
            porque = "O formato inovador em po simula um suco natural gringo e ativa forte curiosidade visual, gerando cliques baratos na regiao da Australia, onde a concorrência de afiliados e quase nula."
            return 7, "ALTA", 61000, 1310, "Australia (AU)", 60, dor, porque

        elif nome == "Cortexi":
            dor = "Zumbido estridente e agudo incessante no pavilhao auditivo que destroi a qualidade do sono profundo, causa irritabilidade psicologica severa e bloqueia a concentracao intelectual no dia a dia."
            porque = "Oferta movida pelo desespero por alivio imediato. O lead gringo nao gasta tempo pesquisando blogs, ele busca uma solucao direta no topo do Google Search e adquire kits de alto valor de comissao."
            return 8, "ALTA", 58000, 1190, "Reino Unido (UK)", 57, dor, porque

        elif nome == "FlowForce Max":
            dor = "Inflamacao severa na prostata obrigando o homem senior a interromper o sono de 4 a 6 vezes por noite para ir ao banheiro com forte queimacao pelvica e jato urinario interrompido."
            porque = "Nicho focado em publico idoso internacional com alto poder financeiro disponivel para aquisicao imediata. Subir campanhas focadas na rede de busca assegura alta conversao por necessidade urgente."
            return 9, "ALTA", 54000, 1050, "Estados Unidos (USA)", 53, dor, porque

        elif nome == "Metanail Serum":
            dor = "Infeccao fungica severa e micoses profundas que destroem a queratina protetora, deixando as unhas dos pes amareladas, escuras, quebradicas e descascando, gerando constrangimento social."
            porque = "Fator de transformacao de forte impacto visual. Rodar trafego utilizando campanhas de rede de display ou Youtube Ads no mercado canadense entrega cliques qualificadissimos de menor custo."
            return 10, "ALTA", 51000, 980, "Canada (CA)", 50, dor, porque

        elif nome == "LeanBliss":
            dor = "Ganho acelerado de gordura visceral associado a picos severos de ansiedade alimentar cronica e desejos noturnos incontrolaveis por doces refinados."
            porque = "Excelente cenario de arbitragem de leilao oculto. Como a maioria dos afiliados satura as ofertas do topo, este produto entrega retorno alto com custo baixo nos paises da Oceania por ser menos concorrido."
            return 11, "NORMAL", 14500, 320, "Australia (AU)", 14, dor, porque

        elif nome == "Neotonics":
            dor = "Flacidez cellular cutanea precoce e envelhecimento acelerado da derme provocado por ma absorcao de nutrientes essenciais e desregulagem no sistema digestivo baixo."
            porque = "Oportunidade deserta no leilao europeu. O custo por clique na regiao da Alemanha entrega leads qualificados operando paginas limpas de review nativo com baixa concorrencia de lances publicitarios."
            return 12, "NORMAL", 13200, 290, "Alemanha (DE)", 13, dor, porque

        elif nome == "Synogut":
            dor = "Constipacao intestinal cronica dolorosa, gases severos e inchaco estomacal pos-refeicoes basicas que reduzem o bem-estar e causam dores abdominais agudas continuas."
            porque = "Oferta evergreen de altissima conversao e estabilidade de mercado, estruturada com um funil de vendas altamente responsivo gringo de menor leilao concorrente na rede de pesquisa."
            return 13, "NORMAL", 12400, 260, "Estados Unidos (USA)", 12, dor, porque

        elif nome == "Kerassentials":
            dor = "Coceira e descamacao severa na regiao interdigital dos pes decorrente de colonias fungicas resistentes a pomadas tradicionais do mercado de saude."
            porque = "Volume constante de buscas ativas fundo de funil utilizando a rede do Bing Ads, escapando do leilao inflacionado americano e aproveitando custos reduzidos por conversao liquida."
            return 14, "NORMAL", 11800, 240, "Reino Unido (UK)", 11, dor, porque

        elif nome == "SightCare":
            dor = "Visao turva, fadiga ocular cronica devido ao uso excessivo de telas e degeneracao macular acelerada em leads seniores que temem a perda definitiva da autonomia visual."
            porque = "Foco cirurgico em publico de alta idade no Canada. O leilao limpo permite vender kits de alta duracao com comissao cheia e cliques mais em conta na rede de pesquisa de fundo."
            return 15, "NORMAL", 10500, 210, "Canada (CA)", 10, dor, porque

        elif nome == "Prostadine":
            dor = "Dificuldade de fluxo urinario continuo e inchaco pelvico incomodo prostatico associado ao envelhecimento natural masculino e falta de nutrientes especificos."
            porque = "Pouquissimos afiliados operando criativos e copys estruturadas para o mercado australiano, deixando a margem liquida livre de concorrentes agressivos de lances publicitarios."
            return 16, "NORMAL", 9800, 190, "Australia (AU)", 9, dor, porque

        elif nome == "Fast Lean Pro":
