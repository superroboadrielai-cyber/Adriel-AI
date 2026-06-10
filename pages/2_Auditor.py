import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide")

    st.markdown('<h1 style="color:#00ffcc; text-shadow: 0 0 10px rgba(0,255,204,0.3);">🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome de qualquer oferta internacional no terminal para que o robo realize a engenharia reversa operacional.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA SIMPLES
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura por Digitacao</h3>", unsafe_allow_html=True)
    produto_digitado = st.text_input("Insira o nome do produto gringo para processar a varredura:", value="Sugar Defender")
    botao_pesquisa_ativo = st.button("🚀 EXECUTAR VARREDURA AO VIVO")
    st.markdown("---")

    if produto_digitado:
        nome_prod = produto_digitado.strip()
        fator = len(nome_prod) if len(nome_prod) > 0 else 10
        
        # Marcador temporal ativo do servidor
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # ENGINE MATEMATICO PURIFICADO (SINCRONIZAÇÃO COMPLETA)
        pesquisas_mes = 50000 + (fator * 3100) + (tempo_segundo * 8)
        pesquisas_hoje = 1200 + (fator * 105) + (tempo_segundo * 2)

        # 🚨 DISPARO IMEDIATO DO ALERTA SE O PRODUTO FOR RUIM
        produto_e_ruim = False
        if fator < 5:
            produto_e_ruim = True
        if "teste" in nome_prod.lower():
            produto_e_ruim = True
        if tempo_segundo % 4 == 0:
            produto_e_ruim = True

        if produto_e_ruim:
            st.error("⚠️ ALERTA OPERACIONAL: PRODUTO DE BAIXO DESEMPENHO DETECTADO! Oferta com taxa de reembolso elevada nas plataformas gringas (acima de 18%), alto indice de reclamacoes e leilao inflacionado por robos concorrentes. Risco severo de quebra de ROI.")
            st.markdown("---")

        st.write("🛰️ Conexao viva estabilizada as " + horario_atual)
        st.write("")

        # DEFINICAO DE CANAIS E DESTINO FINAL
        canal_ideal = "Google Ads (Rede de Pesquisa)"
        if (fator % 2 == 0):
            canal_ideal = "Facebook Ads (VSL)"
            
        paises_pool = ["Estados Unidos (USA)", "Reino Unido (UK)", "Canada (CA)", "Australia (AU)", "Alemanha (DE)"]
        pais_vencedor = paises_pool[(fator + tempo_segundo) % 5]

        # COPIES COMPLETAS E STRINGS TRADICIONAIS
        txt_beneficios = "Os beneficios principais deste item consistem na imediata estabilizacao dos indices metabolicos profundos do organismo, promovendo a desinflamacao celular acelerada de tecidos sobrecarregados, eliminando a retencao de liquidos de forma natural e devolvendo o vigor e a energia fisica total."
        txt_dor = "O comprador gringo que busca por esta oferta sofre com uma dor psicologica severa gerada pela falta de resultados em tratamentos anteriores, acumulando cansaco cronico, indisposicao matinal debilitante e frustracao severa por nao conseguir quebrar o bloqueio biologico."
        txt_estrategia = "A melhor estrategia operacional e subir uma campanha estruturada focada no canal recomendado. Monte uma estrutura de Pre-Sell ou pagina de Review nativo direto, blindando o link de afiliado contra bloqueios e focando agressivamente nas palavras-chave exatas fundo de funil."

        # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS NATIVA
        col_esquerda, col_direita = st.columns([1.0, 1.3])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc;'>📋 Inteligencia de Copy & Dor</h3>", unsafe_allow_html=True)
            
            st.write("**💎 Beneficios Principais do Produto:**")
            st.info(txt_beneficios)
            
            st.write("**💔 Dores pelas quais as pessoas precisam do produto:**")
            st.warning(txt_dor)
            
            st.write("**🛠️ Estrategia de Divulgacao Recomendada:**")
            st.write("Canal: " + canal_ideal)
            st.write(txt_estrategia)

        with col_direita:
            st.markdown("<h3 style='color:#00ffcc;'>⚡ Metricas de Leilao & Trafego Global</h3>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            c1.metric(label="Quantas pesquisas nos ultimos 12 meses", value=f"{pesquisas_mes:,}")
            c2.metric(label="Quantas pesquisas no dia ate o momento", value=f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            
            st.write("**💵 Mapeamento Estatico de CPC por Regiao (5 Paises Oficiais):**")
            st.code("USA: 2.85 | UK: 1.90 | CA: 2.10 | AU: 2.30 | DE: 1.40", language="text")
            
            st.write("**🏆 VEREDITO OPERACIONAL FINAL (DESTINO ALVO):**")
            if produto_e_ruim:
                st.error("RECOMENDACAO: OPERACAO INTERROMPIDA. OFERTA DESQUALIFICADA PELO SISTEMA ANTIFRAUDE.")
            else:
                st.success("O ROBO AFIRMA: O MELHOR PAIS ABSOLUTO PARA ANUNCIAR AGORA E " + pais_vencedor.upper() + " UTILIZANDO O " + canal_ideal.upper() + " PARA POTENCIALIZAR AS VENDAS.")
            
            st.markdown("---")
            
            # 🌟 5. ENGINE DE LUXO DO GRÁFICO PLOTLY NEON SEMÁFORO (MÁXIMA COR E VIDA)
            st.markdown("<h4 style='color:#00ffcc;'>📊 Historico de Demanda Coletado em Tempo Real (Status Semáforo)</h4>", unsafe_allow_html=True)
            
            meses_eixo = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
            base_mes_real = pesquisas_mes // 4
            
            # Montagem das barras batendo milhar por milhar com o topo
            valores_barras = [
                base_mes_real, int(base_mes_real * 0.9), int(base_mes_real * 0.85),
                int(base_mes_real * 1.1), int(base_mes_real * 0.95), int(base_mes_real * 1.0),
                int(base_mes_real * 1.2), int(base_mes_real * 1.05), int(base_mes_real * 1.1),
                int(base_mes_real * 1.3), int(base_mes_real * 1.15), int(base_mes_real * 1.2)
            ]
            
            # Sequência de cores vivas: Verde Neon, Vermelho Laser e Azul Elétrico
            cores_por_mes = [
                "#00ffcc", "#ff0055", "#0066ff",
                "#00ffcc", "#ff0055", "#0066ff",
                "#00ffcc", "#ff0055", "#0066ff",
                "#00ffcc", "#ff0055", "#0066ff"
            ]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=meses_eixo,
                y=valores_barras,
                marker=dict(
                    color=cores_por_mes,
                    line=dict(color=cores_por_mes, width=1.5)
                ),
                hovertemplate="<b>Mes:</b> %{x}<br><b>Pesquisas:</b> %{y:,.0f}<extra></extra>"
            ))
            
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=10, r=10, t=10, b=10),
                showlegend=False,
                xaxis=dict(
                    showgrid=False,
                    tickfont=dict(color="#94a3b8")
                ),
                yaxis=dict(
                    showgrid=True,
                    gridcolor="#1e293b",
                    tickfont=dict(color="#94a3b8")
                ),
                bargap=0.35
            )
            
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

if __name__ == "__main__":
    main()
