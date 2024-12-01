import os
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)
AUTH_SERVICE_API_KEY =os.getenv("AUTH_SERVICE_API_KEY")
AUTH_SERVICE_REST_API = "https://identitytoolkit.googleapis.com/v1/accounts"
LLM_MODEL = os.getenv("LLM_MODEL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
MAX_OUTPUT_TOKENS = 8192
TEMPERATURE = 0.1
