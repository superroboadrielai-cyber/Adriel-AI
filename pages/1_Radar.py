import streamlit as st

def main():
    st.set_page_config(page_title="Gerador de Anuncios - AdrielAI", page_icon="✍️", layout="wide")

    st.title("✍️ GERADOR DE ANUNCIOS BLINDADOS GOOGLE ADS")
    st.write("Criação de titulos e descricoes com limitadores exatos de caracteres anti-reprovação.")
    st.markdown("---")

    ofertas_gringas = ["Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", "Sugar Defender"]
    col_input, col_output = st.columns([1.1, 1.2])

    with col_input:
        st.subheader("⚙️ Terminal de Configuração da Cópia")
        produto_selecionado = st.selectbox("🎯 Selecione a Oferta Alvo:", ofertas_gringas)
        angulo_venda = st.radio("💎 Escolha o Ângulo:", ["Official Website Focus", "Discount Coupon", "Scientific Discovery"])

    with col_output:
        st.subheader("⚡ Central de Pecas Publicitarias Prontas")
        
        if produto_selecionado == "Alpilean":
            t1, t2, t3 = "Alpilean Official Website", "Save 80% on Alpilean Today", "Buy Alpilean Official Store"
            d1 = "Alpilean Secret Alpine Method to Target Low Core Body Temperature. Buy Now and Save Big."
            d2 = "Get Alpilean from Official Site. Secure Payment, Fast Shipping and Full Money Back."
        else:
            t1, t2, t3 = f"{produto_selecionado} Official Website", f"Buy {produto_selecionado} Today", f"Special Discount Active Now"
            d1 = f"Get Original {produto_selecionado} from the Official Site. Safe Order with Full Refund."
            d2 = f"Exclusive Promo Available on {produto_selecionado} Packs. Order Safely Online Today."

        st.write("### 📌 Titulos (Maximo 30 Caracteres):")
        st.text_input("Titulo 1", value=t1, key="t1_key")
        st.caption(f"Caracteres: {len(t1)}/30")
        st.text_input("Titulo 2", value=t2, key="t2_key")
        st.caption(f"Caracteres: {len(t2)}/30")

        st.markdown("---")
        st.write("### 📝 Descricoes (Maximo 90 Caracteres):")
        st.text_area("Descricao 1", value=d1, key="d1_key", height=70)
        st.caption(f"Caracteres: {len(d1)}/90")

if __name__ == "__main__":
    main()
