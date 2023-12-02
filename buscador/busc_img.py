from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from PIL import Image
import io
import os
import requests  # Adicionada importação

# Configurações da API
API_KEY = "AIzaSyCaruQ2EPnbIOdTf8bJla6lPQJvrS8why4"  # Substitua pelo seu próprio chave de API
SEARCH_ENGINE_ID = "63e73428c5279432c"  # Substitua pelo seu próprio ID de mecanismo de pesquisa

# ...
def search_images(query, num_images=100):  # Ajuste o valor padrão ou passe um valor diferente ao chamar a função
    service = build("customsearch", "v1", developerKey=API_KEY)
    
    try:
        result = service.cse().list(
            q=query,
            cx=SEARCH_ENGINE_ID,
            searchType="image",
            num=num_images  # Ajuste o valor aqui
        ).execute()

        items = result.get("items", [])
        
        return items

    except HttpError as e:
        print("Erro na busca:", e)
        return None
# ...


def download_and_display_images(query, num_images=5):
    items = search_images(query, num_images)
    
    if not items:
        return
    
    download_path = os.path.join(os.path.expanduser("~"), "Desktop", "images", query.replace(" ", "_"))
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    print("Baixando e exibindo imagens...")
    
    for idx, item in enumerate(items, start=1):
        image_url = item.get("link")
        
        try:
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content))
            
            image_filename = f"{idx}.jpg"
            image_path = os.path.join(download_path, image_filename)
            with open(image_path, "wb") as f:
                f.write(response.content)
            
            print(f"Imagem {idx} baixada e exibida")
        
        except Exception as e:
            print(f"Erro ao baixar/exibir imagem {idx}: {e}")

def main():
    search_query = input("Digite o que você deseja buscar: ")
    num_images = int(input("Digite o número de imagens que deseja baixar e exibir: "))
    
    download_and_display_images(search_query, num_images)
def download_and_display_images(query, num_images=5):
    items = search_images(query, num_images)
    
    if not items:
        return
    
    download_path = os.path.join(os.path.expanduser("~"), "Desktop", "images", query.replace(" ", "_"))
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    print("Baixando imagens...")
    
    for idx, item in enumerate(items, start=1):
        image_url = item.get("link")
        
        try:
            response = requests.get(image_url)
            
            image_filename = f"{idx}.jpg"
            image_path = os.path.join(download_path, image_filename)
            with open(image_path, "wb") as f:
                f.write(response.content)
            
            print(f"Imagem {idx} baixada")
        
        except Exception as e:
            print(f"Erro ao baixar imagem {idx}: {e}")

if __name__ == "__main__":
    main()
