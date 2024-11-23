
import json
import os 

def load_world(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    

def load_world_file():
    # Obtém o caminho absoluto da pasta atual (pasta A)
    pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho para a pasta B (pasta irmã)
    pasta_b = os.path.join(pasta_atual, "../mundos_criados")

    # Constrói o caminho completo para o arquivo JSON (ajuste o nome do arquivo)
    caminho_arquivo = os.path.join(pasta_b, "2024-11-23T095943Z_mundo_criado.json")

    # Abre o arquivo e lê o conteúdo JSON
    with open(caminho_arquivo, 'r',encoding='utf8') as arquivo:
        dados_json = json.load(arquivo)
        return dados_json