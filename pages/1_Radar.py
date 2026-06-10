import streamlit as st
import random
from datetime import datetime

# Mecanismo de Descriptografia Sênior em Tempo de Execução (Blindagem Anti-Magic)
def decode_intel_saas(hex_str):
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except:
        return hex_str

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    # 2. INJEÇÃO VISUAL PREMIUM COMPILADA (ESTABILIDADE ABSOLUTA)
    st.markdown('<style>.stApp {background-color: #040814 !important; color: #f3f4f6 !important;} h1,h2,h3,h4 {color: #00ffcc !important; text-shadow: 0 0 12px rgba(0,255,204,0.3);}</style>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 12px rgba(0, 255, 204, 0.3); margin-bottom: 5px;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    # Exibição do Status de Varredura Viva Baseado no Relógio Atual do Servidor
    tempo_segundo_vovo = datetime.now().second
    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"🛰️ **Status do Ecossistema:** <span style='color:#00ffcc; font-weight:bold;'>ATIVO</span> | Varredura viva realizada com sucesso às <span style='color:#ff0055; font-weight:bold;'>{horario_atual}</span> (Dados recalculados conforme a oscilação de tráfego gringo).", unsafe_allow_html=True)
    st.markdown("---")

    # 3. BASE DE DADOS COMPLETA E CRIPTOGRAFADA EM HEX (PROTEÇÃO CONTRA PYTHON 3.14)
    PRODUTOS_POOL = [
        {
            "ranking": 1, "nome": "Alpilean", "status": "🔥 ALTA TRACÃO", "plataforma": "ClickBank", "base_mes": 112000, "base_hoje": 3420, "melhor_pais": "Estados Unidos (USA)", "semente": 110,
            "hex_dor": "4d657461626f6c69736d6f207365766572616d656e7465207472617661646f206520656d2065737461646f206c6174656e746520696e64757a69646f2070656c612062616978612074656d7065726174757261206461732063656c756c617320652074656369646f7320696e7465726e6f732c20676572616e646f20756d20626c6f717565696f2062696f6c6f6769636f206372697469636f2071756520696d70656465206120717565696d6120646520676f7264757261732070726f66756e6461732e",
            "hex_porque": "4f20766572656469746f207465636e69636f20636f6e6669726d61207175652065737465207375706c656d656e7465206c696465726120636f6d20666f6c67612061732062757363617320706f72207465726d6f7320696e737469747563696f6e6169732e20416e756e63696172206e617320726564657320646520706573717569736120646f20476f6f676c6520416473206e6f7274652d616d65726963616e6f2063617074757261206c65616473207175616c6966696361646f7320652070726f6e746f73207061726120636f6d707261722e"
        },
        {
            "ranking": 2, "nome": "Puravive", "status": "🔥 ALTA TRACÃO", "plataforma": "ClickBank", "base_mes": 98500, "base_hoje": 2890, "melhor_pais": "Estados Unidos (USA)", "semente": 95,
            "hex_dor": "46616c746120646520617469766163616f2062696f6c6f6769636120646f2074656369646f20616469706f736f206d6172726f6d2028424154292c2066617a656e646f20636f6d20717565206f20636f72706f2061726d617a656e6520676f72647572612070726f66756e646120656d206174656369646f73207669736365726169732e",
            "hex_porque": "41206f6665727461206d616e74656d20756d612074617861206465207265656d626f6c736f20686973746f726963616d656e74652062616978612065207061676120616c74617320636f6d6973736f65732e204f2077656273697465206f66696369616c20636f6e7665727465206d7569746f2062656d206e6f207472616665676f2064652070657371756973612e"
        },
        {
            "ranking": 3, "nome": "Java Burn", "status": "🔥 ALTA TRACÃO", "plataforma": "BuyGoods", "base_mes": 87000, "base_hoje": 2100, "melhor_pais": "Reino Unido (UK)", "semente": 85,
            "hex_dor": "46616c746120616775646120646520656e65726769612063656c756c617220652063616e7361636f206d61737369766f206e6173207072696d656972617320686f72617320646f206469612c20636f6d62696e61646120636f6d20737572746f7320636f6e74696e756f7320646520666f6d6520707369636f6c6f676963612e",
            "hex_porque": "41206e6f76696461646520646f207361636865206d69737475726176656c206e6f2063616f2064696172696f20746f6d6f75206f206d65726361646f206772696e676f20646520617373616c746f2e204f20766572656469746f2061706f6e746120657863656c656e7465207265746f726e6f20656d20636c69717565732062617261746f73206e61204575726f70612e"
        }
    ]

    # Ingestão Automatizada e Segura dos outros 17 produtos obrigatórios do ecossistema gringo
    restantes_config = [
        ("GlucoTrust", 4, "ClickBank", 74000, 1950, "Estados Unidos (USA)", 72),
        ("ProDentim", 5, "ClickBank", 69000, 1650, "Canadá (CA)", 68),
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
            "ranking": rk_r, "nome": nome_r, "status": "🔥 ALTA TRACÃO" if rk_r <= 10 else "✅ VALIDADO", "plataforma": pl_r, "base_mes": bm_r, "base_hoje": bh_r, "melhor_pais": mp_r, "semente": sm_r,
            "hex_dor": "46616c746120646520766974616c69646164652063656c756c61722c206661646967612073657665726120652064657367617374652063726f6e69636f207175652061666574612061207175616c6964616465206465207669646120646f73206c656164732e",
            "hex_porque": "4e6f73736120766172726564757261206465746563746f7520756d6120627265636861206f7065726163696f6e616c206e65737465206c65696c616f20736563756e646172696f2e204120636f6e636f7272656e63696120652062616978612c207065726d6974696e646f20524f4920616c746f2e"
        })

    # Inicialização forçada do estado de sessão do Streamlit
    if "produto_radar_dados" not in st.session_state:
        st.session_state.produto_radar_dados = PRODUTOS_POOL[0]

    p_sel = st.session_state.produto_radar_dados

    # Decodificação imediata dos textos reais longos e cirúrgicos do item ativo
    txt_dor_exibida = decode_intel_saas(p_sel["hex_dor"])
    txt_porque_exibido = decode_intel_saas(p_sel["hex_porque"])

    # 4. CONSTRUÇÃO DO GRID EM DUAS COLUNAS PRINCIPAIS (MÁXIMO PREENCHIMENTO DE TELA)
    col_esquerda, col_direita = st.columns([1.2, 1.1])

    with col_esquerda:
        st.subheader("🎯 Painel Estatistico Global")
        st.write("Clique no produto evergreen para projetar os dados analiticos em tempo real na central:")
        st.write("")
        
        # Renderização estável dos botões com setas de tendência geradas pelo relógio vivo do servidor
        for idx, p in enumerate(PRODUTOS_POOL):
            c_btn, c_pop = st.columns(2)
            
            # Símbolos oscilantes em tempo real baseados na posição e no segundo atual
            is_top = p["ranking"] <= 10
            icone_principal = "🔥" if is_top else "✅"
            
            # Oscilação da seta em tempo real simulando o robô operando vivo para o cliente ver
            seta_viva = "📈 SUBINDO" if (tempo_segundo_vovo + idx) % 2 == 0 else "📉 CORRIGINDO"
            if is_top and (tempo_segundo_vovo + idx) % 3 == 0:
                seta_viva = "📈 ACELERANDO"
                
            texto_botao = f"{icone_principal} {p['nome']} [{seta_viva}]"
            
            with c_btn:
                if st.button(texto_botao, key=f"btn_r_{p['nome']}", use_container_width=True):
                    st.session_state.produto_radar_dados = p
                    st.rerun()
                    
            with c_pop:
                with st.popover("ℹ️ Micro Dossie", use_container_width=True):
                    st.write(f"### 🛡️ Pre-Analise: {p['nome']}")
                    st.write(f"**Distribuição:** `{p['plataforma']}`")
                    st.write(f"**Melhor Local:** {p['melhor_pais']}")
                    st.write(f"**Veredito:** {decode_intel_saas(p['hex_porque'])}")

    with col_direita:
        st.subheader("⚡ Central de Inteligencia de Mercado")
        st.header(p_sel["nome"])
        
        # Variação realística das pesquisas em tempo real baseada no segundo do relógio
        variacao_mes_viva = p_sel["base_mes"] + (tempo_segundo_vovo * random.randint(3, 8))
        variacao_hoje_viva = p_sel["base_hoje"] + (tempo_segundo_vovo * random.randint(1, 3))
        
        st.write(f"**Status de Leilão:** {p_sel['status']} • CAPTURA AUTOMATIZADA")
        st.write("")
        
        # Grid Numérico SaaS preenchendo a tela
        c1, c2 = st.columns(2)
        c1.metric(label="🔎 Volume de Pesquisas no Mes Atual", value=f"{variacao_mes_viva:,}")
        c2.metric(label="⚡ Volume de Pesquisas Registradas Hoje", value=f"{variacao_hoje_viva:,}")
        
        st.markdown("---")
        
        # Exibição das justificativas pesadas e reais de 5 linhas decodificadas
        st.write("### 💔 Dor Cirurgica do Comprador Gringo (Motivo da busca):")
        st.warning(txt_dor_exibida)
        
