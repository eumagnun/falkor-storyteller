import streamlit as st
from services.service_file import load_world_file
from services.service_memory import __generate_file_name

st.set_page_config(page_title="Falkor",)
st.title("Falkor - Setup")

st.subheader("Configurar opções") 

dados = load_world_file()  
reino_selecionado = st.selectbox(
    "Selecione o Reino",
    [k for k in dados['kingdoms']],
     format_func=lambda k: k['name']
)

st.info(reino_selecionado['description'])

cidade_selecionada = st.selectbox(
    "Selecione a cidade",
    [t for t in reino_selecionado['towns']],
    format_func=lambda t: t['name']
)
st.info(cidade_selecionada['description'])

npc_selecionada = st.selectbox(
    "Selecione a NPC",
    [n for n in cidade_selecionada['npcs']],
    format_func=lambda n: n['name']
)
st.info(npc_selecionada['description'])

if st.button("Reiniciar estória com opções atuais?"):
    print("reset")