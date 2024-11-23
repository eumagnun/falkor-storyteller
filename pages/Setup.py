import google.generativeai as genai
import streamlit as st
from Home_config import LLM_API_KEY,LLM_MODEL
from services.service_file import load_world

st.set_page_config(page_title="Falkor",)
st.title("Falkor - Setup")
