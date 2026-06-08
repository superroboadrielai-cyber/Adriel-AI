import streamlit as st

# Configuração da página
st.set_page_config(page_title="Ativador", page_icon="⚡")

# Título
st.title("⚡ Ativador")

st.write("Bem-vindo à página de Ativador.")

# Exemplo de conteúdo
if st.button("Executar Ativação"):
    st.write("Iniciando processo de ativação...")
