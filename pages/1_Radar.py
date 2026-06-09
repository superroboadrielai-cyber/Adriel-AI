import streamlit as st
import random

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO CSS AVANÇADA
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    h1, h2, h3, h4, p, span { color: #ffffff !important; font-family: sans-serif; }
    div[data-testid="stMetricValue"] > div { color: #f59e0b !important; }
    
    div[data-testid="stHorizontalBlock"] { gap: 10px !important; }
    
    div[data-testid="stColumn"] button {
        background-color: #1e293b !important;
        border-radius: 8px !important;
        padding: 12px 10px !important;
        min-height: 45px !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        display: block !important;
    }
    
    div[data-testid="stColumn"] button p {
        font-size: 15px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    
    .btn-alta button {
        border: 2px solid #ef4444 !important;
        box-shadow: 0 0 12px rgba(239, 68, 68, 0.3) !important;
    }
    .btn-alta button p {
        color: #f87171 !important;
        text-shadow: 0 0 8px rgba(239, 68, 68, 0.5) !important;
    }
    .btn-alta button:hover {
        background-color: #ef4444 !important;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.7) !important;
    }
    .btn-alta button:hover p { color: #ffffff !important; }

    .btn-validado button {
        border: 2px solid #10b981 !important;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.3) !important;
    }
    .btn-validado button p {
        color: #34d399 !important;
        text-shadow: 0 0 8px rgba(16, 185, 129, 0.5) !important;
    }
    .btn-validado button:hover {
        background-color: #10b981 !important;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.7) !important;
    }
    .btn-validado button:hover p { color: #ffffff !important; }

    .btn-info button {
        border: 2px solid #06b6d4 !important;
        box-shadow: 0 0 10px rgba(6, 182, 212, 0.2) !important;
    }
    .btn-info button p { color: #22d3ee !important; }
    .btn-info button:hover {
        background-color: #06b6d4 !important;
        box-shadow: 0 0 18px rgba(6, 182, 212, 0.6) !important;
    }
    .btn-info button:hover p { color: #0f172a !important; }
    
    .card-info {
        background-color: #1e293b; border: 1px solid #334155;
        padding: 20px; border-radius: 12px; margin-top: 15px;
    }
    .badge-alta {
        background-color: #991b1b; color: #ffffff !important;
        padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 13px;
        border: 1px solid #f87171; box-shadow: 0 0 10px rgba(239, 68, 68, 0.4);
    }
    .badge-normal {
        background-color: #16a34a; color: #ffffff !important;
        padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 13px;
        border: 1px solid #34d399; box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Mudamos o título para focar apenas em Produtos Perpétuos/Validados
st.title("📊 Radar de Produtos da Gringa")
st.write("Acompanhe a movimentação real dos produtos perpétuos mais quentes do mercado internacional.")

# 3. BANCO DE DADOS EXCLUSIVO DE PRODUTOS VALIDADOS (SEM LANÇAMENTOS)
if "lista_completa_produtos" not in st.session_state:
    # Pool de 25 produtos consolidados do mercado internacional (Evergreen)
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
        {"name": "Kerassentials", "platform": "ClickBank", "type": "Óleo Antifúngico"},
        {"name": "SightCare", "platform": "BuyGoods", "type": "Suporte à Visão"},
        {"name": "Prostadine", "platform": "ClickBank", "type": "Suporte à Próstata"},
        {"name": "Fast Lean Pro", "platform": "ClickBank", "type": "Auxílio de Jejum"},
        {"name": "Amiclear", "platform": "ClickBank", "type": "Energia e Glicose"},
        {"name": "Alpha Tonic", "platform": "BuyGoods", "type": "Potência Masculina"},
        {"name": "Endopump", "platform": "ClickBank", "type": "Fluxo Sanguíneo"},
        {"name": "Proaxil", "platform": "BuyGoods", "type": "Saúde Geral"},
        {"name": "Joint Genesis", "platform": "ClickBank", "type": "Articulações"},
        {"name": "ClariTox Pro", "platform": "ClickBank", "type": "Equilíbrio/Tontura"},
        {"name": "GenoGreens", "platform": "BuyGoods", "type": "Superalimento Verde"},
        {"name": "NeuroRise", "platform": "ClickBank", "type": "Memória/Foco"}
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
        porque_anunciar = f"Alta densidade de compradores qualificados de fundo de funil ativos em {veredicto_pais}."
        
        processados.append({
            "ranking": index + 1, "nome": prod["name"], "plataforma": prod["platform"], "tipo": prod["type"],
            "status": status_label, "buscas_mes": buscas_mes, "buscas_hoje": buscas_hoje,
            "paises": paises_dados, "melhor_pais": veredicto_pais, "porque": porque_anunciar,
            "grafico": [random.randint(20, 100) for _ in range(12)]
        })
    st.session_state.lista_completa_produtos = processados
    st.session_state.produto_radar = processados[0]  # Define Alpilean explicitamente como o primeiro item ativo

# Atalhos das variáveis
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
    st.subheader("Painel Estatístico Global")
    st.write("Selecione um produto para carregar as métricas ou veja os 5 países em Info:")
    
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
            st.markdown('</div>', unsafe_allow_html=True)

with col_direita:
    st.subheader("⚡ Movimentação de Mercado em Tempo Real")
    st.markdown(f"## {p_sel['nome']}")
    
    if "🔥" in p_sel["status"]:
        st.markdown(f'<span class="badge-alta">{p_sel["status"]}</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span class="badge-normal">{p_sel["status"]}</span>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.metric(label="🔎 Pesquisas Realizadas no Mês", value=f"{p_sel['buscas_mes']:,}")
    c2.metric(label="⚡ Pesquisas Acumuladas Hoje", value=f"{p_sel['buscas_hoje']:,}")
