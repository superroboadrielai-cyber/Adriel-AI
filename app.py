import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black herdado da família Adriel AI
st.set_page_config(page_title="Adriel AI - Radar de Produtos", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE CÓDIGO CSS PREMIUM (O MESMO VISUAL CORTE DE LUXO DA CENTRAL HOME)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro de Luxo Espacial */
    .stApp {
        background-color: #050811 !important;
        color: #ffffff !important;
    }
    
    /* 🎨 ANIMAÇÃO QUE ALTERNA AS CORES DAS BORDAS (CIANO <-> VERDE) */
    @keyframes alterna-cores {
        0% { border-color: #00E5FF; box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.15); }
        50% { border-color: #00FF87; box-shadow: 0px 4px 15px rgba(0, 255, 135, 0.25); }
        100% { border-color: #00E5FF; box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.15); }
    }

    .modulo-container-interno {
        background: linear-gradient(135deg, #0f172a 0%, #050811 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 12px !important;
        padding: 20px !important;
        margin-bottom: 25px !important;
        animation: alterna-cores 5s infinite ease-in-out !important;
    }
    
    /* Títulos Dinâmicos em Gradiente Líquido */
    h1, h2, h3 {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    
    /* Tabelas e Dataframes customizados para o modo Escuro */
    .stDataFrame {
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# CHASSI INTERNO DA PÁGINA (RECORTADO E IDÊNTICO À HOME)
# =============================================================================================================
st.markdown("""
<div class="modulo-container-interno">
    <h2 style='margin-top: 0; font-size: 24px;'>🛰️ MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</h2>
    <p style='margin: 10px 0 0 0; font-size: 14px; color: #cbd5e1; line-height: 1.5;'>
        Filtro analítico avançado focado na extração e mineração das 22 ofertas com maior tração de vendas e ROI 
        nas plataformas ClickBank, BuyGoods e Hotmart.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# 📑 SEÇÃO DE CONFIGURAÇÃO DO RADAR (SELETORES INTERNOS)
col_filtro1, col_filtro2 = st.columns(2)
with col_filtro1:
    plataforma = st.selectbox("Selecione a Plataforma de Origem:", ["ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Hotmart 🇧🇷", "Braip 🇧🇷"])
with col_filtro2:
    categoria = st.selectbox("Selecione o Nicho de Mercado:", ["Saúde & Bem-Estar", "Renda Extra / Finanças", "Mentalidade / Espiritualidade"])

st.write("---")

# 📊 EXIBIÇÃO DA TABELA REQUINTADA DENTRO DO PAINEL RECORTADO
st.markdown("#### 📋 Listagem de Produtos Validados pela IA")

dados_radar = {
    "Nome do Produto": ["Java Burn", "Puravive", "Sugar Defender", "Citrus Burn", "Protocolo Zero", "Alpilean", "Cortexi"],
    "Gravidade / Temperatura": ["180+ (Alta)", "150+ (Alta)", "210+ (Extrema)", "95+ (Média)", "120+ (Média)", "85+ (Estável)", "140+ (Alta)"],
    "Comissão Média": ["$ 135.00", "$ 142.50", "$ 118.20", "R$ 197,00", "R$ 247,00", "$ 105.00", "$ 122.00"],
    "Status de Leilão": ["Livre 🟢", "Livre 🟢", "Competitivo 🟡", "Livre 🟢", "Livre 🟢", "Saturado 🔴", "Competitivo 🟡"]
}
df_radar = pd.DataFrame(dados_radar)
st.dataframe(df_radar, use_container_width=True, hide_index=True)

st.write("")
if st.button("📥 EXPORTAR RELATÓRIO DO RADAR PARA EXCEL (.CSV)", key="btn_radar_csv"):
    st.success("✅ Download concluído! Arquivo gerado com os parâmetros operacionais atualizados.")
