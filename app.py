import google.generativeai as genai
import streamlit as st
from app_config import LLM_API_KEY,LLM_MODEL
from services.service_memory import retrieve_memories
from prompts import basic_template

st.set_page_config(page_title="Falkor",)
st.title("Falkor - O contador de histórias")

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
    llm_model = genai.GenerativeModel(
        model_name=LLM_MODEL,
        generation_config=generation_config,
        )
    st.session_state["client"] = llm_model


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"])

if user_message := st.chat_input("Digite aqui..."):
   
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.spinner('Wait for it...'):
        with st.chat_message("assistant"):
            client = st.session_state["client"]

            memories = retrieve_memories(st.session_state.messages)
            prompt = basic_template.get().format(user_message,memories)
            llm_response=client.generate_content(prompt)
            st.write(llm_response.text)

        st.session_state.messages.append({"role": "user", "parts": user_message})        
        st.session_state.messages.append({"role": "assistant", "parts": llm_response.text})
        
       # print(st.session_state.messages)
       # print("====================================")
