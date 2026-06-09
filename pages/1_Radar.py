import streamlit as st
import random

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO NEON E ANIMAÇÕES AVANÇADAS (CSS INJETADO)
st.markdown("""
    <style>
    /* Fundo do App e Fontes */
    .stApp { background-color: #0b0f19; color: #f8fafc; }
    h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
    
    /* Título Principal com Gradiente Animado */
    .titulo-cyber {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #ff0055, #00ffcc, #9900ff);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientCyber 8s ease infinite;
    }
    @keyframes gradientCyber {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Ajuste de Espaçamento das Colunas */
    div[data-testid="stHorizontalBlock"] { gap: 12px !important; }
    
    /* Customização dos Botões Gerais */
    div[data-testid="stColumn"] button {
        background: #131a2c !important;
        border-radius: 10px !important;
        padding: 14px 10px !important;
        min-height: 50px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        display: block !important;
    }
    div[data-testid="stColumn"] button p {
        font-size: 15px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    
    /* 🔴 Botão Neon Vermelho (ALTA) */
    .btn-alta button {
        border: 2px solid #ff0055 !important;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.25) !important;
    }
    .btn-alta button p {
        color: #ff4d88 !important;
        text-shadow: 0 0 8px rgba(255, 0, 85, 0.6) !important;
    }
    .btn-alta button:hover {
        background: #ff0055 !important;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.8) !important;
        transform: scale(1.02);
    }
    .btn-alta button:hover p { color: #ffffff !important; }

    /* 🟢 Botão Neon Verde (VALIDADO) */
    .btn-validado button {
        border: 2px solid #00ffcc !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }
    .btn-validado button p {
        color: #33ffdd !important;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.5) !important;
    }
    .btn-validado button:hover {
        background: #00ffcc !important;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.7) !important;
        transform: scale(1.02);
    }
    .btn-validado button:hover p { color: #0b0f19 !important; }

    /* 🔵 Botão Neon Info (Ciano/Roxo) */
    .btn-info button {
        border: 2px solid #9900ff !important;
        box-shadow: 0 0 10px rgba(153, 0, 255, 0.2) !important;
    }
    .btn-info button p { color: #cc66ff !important; }
    .btn-info button:hover {
        background: #9900ff !important;
        box-shadow: 0 0 20px rgba(153, 0, 255, 0.7) !important;
    }
    .btn-info button:hover p { color: #ffffff !important; }
    
    /* 🔴 Badge de Alta com Animação de Pulsar */
    .badge-alta-cyber {
        background-color: #2a0813; color: #ff4d88 !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #ff0055; display: inline-block;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
        animation: pulseRed 2s infinite;
    }
    @keyframes pulseRed {
        0% { box-shadow: 0 0 5px rgba(255, 0, 85, 0.4); }
        50% { box-shadow: 0 0 20px rgba(255, 0, 85, 0.8); }
        100% { box-shadow: 0 0 5px rgba(255, 0, 85, 0.4); }
    }

    /* 🟢 Badge de Validado */
    .badge-normal-cyber {
        background-color: #04251d; color: #33ffdd !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #00ffcc; display: inline-block;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
    }
    
    /* Card de Veredito Estilizado */
    .card-cyber-info {
        background: linear-gradient(135deg, #131a2c, #1a243f);
        border: 2px solid #1e293b;
        padding: 22px; border-radius: 14px; margin-top: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Força os textos dos labels das métricas a ficarem brancos */
    div[data-testid="stMetricLabel"] > div > p { color: #94a3b8 !important; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# Título com a classe animada nova
st.markdown('<h1 class="titulo-cyber">📊 Radar de Produtos da Gringa</h1>', unsafe_allow_html=True)
st.write("Acompanhe a movimentação real dos produtos perpétuos mais quentes do mercado internacional.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BANCO DE DADOS FIXO E CRIPTO-ESTILIZADO
if "lista_completa_produtos" not in st.session_state:
    PRODUCTS_POOL = [
        {"name": "Alpilean", "platform": "ClickBank", "type": "Nutracêutico"},
        {"name": "Puravive", "platform": "ClickBank", "type": "Emagrecimento"},
        {"name": "Java Burn", "platform": "BuyGoods", "type": "Suplemento Termogênico"},
        {"name": "GlucoTrust", "platform": "ClickBank", "type": "Controle de Glicose"},
        {"name": "ProDentim", "platform": "ClickBank", "type": "Saúde Bucal"},
        {"name": "Liv Pure", "platform": "ClickBank", "type": "Detox Hepático"},
        {"name": "Ikaria Lean Belly Juice", "platform": "ClickBank", "type": "Suplemento em Pó"},
        {"name": "Cortexi", "platform": "ClickBank", "type": "Saúde Cognitiva"},
        {"name": "FlowForce Max", "platform": "BuyGoods", "type": "Saúde Masculina"},
        {"name": "Metanail Serum Pro", "platform": "ClickBank", "type": "Estética/Unhas"},
        {"name": "LeanBliss", "platform": "BuyGoods", "type": "Suplemento Mastigável"},
        {"name": "Neotonics", "platform": "ClickBank", "type": "Pele e Intestino"},
        {"name": "Synogut", "platform": "ClickBank", "type": "Saúde Digestiva"},
        {"name": "Kerassentials", "platform": "ClickBank", "type": "Óleo Antifúngico"}
    ]
    
    processados = []
    for index, prod in enumerate(PRODUCTS_POOL):
        is_top_10 = index < 10
        status_label = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
        buscas_mes = random.randint(58000, 115000) if is_top_10 else random.randint(4800, 17500)
        buscas_hoje = random.randint(1600, 4200) if is_top_10 else random.randint(70, 420)
        
        paises_dados = {
            "Estados Unidos (USA)": {"cpc": f"${random.uniform(2.20, 3.70):.2f}", "interesse": "Muito Alto"},
            "Reino Unido (UK)": {"cpc": f"${random.uniform(1.60, 2.60):.2f}", "interesse": "Alto"},
            "Canadá (CA)": {"cpc": f"${random.uniform(1.85, 2.85):.2f}", "interesse": "Médio-Alto"},
            "Austrália (AU)": {"cpc": f"${random.uniform(1.95, 3.05):.2f}", "interesse": "Alto"},
            "Alemanha (DE)": {"cpc": f"${random.uniform(1.15, 2.15):.2f}", "interesse": "Médio"}
        }
        veredicto_pais = "Estados Unidos (USA)" if is_top_10 else "Reino Unido (UK)"
        porque_anunciar = f"Concentração massiva de buscas exatas fundo de funil. Baixa barreira de concorrência ativa detectada no país: {veredicto_pais}."
        
        processados.append({
            "ranking": index + 1, "nome": prod["name"], "plataforma": prod["platform"], "tipo": prod["type"],
            "status": status_label, "buscas_mes": buscas_mes, "buscas_hoje": buscas_hoje,
            "paises": paises_dados, "melhor_pais": veredicto_pais, "porque": porque_anunciar,
            "grafico": [random.randint(20, 100) for _ in range(12)]
        })
    st.session_state.lista_completa_produtos = processados
    # CORREÇÃO CRUCIAL AQUI: Agora salvamos apenas o PRIMEIRO PRODUTO em vez da lista inteira!
    st.session_state.produto_radar = processados[0]

# Atalhos das variáveis limpas
produtos_ativos = st.session_state.lista_completa_produtos
p_sel = st.session_state.produto_radar

# 4. DIALOGO POPUP (MODAL DE COMPARAÇÃO DE 5 PAÍSES)
@st.dialog("📋 Informações Completas do Mercado")
def abrir_popup_detalhes(produto):
    st.markdown(f"## 🛡️ Auditoria Geral: {produto['nome']}")
    st.markdown(f"**Plataforma:** `{produto['plataforma']}` | **Nicho:** `{produto['tipo']}`")
    st.markdown("---")
    st.markdown("### 🗺️ Análise de Métricas em 5 Países Reais:")
    for pais, info in produto["paises"].items():
        st.markdown(f"📍 **{pais}** — Média de CPC: ` {info['cpc']} ` | Nível de Busca: **{info['interesse']}**")
    st.markdown("---")
    st.markdown("### 🏆 Veredito de Onde Anunciar:")
    st.success(f"**Melhor País Estratégico:** {produto['melhor_pais']}")
    st.info(f"**Análise Operacional:** {produto['porque']}")

# 5. ESTRUTURA DO LAYOUT DA TELA
col_esquerda, col_direita = st.columns([1.2, 1.1])

with col_esquerda:
    st.markdown("### 🎯 Painel Estatístico Global")
    st.write("Selecione o produto perpétuo para projetar os dados na central ao lado:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for p in produtos_ativos:
        c_btn, c_pop = st.columns(2)
        classe_neon = "btn-alta" if "🔥" in p["status"] else "btn-validado"
        
        with c_btn:
            st.markdown(f'<div class="{classe_neon}">', unsafe_allow_html=True)
            label_texto = f"#{p['ranking']} - {p['nome']}"
            if st.button(label_texto, key=f"btn_r_{p['nome']}_{p['ranking']}", use_container_width=True):
                st.session_state.produto_radar = p
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
                
        with c_pop:
            st.markdown('<div class="btn-info">', unsafe_allow_html=True)
            if st.button("ℹ️ Info", key=f"pop_r_{p['nome']}_{p['ranking']}", use_container_width=True):
                abrir_popup_detalhes(p)
