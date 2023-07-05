import streamlit as st
import models.cliente as Cliente
import controllers.clientecontroller as Clientecontroller

def Create():
    idAlteracao = st.experimental_get_query_params()
    clienteRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        clienteRecuperado = Clientecontroller.selecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[clienteRecuperado.id]
        )
        st.title("Alterar cliente")
    else:
        st.title("Incluir cliente")
    with st.form(key="include_cliente", clear_on_submit=True):
        ListOcuppation = ["Desenvolvedor(a)", "Professor(a)", "Eletricista", "Musico", "Designer", "Mecanico", "Uber"]
        
        if clienteRecuperado == None:
            input_name = st.text_input(label="Insira seu nome")
            input_age = st.number_input(label="Insira sua idade", format='%d', value=0, min_value=0, max_value=125, step=1)
            input_occupation = st.selectbox("Selecione sua profissão", options=ListOcuppation)
        else:
            input_name = st.text_input(label="Insira seu nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira sua idade", format='%d', value=clienteRecuperado.idade, min_value=0, max_value=125, step=1)
            input_occupation = st.selectbox("Selecione sua profissão", options=ListOcuppation, index=ListOcuppation.index(clienteRecuperado.profissao))
        Input_button_submit = st.form_submit_button("Enviar")

    if Input_button_submit:
        if clienteRecuperado == None:
            Clientecontroller.Incluir(Cliente.Cliente(0, input_name, input_age, input_occupation))
            st.success("Cliente incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            Clientecontroller.Alterar(Cliente.Cliente(clienteRecuperado.id, input_name, input_age, input_occupation))
            st.success("Cliente alterado com sucesso!")