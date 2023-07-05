import streamlit as st

import controllers.clientecontroller as Clientecontroller
import Pages.Cliente.Create as pageincluirCliente
import Pages.Cliente.Read as pageListCliente

st.sidebar.title("Menu")
page_cliente = st.sidebar.selectbox('Opções:', ['Incluir', 'Consultar'], 0)

if 'Consultar' in page_cliente:
    pageListCliente.List()

if 'Incluir' in page_cliente:
    st.experimental_set_query_params()
    pageincluirCliente.Create()


