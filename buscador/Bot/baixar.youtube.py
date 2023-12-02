import os
from pytube import YouTube

def baixar_video(link):
    try:
        # Crie uma instância do objeto YouTube com o link do vídeo
        yt = YouTube(link)
        
        # Obtenha a melhor resolução disponível
        stream = yt.streams.get_highest_resolution()
        
        # Defina a pasta de destino onde você deseja salvar o vídeo
        pasta_destino = r"C:\Users\mocob\Desktop\PASTAS\exerciciosPython\buscador\videos"
        
        # Verifique se a pasta de destino existe e crie-a se não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        # Baixe o vídeo para a pasta de destino
        stream.download(output_path=pasta_destino)
        
        print(f"Download completo! O vídeo foi salvo em: {os.path.join(pasta_destino, yt.title)}")
        
        # Após o download, você pode fazer qualquer processamento adicional necessário aqui.
    except Exception as e:
        print("Ocorreu um erro:", e)

# Exemplo de uso:
link_do_video = input("Informe a URL: ")
baixar_video(link_do_video)
