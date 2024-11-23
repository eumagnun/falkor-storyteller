import google.generativeai as genai
import streamlit as st
from Home_config import LLM_API_KEY,LLM_MODEL
from services.service_memory import retrieve_memories,setup_world_options
from prompts import basic_template


st.set_page_config(page_title="Falkor",)
st.title("Falkor - O contador de histórias")


def call_assistant(user_message, start=False):
    client = st.session_state["client"]

    memories = retrieve_memories(st.session_state.messages)
    prompt = f"""Responda a solicitacao do usuario considerando o o seguinte contexto: 
                 solicitacao={user_message},
                 historico={memories}, 
                 world_info={st.session_state["world_info"]}
                 """
    llm_response=client.generate_content(prompt)

    st.info(llm_response.text)

    if not start:
        st.session_state.messages.append({"role": "user", "parts": user_message})  
        st.session_state.messages.append({"role": "falkor", "parts": llm_response.text})    
      
if "messages" not in st.session_state:
    st.session_state.messages = []



if "client" not in st.session_state:
    genai.configure(api_key=LLM_API_KEY)

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    setup_world_options()

    persona = basic_template.get()

    llm_model = genai.GenerativeModel(
        model_name=LLM_MODEL,
        generation_config=generation_config,
        system_instruction=persona
    )
    st.session_state["client"] = llm_model

    call_assistant("descreva de forma detalhada o reino, cidades, personagem e ultimas ocorrências",start=True)


for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=f"{message['role']}.png"):
        st.markdown(message["parts"])


if user_message := st.chat_input("Digite START para começar..."):
   
    with st.chat_message("user",avatar="user.png"):
        st.markdown(user_message)

    with st.spinner('Wait for it...'):
        with st.chat_message("falkor",avatar="falkor.png"):
            call_assistant(user_message)
        