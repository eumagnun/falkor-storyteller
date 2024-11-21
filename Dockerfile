#Base Image to use
FROM python:3.9

ENV STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true
ENV AUTH_SERVICE_API_KEY=${AUTH_SERVICE_API_KEY}
ENV AUTH_SERVICE_REST_API=${AUTH_SERVICE_REST_API}
ENV PROJECT_ID=${PROJECT_ID}
ENV REGION=${REGION}
ENV LLM_MODEL=${LLM_MODEL}

EXPOSE 8080
WORKDIR /app
COPY app.py app_config.py requirements.txt favicon.ico image_logo.png image_assistente.png /app/
ADD .streamlit ./.streamlit
ADD css ./css
ADD prompts ./prompts
ADD services ./services

#install all requirements in requirements.txt
RUN pip install -r requirements.txt

# Run the web service on container startup
CMD ["streamlit", "run", "app.py", "--server.port=8080"]