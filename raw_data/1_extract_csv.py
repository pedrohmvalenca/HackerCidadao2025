import os
import requests

# Lista de URLs
# urls = [
#     # Saúde
#     "http://dados.recife.pe.gov.br/dataset/67e48ef2-b8ca-43b7-b29b-419f4f25e524/resource/a30f6b47-e5f0-421d-b891-8fcfdcbe8ecc/download/mae_coruja.csv",
#     # Mobilidade
#     "http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/29afbf42-a36c-475c-8b75-761e17e67679/download/acidentes2024.csv",
#     # Segurança
#     "http://dados.recife.pe.gov.br/dataset/84e0436c-4d17-4c51-b0f0-412e661bbb7d/resource/7dd0e3a9-089b-462a-878a-f892523c0f0d/download/sedec2023.csv",
#     # Meio Ambiente
#     "http://dados.recife.pe.gov.br/dataset/2bc56ecf-4716-449e-9c72-1241f090c6d9/resource/41a65b6d-1e31-4084-9d6b-1f50bfd004e5/download/pesagens2016.csv",
#     "http://dados.recife.pe.gov.br/dataset/9359b0ac-11ce-47ca-be63-d73af5736426/resource/2f3a8820-8680-4768-9f27-b5105239482a/download/coleta.csv",
#     "http://dados.recife.pe.gov.br/dataset/aa9ab544-dc34-4312-8c8f-68a5da7c1ee1/resource/f4ca6471-bb7b-4412-b248-d522948aa789/download/roteirizacao.csv",

# Lista de URLs
urls = [
    # Saúde
    "http://dados.recife.pe.gov.br/dataset/67e48ef2-b8ca-43b7-b29b-419f4f25e524/resource/a30f6b47-e5f0-421d-b891-8fcfdcbe8ecc/download/mae_coruja.csv",
    # Mobilidade
    "http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/29afbf42-a36c-475c-8b75-761e17e67679/download/acidentes2024.csv",
    # Segurança
    "http://dados.recife.pe.gov.br/dataset/84e0436c-4d17-4c51-b0f0-412e661bbb7d/resource/7dd0e3a9-089b-462a-878a-f892523c0f0d/download/sedec2023.csv",
    # Meio Ambiente
    "http://dados.recife.pe.gov.br/dataset/2bc56ecf-4716-449e-9c72-1241f090c6d9/resource/41a65b6d-1e31-4084-9d6b-1f50bfd004e5/download/pesagens2016.csv",
    "http://dados.recife.pe.gov.br/dataset/9359b0ac-11ce-47ca-be63-d73af5736426/resource/2f3a8820-8680-4768-9f27-b5105239482a/download/coleta.csv",
    "http://dados.recife.pe.gov.br/dataset/aa9ab544-dc34-4312-8c8f-68a5da7c1ee1/resource/f4ca6471-bb7b-4412-b248-d522948aa789/download/roteirizacao.csv",
]

# Caminho do diretório "raw_data"
diretorio_data = "./"

# Criar o diretório "raw_data" se ele não existir
if not os.path.exists(diretorio_data):
    os.makedirs(diretorio_data)

# Fazer o download de cada URL
for i, url in enumerate(urls, start=1):
    #nome_arquivo = f"arquivo_{i}.csv"  # Nome único para cada arquivo
    #caminho_arquivo = os.path.join(diretorio_data), #nome_arquivo)
    caminho_arquivo = os.path.join(diretorio_data, os.path.basename(url))

    try:
        print(f"Baixando: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        with open(caminho_arquivo, "wb") as file:
            file.write(response.content)
        print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {url}: {e}")
