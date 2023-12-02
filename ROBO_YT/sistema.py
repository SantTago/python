
#                        FASE 1
#--------------------------------------------------------
#-------------------- -Captura de URL -------------------
#--------------------------------------------------------



#                        FASE 2
#--------------------------------------------------------
#--------------------Baixar links------------------
#--------------------------------------------------------

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



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#                        FASE 3
#--------------------------------------------------------
#--------------------Cortador de video------------------
#--------------------------------------------------------

from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import time

def cortar_video(video_path, pasta_destino, duracao_segmento):
    try:
        video = VideoFileClip(video_path)
        duracao_total = video.duration

        base_name = os.path.splitext(os.path.basename(video_path))[0]

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        start_time = 0
        end_time = duracao_segmento
        segment_number = 1  # Adiciona um número sequencial ao nome do arquivo

        while start_time < duracao_total:
            if end_time > duracao_total:
                end_time = duracao_total

            segmento = video.subclip(start_time, end_time)
            segmento_path = os.path.join(pasta_destino, f"{base_name}_{segment_number}.mp4")  # Nome do arquivo único
            segmento.write_videofile(segmento_path, codec="libx264")

            start_time = end_time
            end_time += duracao_segmento
            segment_number += 1  # Incrementa o número sequencial

        print("Corte de vídeo concluído!")

        # Exclua o vídeo original após o corte bem-sucedido
        os.remove(video_path)
    except Exception as e:
        print("Ocorreu um erro:", e)

def buscar_videos_na_pasta(pasta):
    arquivos = os.listdir(pasta)
    videos = [arquivo for arquivo in arquivos if arquivo.endswith('.mp4')]
    caminhos_videos = [os.path.join(pasta, video) for video in videos]
    return caminhos_videos

if __name__ == "__main__":
    pasta_videos = r"C:\\Users\\mocob\\Desktop\\PASTAS\\ROBO_YT\\videos"
    pasta_destino = r"C:\\Users\\mocob\\Desktop\\cortes"
    duracao_segmento = 120  # segundos

    while True:
        videos_para_cortar = buscar_videos_na_pasta(pasta_videos)

        if not videos_para_cortar:
            print("Nenhum vídeo encontrado na pasta.")
            break
        else:
            for video_path in videos_para_cortar:
                cortar_video(video_path, pasta_destino, duracao_segmento)

        # Aguarde um período antes de verificar novamente
        time.sleep(122)  # Verifique a cada 60 segundos


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#                        FASE 4
#--------------------------------------------------------
#--------------------Enviar o video------------------
#--------------------------------------------------------
while True:
    
    import webbrowser
    import time
    import pyautogui

    url = "https://www.facebook.com/"

    # Abrir o navegador no YouTube
    webbrowser.open(url)

    # Aguarde alguns segundos para que o YouTube seja carregado
    time.sleep(5)

    def corder(x=0,y=0):
        
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
        
    # Simule um clique com o botão direito do mouse
    #pyautogui.click(button='right')
    
    # Simule o atalho Ctrl + C
    # pyautogui.hotkey('ctrl', 'c')
  
    try:  
        corder(677,519) # video
        time.sleep(3)

        corder(674,379) # quadro
        time.sleep(3)

        corder(94,432) # area de trabalho
        time.sleep(3)

        corder(230,165) # pasta
        time.sleep(3)

        corder(509,654) # abrir
        time.sleep(3)

        corder(305,119) # primeiro video
        pyautogui.click(button='right')
        time.sleep(2)

        corder(378,571) # renomear 
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(3)

        corder(509,654) # abrir
        time.sleep(1)
        corder(509,654) # abrir
        time.sleep(3)

        corder(644,316) # legenda
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(5)

        corder(671,629) # Publicar
        corder(685,599) # agora nao
        corder(766,168) # sair
        time.sleep(60)
        
        corder(233,15) # Quit
    except:
        print("\033[31mErro no caminho da postagem!\033[m")

    finally:
        print("\033[32mEnvio Finalizado com Sucesso!!\033[m")
        
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    #                        FASE 5
    #--------------------------------------------------------
    #-------------------- excluir o video -------------------
    #--------------------------------------------------------

    # para apagar apos ser postado 

    #Simule um clique com o botão direito do mouse nas coordenadas (x, y)
    
    

    def click(x=0,y=0):
            
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
            
    try: 
        click(170,748) # pasta
        #pyautogui.click(500, 300, button='right')
        time.sleep(2)
        
        click(872,343) #area de trabalho
        time.sleep(2)
        
        pyautogui.click(1055, 353, button='right') # segundo botao em cima da pasta
        time.sleep(2)
        
        click(1081,176) # abrie
        time.sleep(2)
        
        click(1048,362) # primeiro video
        time.sleep(3)
        
        pyautogui.click(1055, 353, button='right') # segundo botao em cima do video
        time.sleep(4)
        
        click(948,660) # Excluir
        time.sleep(2)
        
        click(1283,109) # Quit
        time.sleep(2)
        
    finally:
        print("Fim")
    

    print("Verificação de vídeos concluída.")
    pasta_videos = r"C:\\Users\\mocob\\Desktop\\cortes"
    videos_para_cortar = buscar_videos_na_pasta(pasta_videos)

    if not videos_para_cortar:
        print("Nenhum vídeo encontrado na pasta.")
        break
    
print("PROGRAMA FINALIZADO COM SUCESSO!!!!")