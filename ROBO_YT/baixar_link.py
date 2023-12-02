import os
from pytube import YouTube

def baixar_video(link, arquivo):
    try:
        # Crie uma instância do objeto YouTube com o link do vídeo
        yt = YouTube(link)
        
        # Obtenha a melhor resolução disponível
        stream = yt.streams.get_highest_resolution()
        
        # Defina a pasta de destino onde você deseja salvar o vídeo
        pasta_destino = "C:\\Users\\mocob\\Desktop\\PASTAS\\ROBO_YT\\videos"
        
        # Verifique se a pasta de destino existe e crie-a se não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        # Baixe o vídeo para a pasta de destino
        stream.download(output_path=pasta_destino)
        
        print(f"Download completo! O vídeo foi salvo em: {os.path.join(pasta_destino, yt.title)}")
        
        # Após o download, você pode fazer qualquer processamento adicional necessário aqui.
        
        # Elimine o link do arquivo .txt
        with open(arquivo, "r") as file:
            lines = file.readlines()
        
        with open(arquivo, "w") as file:
            for line in lines:
                if line.strip() != link:
                    file.write(line)
    except Exception as e:
        print("Ocorreu um erro:", e)

# Nome do arquivo .txt com os links dos vídeos
arquivo_txt = "links.txt"

# Verifique se o arquivo .txt existe
if os.path.exists(arquivo_txt):
    # Abra o arquivo .txt e leia os links linha por linha
    with open(arquivo_txt, "r") as arquivo:
        for linha in arquivo:
            link_do_video = linha.strip()  # Remove espaços em branco e quebras de linha
            baixar_video(link_do_video, arquivo_txt)
else:
    print(f"O arquivo {arquivo_txt} não foi encontrado.")
