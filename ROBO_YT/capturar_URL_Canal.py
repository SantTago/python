import os
import googleapiclient.discovery
import re

# Defina sua chave de API aqui
API_KEY = 'AIzaSyCaruQ2EPnbIOdTf8bJla6lPQJvrS8why4'

# Crie um serviço da API do YouTube
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

# Nome do arquivo de texto para armazenar a URL anterior
file_name = 'previous_url.txt'

def get_latest_video_url(channel_id):
    try:
        # Faz uma solicitação à API para obter os uploads do canal
        response = youtube.channels().list(part='contentDetails', id=channel_id).execute()
        
        # Obtém a playlist de uploads do canal
        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        # Faz uma solicitação à API para obter os vídeos na playlist de uploads
        playlist_response = youtube.playlistItems().list(
            part='snippet',
            maxResults=1,  # Obtém apenas o vídeo mais recente
            playlistId=uploads_playlist_id
        ).execute()
        
        # Obtém o ID do vídeo mais recente
        video_id = playlist_response['items'][0]['snippet']['resourceId']['videoId']
        
        # Cria o link para o vídeo
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        return video_url
    except Exception as e:
        return str(e)

def read_previous_url(file_name):
    # Lê a URL anterior do arquivo de texto
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            return file.read().strip()
    else:
        return None

def save_previous_url(file_name, url):
    # Salva a URL anterior no arquivo de texto
    with open(file_name, 'w') as file:
        file.write(url)

if __name__ == '__main__':
    channel_input = input('\033[33mDigite o nome do canal do YouTube ou a URL do canal: \033[m')
    
    # Verifica se o input é uma URL de canal ou um nome de canal
    if 'youtube.com/channel/' in channel_input:
        match = re.match(r'https://www\.youtube\.com/channel/([a-zA-Z0-9_-]+)', channel_input)
        if match:
            channel_id = match.group(1)
    else:
        # Faz uma solicitação à API para buscar o canal pelo nome
        search_response = youtube.search().list(
            q=channel_input,
            type='channel',
            part='id',
            maxResults=1
        ).execute()
        
        if 'items' in search_response:
            channel_id = search_response['items'][0]['id']['channelId']
        else:
            print('\033[31mCanal não encontrado.\033[m')
            exit()

    latest_video_url = get_latest_video_url(channel_id)
    previous_url = read_previous_url(file_name)

    # Verifica se a URL anterior é igual à nova URL
    if previous_url and latest_video_url.lower() == previous_url.lower():
        print('\033[31mURL IGUAL A ANTERIOR\033[m')
    else:
        print(f'\033[32mO link do último vídeo do canal é:\033[m {latest_video_url}')
        save_previous_url(file_name, latest_video_url)  # Salva a nova URL como anterior
