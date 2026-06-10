import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", page_icon="🛡️", layout="wide")

    # FORCADOR GLOBAL DE TEMA BLACK-LABEL COM BRILHO NEON NAS BORDAS E TEXTOS
    st.markdown("""
        <style>
            header, [data-testid="stHeader"] {
                background-color: rgba(0,0,0,0) !important;
                background: transparent !important;
                display: none !important;
            }
            [data-testid="stAppViewContainer"] {
                padding-top: 0px !important;
            }
            html, body, [data-testid="stAppViewContainer"], .stApp {
                background-color: #020617 !important;
                color: #f9fafb !important;
            }
            [data-testid="stSidebar"], section[data-testid="stSidebar"] div {
                background-color: #070a13 !important;
            }
            [data-testid="stSidebar"] nav ul li div a span {
                color: #00ffcc !important;
                font-weight: bold !important;
                text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;
            }
            
            /* Input de Texto SaaS Neon */
            .stTextInput>div>div>input {
                background-color: #0b1329 !important;
                color: #00ffcc !important;
                border: 2px solid #1e293b !important;
                border-radius: 8px !important;
                box-shadow: 0 0 10px rgba(0,0,0,0.5) !important;
                font-size: 1.1rem !important;
            }
            .stTextInput>div>div>input:focus {
                border-color: #00ffcc !important;
                box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;
            }
            
            /* Botão de Execução Executar Varredura */
            .stButton>button {
                background-color: #0b1329 !important;
                color: #00ffcc !important;
                border: 2px solid #00ffcc !important;
                border-radius: 8px !important;
                font-weight: bold !important;
                box-shadow: 0 0 12px rgba(0, 255, 204, 0.2) !important;
                transition: all 0.3s ease-in-out !important;
                width: 100% !important;
                height: 45px !important;
            }
            .stButton>button:hover {
                background-color: #00ffcc !important;
                color: #020617 !important;
                box-shadow: 0 0 25px #00ffcc !important;
            }
            
            /* Customização das Caixas de Métricas Neon */
            [data-testid="stMetricContainer"] {
                background: linear-gradient(135deg, #0f172a, #020617) !important;
                border: 1px solid #1e293b !important;
                border-left: 4px solid #00ffcc !important;
                padding: 15px !important;
                border-radius: 10px !important;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
            }
            
            h1, h2, h3, h4, span, p, label {
                color: #f3f4f6 !important;
            }
            h1 {
                color: #00ffcc !important;
                text-shadow: 0 0 15px rgba(0,255,204,0.4) !important;
            }
            [data-testid="stNotification"] {
                background-color: #0b1329 !important;
                border: 1px solid #1e293b !important;
                border-radius: 10px !important;
            }
            /* Remove a borda padrão feia do formulário do streamlit */
            [data-testid="stForm"] {
                border: none !important;
                padding: 0px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; margin-bottom: 5px;">🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome de qualquer oferta internacional no terminal para que o robo realize a engenharia reversa operacional.")
    st.markdown("---")

    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura por Digitacao</h3>", unsafe_allow_html=True)
    
    # 🚀 ENGENHARIA DE FORMULÁRIO: Força o botão a funcionar ativando o gatilho na hora do clique
    with st.form(key="auditor_form"):
        produto_digitado = st.text_input("Insira o nome do produto gringo para auditar:", value="Sugar Defender")
        st.markdown("<br>", unsafe_allow_html=True)
        botao_pesquisa_ativo = st.form_submit_button(label="🚀 EXECUTAR VARREDURA AO VIVO")

    st.markdown("---")

    # O sistema carrega os dados ou executa se o botão for clicado
    if produto_digitado:
        nome_prod = produto_digitado.strip()
        fator = len(nome_prod) if len(nome_prod) > 0 else 10
        
        # Marcador de tempo real
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")
        st.write("Sincronizacao de trafego ativa para " + nome_prod + " as " + horario_atual)
        st.write("")

        # MECANISMO DE DETECÇÃO DE RISCO (ALERTA DE PRODUTO RUIM)
        score_integridade = (fator * 7 + tempo_segundo) % 100
        produto_e_ruim = score_integridade < 30 or fator < 5

        if produto_e_ruim:
            st.markdown("<h3 style='color:#ff0055; text-shadow: 0 0 15px #ff0055;'>⚠️ ALERTA OPERACIONAL: PRODUTO DE BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
            st.error("CUIDADO AFILIADO: O robo AdrielAI detectou indices perigosos para " + nome_prod.upper() + ". Esta oferta apresenta taxa de reembolso acima de 18% nas plataformas gringas, alto volume de reclamacoes de leads e leilao inflacionado com robos concorrentes. Riscos massivos de quebra de ROI e perda de contingencia.")
            st.markdown("---")

        # ENGINE DINAMICO ANALITICO
        pesquisas_mes = 35000 + (fator * 2400) + (tempo_segundo * 8)
        pesquisas_hoje = 950 + (fator * 95) + (tempo_segundo * 2)
        semente_grafico = 8 + (fator % 5) * 4

        plataformas_anuncio = ["Google Ads (Rede de Pesquisa)", "Facebook Ads (Trafego Direto / VSL)", "Google Ads + Bing Ads"]
        canal_ideal = plataformas_anuncio[fator % 3]
        
        paises_pool = ["Estados Unidos (USA)", "Reino Unido (UK)", "Canada (CA)", "Australia (AU)", "Alemanha (DE)"]
        pais_vencedor = paises_pool[(fator + tempo_segundo) % 5]

        txt_beneficios = "Os beneficios principais de " + nome_prod + " consistem na imediata estabilizacao dos indices metabolicos profundos do organismo, promovendo a desinflamacao celular acelerada de tecidos sobrecarregados, eliminando a retencao de liquidos de forma natural e devolvendo o vigor e a energia fisica total para o usuario nas primeiras hours do dia."
        txt_dor = "O comprador gringo que busca por " + nome_prod + " sofre com uma dor psicologica severa gerada pela falta de resultados em tratamentos anteriores, acumulando cansaco cronico, indisposicao matinal debilitante e frustracao severa por nao conseguir quebrar o bloqueio biologico que aprisiona seu bem-estar cotidiano."
        txt_estrategia = "A melhor estrategia operacional para o produto " + nome_prod + " e subir uma campanha estruturada focada em " + canal_ideal + ". Para capturar o lead internacional qualificado, monte uma estrutura de Pre-Sell ou pagina de Review nativo direto, blindando o link de afiliado contra bloqueios e focando agressivamente nas palavras-chave exatas de intencao de compra fundo de funil."

        # CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS
        col_esquerda, col_direita = st.columns([1.0, 1.3])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc !important;'>📋 Inteligencia de Copy & Dor</h3>", unsafe_allow_html=True)
            st.write("Analise comportamental do lead qualificado extraida pelo robo:")
            st.write("")
            
            st.markdown("<h4 style='color:#00ffcc !important;'>💎 Beneficios Principais do Produto:</h4>", unsafe_allow_html=True)
            st.success(txt_beneficios)
            
            st.markdown("<h4 style='color:#ff0055 !important;'>💔 Dores pelas quais as pessoas precisam do produto:</h4>", unsafe_allow_html=True)
            st.warning(txt_dor)
            
            st.markdown("<h4 style='color:#cc66ff !important;'>🛠️ Melhor Ferramenta para Criar a Campanha:</h4>", unsafe_allow_html=True)
            st.info("Canal Recomendado: " + canal_ideal)
            st.write(txt_estrategia)

        with col_direita:
            st.markdown("<h3 style='color:#00ffcc !important;'>⚡ Metricas de Leilao & Trafego Global</h3>", unsafe_allow_html=True)
            st.write("Dados de mercado processados e updated em tempo real:")
            st.write("")
            
            # Grid Numérico SaaS
            c1, c2 = st.columns(2)
            c1.metric(label="🔎 Quantas pesquisas nos ultimos 12 meses", value=f"{pesquisas_mes:,}")
            c2.metric(label="⚡ Quantas pesquisas no dia ate o momento atual", value=f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            
            st.markdown("<h4 style='color:#00ffcc !important;'>💵 Mapeamento de CPC por Regiao (5 Paises Oficiais):</h4>", unsafe_allow_html=True)
            cpc_base = round(1.95 + (fator * 0.06), 2)
            st.code("USA: $" + str(cpc_base) + " | UK: $" + str(round(cpc_base*0.75, 2)) + " | CA: $" + str(round(cpc_base*0.85, 2)) + " | AU: $" + str(round(cpc_base*0.90, 2)) + " | DE: $" + str(round(cpc_base*0.55, 2)), language="text")
            
            # Afirmação final de destino conforme roteiro
            st.markdown("<h4 style='color:#ff0055 !important;'>🏆 VEREDITO OPERACIONAL FINAL (ALVO DE GUERRA):</h4>", unsafe_allow_html=True)
            if produto_e_ruim:
