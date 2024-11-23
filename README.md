# falkor-storyteller
Passos para execução local ou no Cloud Shell:

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
#ou
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
sh run.sh
```
Caso queira gerar uma imagem para implantação no Cloud Run:

 - Gerar imagem:
````
docker build -t us-central1-docker.pkg.dev/{SEU-PROJECT-ID}/demos/falkor .
````
 - Enviar imagem para o Registry:
````
docker push us-central1-docker.pkg.dev/{SEU-PROJECT-ID}/demos/falkor
````

