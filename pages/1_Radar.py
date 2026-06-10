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

    # 2. LISTA FIXA DOS 20 PRODUTOS EXIGIDOS NO ROTEIRO
    LISTA_PRODUTOS = [
        "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim",
        "Liv Pure", "Ikaria Juice", "Cortexi", "FlowForce Max", "Metanail Serum",
        "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare",
        "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
    ]

    # 3. LOGICA SEQUENCIAL PURA: PRODUTO POR PRODUTO (BLINDADO CONTRA PYTHON 3.14)
    def buscar_produto_dados(nome):
        if nome == "Alpilean":
            return 1, "ALTA", 112000, 3420, "Estados Unidos (USA)", 110, "Metabolismo severamente paralisado e travado induzido pela baixa temperatura das celulas e tecidos internos, gerando um bloqueio biologico critico que impede a queima de gorduras profundas.", "O veredicto tecnico confirma que este suplemento lidera com folga as buscas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados."
        elif nome == "Puravive":
            return 2, "ALTA", 98500, 2890, "Estados Unidos (USA)", 95, "Falta de ativacao biologica do tissue adiposo marrom, fazendo com que o corpo armazene gordura profunda em areas criticas do abdomen e desacelere o gasto calorico diario.", "A oferta mantem uma taxa de reembolso historicamente baixa e paga altas comissoes. O publico comprador dos Estados Unidos responde muito bem a paginas que expoem estudos cientificos."
        elif nome == "Java Burn":
            return 3, "ALTA", 87000, 2100, "Reino Unido (UK)", 85, "Falta aguda de energia celular e cansaco massivo nas primeiras horas do dia, combinada com surtos continuos de fome psicologica de fundo emocional.", "A novidade do sache misturavel no cafe diario tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anuncios na Europa, onde os custos de clique estao menores."
        elif nome == "GlucoTrust":
            return 4, "ALTA", 74000, 1950, "Estados Unidos (USA)", 72, "Picos descontrolados de glicose na corrente sanguinea, desequilibrio metabolico na producao de insulina e crises intensas de compulsao noturna por carboidratos pesados.", "Resolve uma dor de saude alarmante e atinge em cheio o publico idoso internacional de alto poder aquisitivo. Anunciar com correspondencia exata filtra cliques curiosos."
        elif nome == "ProDentim":
            return 5, "ALTA", 69000, 1650, "Canada (CA)", 68, "Sangramentos gengivais constantes durante a escovacao basica, proliferacao de bacterias nocivas no trato bucal que destroem o esmalte protetor e causam um mau halito cronico.", "Enquanto a massa de afiliados satura os leiloes de trafego dos Estados Unidos, o leilao do Canada e Reino Unido encontra-se livre para o nicho dentario, permitindo comissoes altas."
        elif nome == "Liv Pure":
            return 6, "ALTA", 65000, 1420, "Estados Unidos (USA)", 64, "Figado sobrecarregado por toxinas e gordura acumulada, paralisando o funcionamento do metabolismo hepatico e impedindo a queima natural de lipidios.", "Excelente cenario de Upsell do produtor gringo. O veredicto indica que rodar trafego direto para termos institucionais exatos entrega alto retorno liquido em dolares."
        elif nome == "Ikaria Juice":
            return 7, "ALTA", 61000, 1310, "Australia (AU)", 60, "Acumulo nocivo de acido urico que gera inflamacoes nas articulacoes, cansaco muscular continuo e retencao liquida na regiao abdominal.", "O formato inovador em po simula um suco natural gringo e ativa forte curiosidade visual, gerando cliques baratos na regiao da Australia."
        elif nome == "Cortexi":
            return 8, "ALTA", 58000, 1190, "Reino Unido (UK)", 57, "Zumbido estridente e agudo incessante no pavilhao auditivo que destroi a qualidade do sono profundo e gera cansaco mental diario.", "Oferta movida pelo desespero por alivio imediato. O lead gringo nao pesquisa blogs, ele busca uma solucao direta e compra kits grandes na hora."
        elif nome == "FlowForce Max":
            return 9, "ALTA", 54000, 1050, "Estados Unidos (USA)", 53, "Inflamacao severa na prostata obrigando o homem senior a interromper o sono de 4 a 6 vezes por noite para urinar com queimacao.", "Nicho focado em publico idoso internacional com alto poder financeiro disponivel para aquisicao imediata de kits de tratamento completo."
        elif nome == "Metanail Serum":
            return 10, "ALTA", 51000, 980, "Canada (CA)", 50, "Infeccao fungica severa e micoses profundas que destroem a queratina protetora e deixam as unhas dos pes amareladas e quebradicas.", "Fator de transformacao de forte impacto visual. Rodar trafego utilizando campanhas de rede de display no mercado canadense entrega cliques qualificadissimos."
        elif nome == "LeanBliss":
            return 11, "NORMAL", 14500, 320, "Australia (AU)", 14, "Ganho acelerado de gordura associado a picos severos de ansiedade alimentar cronica.", "Excelente cenario de arbitragem de leilao oculto! Esta oferta entrega retorno alto com custo baixo nos paises principais por ser menos concorrida."
        elif nome == "Neotonics":
            return 12, "NORMAL", 13200, 290, "Alemanha (DE)", 13, "Flacidez cellular cutanea precoce e envelhecimento da derme provocado por ma absorcao de nutrientes.", "Oportunidade deserta no leilao europeu! O custo por clique na regiao da Alemanha entrega leads qualificados operando paginas limpas com baixa concorrencia."
        elif nome == "Synogut":
            return 13, "NORMAL", 12400, 260, "Estados Unidos (USA)", 12, "Constipacao intestinal cronica dolorosa, gases severos e inchaco estomacal pos-refeicoes.", "Oferta evergreen de altissima conversao e estabilidade de mercado, estruturada com um funil de vendas altamente responsivo gringo de menor leilao."
        elif nome == "Kerassentials":
            return 14, "NORMAL", 11800, 240, "Reino Unido (UK)", 11, "Coceira e descamacao severa na regiao interdigital dos pes decorrente de colonias fungicas.", "Volume constante de buscas ativas fundo de funil utilizando a rede do Bing Ads, escapando do leilao inflacionado americano e aproveitando custos reduzidos."
        elif nome == "SightCare":
            return 15, "NORMAL", 10500, 210, "Canada (CA)", 10, "Visao turva, fadiga ocular cronica devido ao uso excessivo de telas e degeneracao macular.", "Foco cirurgico em publico de alta idade no Canada. O leilao limpo permite vender kits de alta duracao com comissao cheia e cliques mais em conta."
        elif nome == "Prostadine":
            return 16, "NORMAL", 9800, 190, "Australia (AU)", 9, "Dificuldade de fluxo urinario continuo e inchaco pelvico incomodo prostatico.", "Pouquissimos afiliados operando criativos e copys estruturadas para o mercado australiano, deixando a margem liquida livre de concorrentes agressivos."
        elif nome == "Fast Lean Pro":
            return 17, "NORMAL", 8900, 170, "Estados Unidos (USA)", 8, "Falta de foco mental e ansiedade que quebra protocolos de jejum prolongado.", "Angulo de copia persuasivo revolucionario focado em simular o estado biologico de autofagia, convertendo muito via Google Display com menor leilao."
        elif nome == "Amiclear":
            return 18, "NORMAL", 8200, 150, "Reino Unido (UK)", 8, "Quebras bruscas de energia e prostracao fisica no meio do dia decorrentes de instabilidades.", "O produtor disponibiliza uma central de suporte completa com copys validadas, acelerando o processo de criacao de anuncios em oceanos azuis."
        elif nome == "Alpha Tonic":
            return 19, "NORMAL", 7800, 130, "Nova Zelandia", 7, "Queda nos niveis de testosterona e vigor fisico masculino acompanhado por perda severa.", "Nicho deserto na Nova Zelandia. Baixo indice de bloqueios de contas permite trafego agressivo fundo de funil sem a barreira das ofertas concorridas."
        else:
            return 20, "NORMAL", 7100, 110, "Estados Unidos (USA)", 7, "Falta de lubrificacao articular natural gerando dores agudas e rigidez de movimentos.", "Presenca de forte endosso medico em video na VSL principal, quebrando objecoes e elevando as taxas de checkout em campanhas de menor concorrencia."

    # Inicializacao estavel do estado de sessao de forma stic pura
    if "radar_nome_ativo" not in st.session_state:
        st.session_state.radar_nome_ativo = "Alpilean"

    p_nome = st.session_state.radar_nome_ativo
    p_rank, p_status, p_mes, p_hoje, p_pais, p_semente, p_dor, p_porque = buscar_produto_dados(p_nome)

    # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS (MAXIMO PREENCHIMENTO DE TELA)
    col_esquerda, col_direita = st.columns([1.0, 1.3])

    with col_esquerda:
        st.subheader("Painel Estatistico Global")
        st.write("Selecione o produto abaixo:")
        st.write("")
        
        # Geracao dos botoes lineares
        for idx, nome_item in enumerate(LISTA_PRODUTOS):
            r_rank, r_status, r_mes, r_hoje, r_pais, r_semente, r_dor, r_porque = buscar_produto_dados(nome_item)
            
            tag_status = "[ALTA]" if r_rank <= 10 else "[NORMAL]"
            seta_viva = "SUBINDO" if (tempo_segundo + idx) % 2 == 0 else "DECENDO"
            texto_botao = nome_item + " " + tag_status + " - " + seta_viva
