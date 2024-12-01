# Falkor Storyteller
Esse app se trata de uma versão inicial de um livro dinâmico onde o leitor vai interagindo e definindo o rumo da história

## Como rodar o projeto localmente
 - Clonar esse repo
````
git clone xxxxxxxXX
````
 - Criar ambiente virtual:
````
python -m venv venv_falkor
````
 - Ativar ambiente virtual:
```
#Linux
source venv_falkor/bin/activate

#Windows
.\venv_falkor\Scripts\activate
```
 - Instalar dependências:
```
pip install -r requirements.txt
#ou
pip  install --force-reinstall -r requirements.txt
```
 - Executar app:
```
#Linux
sh run.sh
#Windows
streamlit run .\Home.py
```
## Como gerar uma imagem docker e implantar o serviço no Cloud Run
 - Gerar imagem:
````
docker build -t us-central1-docker.pkg.dev/{SEU-PROJECT-ID}/demos/falkor .
````
 - Enviar imagem para o Registry:
````
docker push us-central1-docker.pkg.dev/{SEU-PROJECT-ID}/demos/falkor
````
 - Depois disso basta siga essas instruções para executar o deploy https://cloud.google.com/run/docs/deploying

