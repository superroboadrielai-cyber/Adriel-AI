import random
import streamlit as str  # Alterado o alias para evitar conflito com a variável 'st'

# Configuração da página do Streamlit
str.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# Estilização interna para manter o visual escuro e premium
str.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    h1, h2, h3 { color: #ffffff !important; font-family: sans-serif; }
    div[data-testid="stMetricValue"] { color: #f59e0b !important; }
    .hostinger-box {
        background-color: #064e3b; padding: 20px; border-radius: 12px;
        border: 1px solid #047857; text-align: center; margin-top: 25px;
    }
    .hostinger-btn {
        background-color: #10b981; color: white !important; padding: 12px 24px;
        border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

str.title("📊 Radar de Produtos & Lançamentos da Gringa")
str.write("Análise de movimentação de mercado em tempo real para afiliados e produtores.")

# Banco de dados de produtos da gringa
PRODUCTS_DB = [
    {"name": "Alpilean", "platform": "ClickBank", "type": "Evergreen"},
    {"name": "Puravive", "platform": "ClickBank", "type": "Evergreen"},
    {"name": "Java Burn", "platform": "BuyGoods", "type": "Evergreen"},
    {"name": "GlucoTrust", "platform": "ClickBank", "type": "Evergreen"},
    {"name": "Sugavita Med", "platform": "Digistore24", "type": "Lançamento"},
    {"name": "Keto Drops Pro", "platform": "Hotmart Global", "type": "Lançamento"},
    {"name": "ProDentim", "platform": "ClickBank", "type": "Evergreen"},
    {"name": "Liv Pure", "platform": "ClickBank", "type": "Evergreen"},
    {"name": "Ikaria Lean Belly Juice", "platform": "ClickBank", "type": "Evergreen"},
    {"name": "ZenCortex", "platform": "BuyGoods", "type": "Lançamento"}
]

# Simulação de processamento de mercado em tempo real
produtos_processados = []
lista_copia = PRODUCTS_DB.copy()
random.seed()  # Reseta o gerador para garantir novos números a cada recarga

for index, prod in enumerate(lista_copia):
    is_top_10 = index < 10
    status = "🔥 ALTA" if is_top_10 else "✅ NORMAL"
    
    searches_month = random.randint(15000, 120000) if is_top_10 else random.randint(1500, 12000)
    searches_today = random.randint(300, 2500) if is_top_10 else random.randint(20, 300)
    
    paises = ["USA", "UK", "Canada", "Australia", "Germany"]
    melhor_pais = "USA" if is_top_10 else random.choice(paises)
    
    produtos_processados.append({
        "ranking": index + 1,
        "nome": prod["name"],
        "plataforma": prod["platform"],
        "tipo": prod["type"],
        "status": status,
        "buscas_mes": searches_month,
        "buscas_hoje": searches_today,
        "melhor_pais": melhor_pais
    })

# Layout em duas colunas: Lista na Esquerda e Análise Detalhada na Direita
col_esquerda, col_direita = str.columns([1, 2])

with col_esquerda:
    str.subheader("Tabela de Monitoramento")
    
    # Cria botões interativos para cada produto da lista
    for p in produtos_processados:
        label_botao = f"#{p['ranking']} - {p['nome']} ({p['status']})"
        if str.button(label_botao, key=f"btn_{p['nome']}", use_container_width=True):
            str.session_state.produto_selecionado = p

with col_direita:
    str.subheader("🛡️ Auditoria do Produto Selecionado")
    
    # Verifica se o usuário clicou em algum produto
    if "produto_selecionado" in str.session_state:
        p_sel = str.session_state.produto_selecionado
        
        str.markdown(f"## {p_sel['nome']}")
        str.caption(f"Plataforma: {p_sel['plataforma']} | Tipo: {p_sel['type']}")
        
        # Métricas em caixas separadas
        c1, c2, c3 = str.columns(3)
        c1.metric("Buscas no Mês", f"{p_sel['buscas_mes']:,}")
        c2.metric("Buscas Hoje", f"{p_sel['buscas_hoje']:,}")
        c3.metric("Melhor País", p_sel['melhor_pais'])
        
        # Gráfico de tendência solicitado na estrutura
        str.markdown("### 📈 Tendência de Pesquisas (Últimos 12 Meses)")
        dados_grafico = [random.randint(10, 100) for _ in range(12)]
        str.line_chart(dados_grafico)
        
        # Fabricante de Pré-Sell embutido com o seu link de afiliado
        str.markdown(f"""
            <div class="hostinger-box">
                <h3>🌐 Fabricante de Pré-Sell obrigatório</h3>
                <p>Para o produto <b>{p_sel['nome']}</b> converter na gringa sem bloqueios do Google Ads, você precisa de um domínio próprio profissional de alta velocidade.</p>
                <a class="hostinger-btn" href="https://hostinger.com" target="_blank">👉 Registrar Estrutura na Hostinger</a>
            </div>
        """, unsafe_allow_html=True)
    else:
        str.info("Clique em um produto da lista ao lado para abrir o gráfico e a análise de mercado em tempo real.")
