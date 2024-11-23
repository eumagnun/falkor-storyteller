import streamlit as st
from services.service_file import load_world_file
from services.service_memory import setup_world_options

st.set_page_config(page_title="Falkor",)
st.title("Falkor - Setup")

st.subheader("Configurar opções") 

dados = load_world_file()  
reino_selecionado = st.selectbox(
    "Selecione o Reino",
    [k for k in dados['kingdoms']],
    #index=dados['kingdoms'].index(st.session_state["reino_selecionado"]) ,
    format_func=lambda k: k['name']
)

st.info(reino_selecionado['description'])

cidade_selecionada = st.selectbox(
    "Selecione a cidade",
    [t for t in reino_selecionado['towns']],
    #index=reino_selecionado['towns'].index(st.session_state["cidade_selecionada"]),
    format_func=lambda t: t['name']
)
st.info(cidade_selecionada['description'])

npc_selecionada = st.selectbox(
    "Selecione a NPC",
    [n for n in cidade_selecionada['npcs']],
    #index=cidade_selecionada['npcs'].index(st.session_state["npc_selecionada"])  ,
    format_func=lambda n: n['name']
)
st.info(npc_selecionada['description'])

if st.button("Reiniciar estória com opções atuais?"):
    setup_world_options(reino_selecionado,cidade_selecionada,npc_selecionada)