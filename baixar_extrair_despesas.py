import requests
import zipfile
import io
import os

# Coloque aqui o link que você copiou do portal
url = "https://portaldatransparencia.gov.br/download-de-dados/despesas/20250101.zip"
# Pasta de destino
pasta_destino = "dados"

# Baixar o arquivo
print("Baixando o arquivo...")
response = requests.get(url)

if response.status_code == 200:
    print("Download concluído. Extraindo arquivos...")
    # Criar a pasta de destino se não existir
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Extrair o conteúdo
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(pasta_destino)

    print("Extração concluída. Arquivos salvos em:", pasta_destino)
else:
    print("Erro ao baixar o arquivo:", response.status_code)
