import streamlit as st

st.set_page_config(page_title="projeto Streamlit", layout="wide")
st.markdown("# Testando o Streamlit")

def main():

    abas = st.tabs([
        "clientes",
        "cadastrar cliente",
        "editar",
        "deletar",
])

    with abas [0]:
        st.title("Clientes")

    with abas [1]:
        st.title("Cadastrar Clientes")

        with st.form(key="add_cliente", clear_on_submit=True):
            nome = st.text_input('nome', placeholder="nome")
            email = st.text_input("nome", placeholder="email")
            idade = st.number_input("idade", placeholder="idade")
            telefone = st.number_input("telefone", placeholder="telefone") 
        
            profissao = st.selectbox("seleciona a profissao", options=[
        "desenvolvedor web", "analista de infraestrutura",    
        "DBA Senior", 'Tecnico de informatica'
        ])        
            
            btn_cadastrar = st.form_submit_button("cadastrar cliente")

        
    with abas [2]:
        st.title("editar")

    with abas [3]:
        st.title("Deletar")

main()