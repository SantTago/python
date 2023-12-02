# pip install pytube

import os
from pytube import YouTube

def baixar_video(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        
        pasta_destino = r"C:\Users\mocob\Desktop\PASTAS\exerciciosPython\buscador\videos"
        
        # Cria a pasta de destino se ela não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        # Define o caminho completo para o arquivo a ser baixado
        caminho_arquivo = os.path.join(pasta_destino, yt.title + ".mp4")
        
        print(f"Baixando: {yt.title}")
        stream.download(output_path=pasta_destino, filename=yt.title)
        print("Download completo!")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    video_link = input("Insira o link do vídeo: ")
    baixar_video(video_link)


    """Neste código, removi a solicitação para 
    inserir o caminho da pasta de destino e defini 
    o caminho diretamente na variável pasta_destino. 
    Certifique-se de que o caminho esteja correto e seja 
    acessível em seu sistema. O prefixo r antes do caminho 
    (r"C:\...") indica uma "string raw", o que significa que 
    os caracteres de escape (como \) não serão interpretados, 
    tornando mais fácil lidar com caminhos de diretório no Windows. 
    Certifique-se de que o caminho esteja corretamente formatado de 
    acordo com as convenções do Windows.
    """

