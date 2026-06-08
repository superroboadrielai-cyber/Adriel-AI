import streamlit as st

# 1. Configuração da página (deve ser sempre o primeiro comando)
st.set_page_config(
    page_title="Meu Projeto",
    layout="wide"
)

# 2. Conteúdo da página principal
st.title("Bem-vindo ao meu Sistema")
st.write("Se o menu lateral estiver aparecendo, a estrutura está correta!")
st.write("Use o menu à esquerda para navegar entre as páginas.")

# 3. Adicione aqui o que você quer que apareça na página principal
