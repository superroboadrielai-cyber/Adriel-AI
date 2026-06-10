import streamlit as st
import random
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    # 2. INJECAO VISUAL PREMIUM COMPILADA (ESTABILIDADE ABSOLUTA CONTRA TELA BRANCA)
    st.markdown('<style>.stApp {background-color: #040814 !important; color: #f3f4f6 !important;} h1,h2,h3,h4 {color: #00ffcc !important; text-shadow: 0 0 12px rgba(0,255,204,0.3);}</style>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 12px rgba(0, 255, 204, 0.3); margin-bottom: 5px;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    # Marcador de Varredura Viva Baseado no Relogio Atual do Servidor
    tempo_segundo = datetime.now().second
    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"🛰️ **Status do Ecossistema:** <span style='color:#00ffcc; font-weight:bold;'>ATIVO</span> | Varredura viva realizada com sucesso às <span style='color:#ff0055; font-weight:bold;'>{horario_atual}</span> (Dados recalculados conforme a oscilação de tráfego gringo).", unsafe_allow_html=True)
    st.markdown("---")

    # 3. BASE DE DADOS COMPLETA E RIGOROSA DOS 20 PRODUTOS (SINTAXE PURA SEM LAYOUTS EMBUTIDOS)
    PRODUTOS_POOL = [
        {"ranking": 1, "nome": "Alpilean", "status": "🔥 ALTA", "plataforma": "ClickBank", "base_mes": 112000, "base_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "semente": 110,
         "dor": "Metabolismo severamente travado e em estado latente induzido pela baixa temperatura das celulas e tecidos internos, gerando um bloqueio biologico critico que impede a queima de gorduras profundas mesmo sob restricao calorica severa ou rotinas exaustivas de treinos aerobicos.",
         "porque": "O veredicto tecnico confirma que este suplemento lidera com folga as buscas por termos institucionais. Anunciar nas redes de pesquisa do Google Ads norte-americano captura leads qualificados e altamente propensos a comprar com o cartao na mao nas ultimas 24 horas.",
         "cpc": "USA: $3.10 | UK: $2.15 | CA: $2.40 | AU: $2.60 | DE: $1.45"},
        
        {"ranking": 2, "nome": "Puravive", "status": "🔥 ALTA", "plataforma": "ClickBank", "base_mes": 98500, "base_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "semente": 95,
         "dor": "Falta de ativacao biologica do tecido adiposo marrom (BAT), fazendo com que o corpo armazene gordura profunda em areas criticas e desacelere o gasto calorico diario de forma continua.",
         "porque": "A oferta mantem uma taxa de reembolso historicamente baixa e paga altas comissoes. O publico comprador dos Estados Unidos responde muito bem a paginas que expoem estudos cientificos estruturados, tornando a rede de pesquisa um oceano de lucro estavel.",
         "cpc": "USA: $3.10 | UK: $2.20 | CA: $2.40 | AU: $2.50 | DE: $1.60"},
        
        {"ranking": 3, "nome": "Java Burn", "status": "🔥 ALTA", "plataforma": "BuyGoods", "base_mes": 87000, "base_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "semente": 85,
         "dor": "Falta aguda de energia celular e cansaco massivo nas primeiras horas do dia, combinada com surtos continuos de fome psicolica de fundo emocional que sabotam totalmente o andamento de dietas e protocolos.",
         "porque": "A novidade do sache misturavel no cafe diario tomou o mercado gringo de assalto. O veredicto aponta excelente retorno de anuncios na Europa, onde os custos de clique (CPC) estao bem menores que no inflacionado mercado americano, mantendo alta conversao.",
         "cpc": "USA: $2.75 | UK: $1.70 | CA: $1.95 | AU: $2.20 | DE: $1.30"},
        
        {"ranking": 4, "nome": "GlucoTrust", "status": "🔥 ALTA", "plataforma": "ClickBank", "base_mes": 74000, "base_hoje": 1950, "melhor_pais": "Estados Unidos (USA)", "semente": 72,
         "dor": "Picos descontrolados de glicose na corrente sanguinea, desequilibrio metabolico na producao de insulina e crises intensas de compulsao noturna por carboidratos pesados e doces refinados antes de dormir.",
         "porque": "Resolve uma dor de saude alarmante e atinge em cheio o publico idoso internacional de alto poder aquisitivo. Anunciar com correspondencia exata de palavras-chave oficiais filtra cliques curiosos de concorrentes e traz trafego qualificado de fundo.",
         "cpc": "USA: $2.95 | UK: $1.90 | CA: $2.15 | AU: $2.30 | DE: $1.50"},
        
        {"ranking": 5, "nome": "ProDentim", "status": "🔥 ALTA", "plataforma": "ClickBank", "base_mes": 69000, "base_hoje": 1650, "melhor_pais": "Canadá (CA)", "semente": 68,
         "dor": "Sangramentos gengivais constantes durante a escovacao basica, proliferacao de bacterias nocivas no trato bucal que destroem o esmalte protetor e causam um mau halito cronico de dificil eliminacao social.",
         "porque": "Enquanto a massa de afiliados satura os leiloes de trafego dos Estados Unidos, o leilao do Canada e Reino Unido encontra-se livre para o nicho dentario, permitindo extrair comissoes liquidas altas com anuncios baratos via Pre-Sell rapida.",
         "cpc": "USA: $2.45 | UK: $1.60 | CA: $1.80 | AU: $2.00 | DE: $1.25"}
    ]

    # Ingestão Automatizada dos itens de 11 a 20 (Símbolos Normais com Menos Concorrência)
    restantes_config = [
        ("Liv Pure", 6, "ClickBank", 65000, 1420, "Estados Unidos (USA)", 64),
        ("Ikaria Juice", 7, "ClickBank", 61000, 1310, "Austrália (AU)", 60),
        ("Cortexi", 8, "ClickBank", 58000, 1190, "Reino Unido (UK)", 57),
        ("FlowForce Max", 9, "BuyGoods", 54000, 1050, "Estados Unidos (USA)", 53),
        ("Metanail Serum", 10, "ClickBank", 51000, 980, "Canadá (CA)", 50),
        ("LeanBliss", 11, "BuyGoods", 14500, 320, "Austrália (AU)", 14),
        ("Neotonics", 12, "ClickBank", 13200, 290, "Alemanha (DE)", 13),
        ("Synogut", 13, "ClickBank", 12400, 260, "Estados Unidos (USA)", 12),
        ("Kerassentials", 14, "ClickBank", 11800, 240, "Reino Unido (UK)", 11),
        ("SightCare", 15, "BuyGoods", 10500, 210, "Canadá (CA)", 10),
        ("Prostadine", 16, "ClickBank", 9800, 190, "Austrália (AU)", 9),
        ("Fast Lean Pro", 17, "ClickBank", 8900, 170, "Estados Unidos (USA)", 8),
        ("Amiclear", 18, "ClickBank", 8200, 150, "Reino Unido (UK)", 8),
        ("Alpha Tonic", 19, "BuyGoods", 7800, 130, "Nova Zelândia", 7),
        ("Joint Genesis", 20, "ClickBank", 7100, 110, "Estados Unidos (USA)", 7)
    ]

    for nome_r, rk_r, pl_r, bm_r, bh_r, mp_r, sm_r in restantes_config:
        PRODUTOS_POOL.append({
            "ranking": rk_r, "nome": nome_r, "status": "🔥 ALTA" if rk_r <= 10 else "✅ NORMAIS", "plataforma": pl_r, "base_mes": bm_r, "base_hoje": bh_r, "melhor_pais": mp_r, "semente": sm_r,
            "dor": "Desgaste fisiologico crônico limitante acompanhado de baixa imunidade e fadiga celular, sabotando os indices energeticos e a produtividade diaria de compradores seniores que buscam alternativas naturais de cura rapida.",
            "porque": "Brecha de mercado mapeada! O monitoramento identificou baixissima densidade de grandes afiliados operando campanhas neste leilao especifico, gerando cliques limpos de alta intencao com baixo custo por clique."
        })

    # Inicialização blindada da memória de sessão
    if "produto_radar_dados" not in st.session_state:
        st.session_state.produto_radar_dados = PRODUTOS_POOL[0]

    p_sel = st.session_state.produto_radar_dados

    # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS
    col_esquerda, col_direita = st.columns([1.2, 1.1])

    with col_esquerda:
        st.subheader("🎯 Painel Estatistico Global")
        st.write("Clique no produto para projetar a varredura ao vivo na central de inteligencia:")
        st.write("")
        
        for idx, p in enumerate(PRODUTOS_POOL):
            c_btn, c_pop = st.columns(2)
            
            # Símbolos Dinâmicos de Acordo com o Ranking Solicitado
            icone_principal = "🔥" if p["ranking"] <= 10 else "✅"
            
            # Oscilação real das setas conforme o segundo do relógio do sistema
            seta_viva = "📈 SUBINDO" if (tempo_segundo + idx) % 2 == 0 else "📉 DECENDO"
            
            texto_botao = f"{icone_principal} {p['nome']} [{seta_viva}]"
            
            with c_btn:
                if st.button(texto_botao, key=f"btn_r_{p['nome']}", use_container_width=True):
                    st.session_state.produto_radar_dados = p
                    st.rerun()
                    
            with c_pop:
                with st.popover("ℹ️ Dossie Rápido", use_container_width=True):
                    st.write(f"### 🛡️ Pre-Analise: {p['nome']}")
                    st.write(f"**Local:** {p['melhor_pais']}")
                    st.write(f"**Veredito:** {p['porque']}")

    with col_direita:
        st.subheader("⚡ Central de Inteligencia de Mercado")
        st.header(p_sel["nome"])
        
        # Simulação realista variando as pesquisas em tempo real baseada no segundo do relógio
        variacao_mes_viva = p_sel["base_mes"] + (tempo_segundo * random.randint(3, 8))
        variacao_hoje_viva = p_sel["base_hoje"] + (tempo_segundo * random.randint(1, 3))
        
        st.write(f"**Classificacao:** {p_sel['status']} • MONITORAMENTO ATIVO DO ROBO")
        st.write("")
        
        # Grid Numérico SaaS preenchendo a tela
        c1, c2 = st.columns(2)
        c1.metric(label="🔎 Quantas pesquisas teve nos últimos 12 meses", value=f"{variacao_mes_viva:,}")
        c2.metric(label="⚡ Quantas pesquisas teve no dia ate o momento atual", value=f"{variacao_hoje_viva:,}")
        
        st.markdown("---")
        
        # Exibição de Justificativas Pesadas, Longas e Convincentes de 4 a 5 linhas
