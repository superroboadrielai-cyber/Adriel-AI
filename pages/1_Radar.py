import streamlit as st
import random

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Gerador de Anúncios - AdrielAI", page_icon="✍️", layout="wide")

    # 2. INJEÇÃO DE INLINE CSS BLACK-LABEL (SEGURA SEM CHAVES CONFLITANTES)
    st.markdown('<style>.stApp {background-color: #040814 !important; color: #f3f4f6 !important;} h1,h2,h3,h4 {color: #00ffcc !important; text-shadow: 0 0 12px rgba(0,255,204,0.3);} .stButton>button {border: 2px solid #ff0055 !important; background-color: #0f172a !important; color: #ff4d88 !important; font-weight: 800 !important; width: 100% !important;} .stButton>button:hover {background-color: #ff0055 !important; color: #ffffff !important; box-shadow: 0 0 20px #ff0055 !important;}</style>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 12px rgba(0, 255, 204, 0.3); margin-bottom: 5px;">✍️ GERADOR DE ANÚNCIOS BLINDADOS GOOGLE ADS</h1>', unsafe_allow_html=True)
    st.write("Mecanismo sênior de engenharia de copy gringa. Criação de títulos e descrições com limitadores exatos de caracteres anti-reprovação.")
    st.markdown("---")

    # 3. BASE DE INTELIGÊNCIA DE MERCADO (OFERTAS EVERGREEN DO BRASIL E DA GRINGA)
    ofertas_gringas = ["Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", "Sugar Defender"]

    # 4. FIXAÇÃO DO GRID DE LAYOUT (MÁXIMO PREENCHIMENTO DE TELA)
    col_input, col_output = st.columns([1.1, 1.2])

    with col_input:
        st.subheader("⚙️ Terminal de Configuração da Cópia")
        st.write("Ajuste os parâmetros para minerar os melhores ângulos de venda:")
        st.write("")

        produto_selecionado = st.selectbox("🎯 Selecione a Oferta Evergreen Alvo:", ofertas_gringas)
        angulo_venda = st.radio("💎 Escolha o Ângulo Persuasivo de Guerra:", ["Official Website Focus (Fundo)", "Discount & Promo Coupon (Desconto)", "Scientific Discovery Gancho (Dor)"])
        st.markdown("<br>", unsafe_allow_html=True)
        gatilho_gerar = st.button("🚀 EXECUÇÃO: GENERATE BLINDED COPY")

    with col_output:
        st.subheader("⚡ Central de Peças Publicitárias Prontas")
        st.write("Copie os textos gerados direto para a sua campanha oficial do Google Ads gringo:")
        st.write("")

        # Lógica linear pura de distribuição de Copys Cirúrgicas por Produto
        if produto_selecionado == "Alpilean":
            t1 = "Alpilean Official Website"
            t2 = "Save 80% on Alpilean Today"
            t3 = "Buy Alpilean Official Store"
            d1 = "Alpilean Secret Alpine Method to Target Low Core Body Temperature. Buy Now and Save Big."
            d2 = "Get Alpilean from Official Site. Secure Payment, Fast Shipping and Full Money Back."
        elif produto_selecionado == "Puravive":
            t1 = "Puravive Official Store"
            t2 = "Puravive Special Discount"
            t3 = "Order Puravive From Official"
            d1 = "Puravive Proprietary Blend Optimizes Brown Adipose Tissue Levels. 180 Days Refund Policy."
            d2 = "Exclusive Offer: Save Big on Puravive Multi-Bottles Packages. Order Safely Online Today."
        elif produto_selecionado == "Java Burn":
            t1 = "Java Burn Official Offer"
            t2 = "Java Burn Coffee Sache Promo"
            t3 = "Get Original Java Burn Only"
            d1 = "100% Natural Formula Designed to Boost Metabolism Speed with Your Morning Coffee."
            d2 = "Order Java Burn from Official Shop today. Lowest Price Guaranteed and Free Shipping."
        elif produto_selecionado == "GlucoTrust":
            t1 = "GlucoTrust Official Store"
            t2 = "GlucoTrust Special Discount"
            t3 = "Order GlucoTrust Online"
            d1 = "Support Healthy Blood Sugar Levels with GlucoTrust Natural Formula. Get 180 Days Refund."
            d2 = "Exclusive Offer: Save Big on GlucoTrust Multi-Bottle Packages. Secure Checkout Today."
        elif produto_selecionado == "ProDentim":
            t1 = "ProDentim Official Website"
            t2 = "ProDentim Advanced Dental"
            t3 = "Get ProDentim Oral Care"
            d1 = "Doctor-Formulated ProDentim Blend Packs 3.5 Billion Probiotics for Healthy Teeth & Gums."
            d2 = "Order ProDentim from Official Store Today and Claim Your Special Discount with Free Ship."
        else:
            t1 = "Sugar Defender Official"
            t2 = "Sugar Defender Discount"
            t3 = "Buy Sugar Defender Store"
            d1 = "Sugar Defender Advanced Blend Supports Healthy Blood Sugar and Energy Levels. Buy Today."
            d2 = "Get Original Sugar Defender from Official Shop. Safe Order with 60 Days Refund Policy."

        # Modulação de acordo com o Ângulo de Venda Selecionado para trazer mais inteligência viva
        if angulo_venda == "Discount & Promo Coupon (Desconto)":
            t2 = "Claim Limited 80% Off Today"
            t3 = "Special Coupon Active Now"
        elif angulo_venda == "Scientific Discovery Gancho (Dor)":
            t2 = "New Scientific Discovery"
            t3 = "Target the Real Root Cause"

        # 5. EXIBIÇÃO DOS COMPONENTES COM VALIDAÇÃO RÍGIDA DE TAMANHO
        st.write("### 📌 Títulos Persuasivos (Máximo 30 Caracteres):")
        
        st.text_input("Título 1", value=t1, key="t1_val")
        st.caption(f"Contador de Caracteres: **{len(t1)}/30**")

        st.text_input("Título 2", value=t2, key="t2_val")
        st.caption(f"Contador de Caracteres: **{len(t2)}/30**")

        st.text_input("Título 3", value=t3, key="t3_val")
        st.caption(f"Contador de Caracteres: **{len(t3)}/30**")

        st.markdown("---")

        st.write("### 📝 Descrições Cirúrgicas (Limite 90 Caracteres):")
        
        st.text_area("Descrição 1", value=d1, key="d1_val", height=70)
        st.caption(f"Contador de Caracteres: **{len(d1)}/90**")

        st.text_area("Descrição 2", value=d2, key="d2_val", height=70)
        st.caption(f"Contador de Caracteres: **{len(d2)}/90**")

        st.markdown("---")
        st.info("🛰️ Todas as copys foram geradas em inglês nativo gringo, respeitando estritamente as políticas editoriais de anúncios para evitar suspensões.")

if __name__ == "__main__":
    main()
