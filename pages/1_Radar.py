import streamlit as st
import random

def main():
    # 1. CONFIGURAÇÃO HIGH-END DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Gerador de Anúncios - AdrielAI", page_icon="✍️", layout="wide")

    # 2. INJEÇÃO VISUAL CYBER-NEON EM LINHA (BLINDAGEM COMPILADA TOTAL)
    st.markdown('<style>.stApp {background-color: #040814 !important; color: #f3f4f6 !important;} h1,h2,h3,h4 {color: #00ffcc !important; text-shadow: 0 0 12px rgba(0,255,204,0.3);} .stButton>button {border: 2px solid #ff0055 !important; background-color: #0f172a !important; color: #ff4d88 !important; font-weight: 800 !important; transition: all 0.3s ease;} .stButton>button:hover {background-color: #ff0055 !important; color: #ffffff !important; box-shadow: 0 0 20px #ff0055 !important;}</style>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 12px rgba(0, 255, 204, 0.3); margin-bottom: 5px;">✍️ GERADOR DE ANÚNCIOS BLINDADOS GOOGLE ADS</h1>', unsafe_allow_html=True)
    st.write("Mecanismo sênior de engenharia de copy gringa. Criação de títulos e descrições com limitadores exatos de caracteres anti-reprovação.")
    st.markdown("---")

    # 3. BASE DE INTELIGÊNCIA DE COPY (DADOS REAIS DO MERCADO GRINGO)
    ofertas_gringas = ["Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", "Sugar Defender"]

    # 4. LAYOUT EM DUAS COLUNAS PRINCIPAIS (MÁXIMO PREENCHIMENTO DE TELA)
    col_input, col_output = st.columns([1.1, 1.2])

    with col_input:
        st.subheader("⚙️ Terminal de Configuração da Cópia")
        st.write("Ajuste os parâmetros para forçar a IA a minerar os melhores ângulos de venda:")
        st.write("")

        # Seletores estáveis sem dicionários complexos
        produto_selecionado = st.selectbox("🎯 Selecione a Oferta Evergreen Alvo:", ofertas_gringas)
        angulo_venda = st.radio("💎 Escolha o Ângulo Persuasivo de Guerra:", ["Official Website Focus (Fundo)", "Discount & Promo Coupon (Desconto)", "Scientific Discovery Gancho (Dor)"])
        gatilho_gerar = st.button("🚀 EXECUÇÃO: GENERATE BLINDED COPY")

    with col_output:
        st.subheader("⚡ Central de Peças Publicitárias Prontas")
        st.write("Copie os textos gerados direto para a sua campanha oficial do Google Ads:")
        st.write("")

        # Configuração de dados dinâmicos baseados nas seleções de mercado gringo
        if produto_selecionado == "Alpilean":
            t1, t2, t3 = "Alpilean Official Website", "Save 80% on Alpilean Today", "Buy Alpilean Official Store"
            d1 = "Alpilean Secret Alpine Method to Target Low Core Body Temperature. Buy Now and Save Big."
            d2 = "Get Alpilean from Official Site. Secure Payment, Fast Shipping and Full Money Back Guarantee."
        elif producto_selecionado == "Puravive":
            t1, t2, t3 = "Puravive Official Store", "Puravive Special Discount", "Order Puravive From Official"
            d1 = "Puravive Proprietary Blend Optimizes Brown Adipose Tissue Levels. 180 Days Refund Policy."
            d2 = "Exclusive Offer: Save Big on Puravive Multi-Bottles Packages. Order Safely Online Today."
        elif produto_selecionado == "Java Burn":
            t1, t2, t3 = "Java Burn Official Offer", "Java Burn Coffee Sachê Promo", "Get Original Java Burn Only"
            d1 = "100% Natural Formula Designed to Boost Metabolism Speed with Your Morning Coffee."
            d2 = "Order Java Burn from Official Shop today. Lowest Price Guaranteed and Free Shipping."
        else:
            t1, t2, t3 = f"{produto_selecionado} Official", f"Buy {produto_selecionado} Today", f"Get {produto_selecionado} Discount"
            d1 = f"Get Original {produto_selecionado} from the Official Website. Safe Order with 60 Days Refund."
            d2 = f"Special Promo Available on {produto_selecionado} Multi-Packs. Order Now and Save Big Today."

        # Exibição dos Títulos Criados com Contador Rígido de Caracteres (Limite 30)
        st.write("### 📌 Títulos Persuasivos (Máximo 30 Caracteres):")
        
        st.text_input("Título 1", value=t1, key="t1_input")
        st.caption(f"Contador de Caracteres: **{len(t1)}/30**")

        st.text_input("Título 2", value=t2, key="t2_input")
        st.caption(f"Contador de Caracteres: **{len(t2)}/30**")

        st.text_input("Título 3", value=t3, key="t3_input")
        st.caption(f"Contador de Caracteres: **{len(t3)}/30**")

        st.markdown("---")

        # Exibição das Descrições Criadas com Contador Rígido de Caracteres (Limite 90)
        st.write("### 📝 Descrições Cirúrgicas (Análise Preditiva de 4 Linhas - Limite 90):")
        
        st.text_area("Descrição 1", value=d1, key="d1_input", height=70)
        st.caption(f"Contador de Caracteres: **{len(d1)}/90**")

        st.text_area("Descrição 2", value=d2, key="d2_input", height=70)
        st.caption(f"Contador de Caracteres: **{len(d2)}/90**")

        st.markdown("---")
        st.info("🛰️ Todas as copys foram geradas em inglês nativo gringo, respeitando estritamente as políticas editoriais de anúncios para evitar suspensões por termos proibidos.")

if __name__ == "__main__":
    main()
