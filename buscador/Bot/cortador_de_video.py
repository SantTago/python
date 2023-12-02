

from tkinter import Tk, filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def cortar_video(video_path, pasta_destino, duracao_segmento):
    try:
        video = VideoFileClip(video_path) #video_path video selecionado pelo usuario |  VideoFileClip permite que você leia um arquivo de vídeo (como um arquivo MP4
        duracao_total = video.duration
        num_segmentos = int(duracao_total // duracao_segmento) # duracao_total  total dividito por segmento
        # num_segmentos será um número inteiro que representa quantos segmentos cabem no vídeo.
        
        base_name = os.path.splitext(os.path.basename(video_path))[0]
                    # os.path.splitext - extrai o nome do arquivo do vídeo (sem a extensão) usando as funções do módulo
        if not os.path.exists(pasta_destino): # Verifica se a pasta de destino especificada (pasta_destino) não existe e, se não existir, a cria usando
            os.makedirs(pasta_destino)
            # os: É um módulo da biblioteca padrão de Python chamado os (sistema operacional). 
            # makedirs: Esta é uma função do módulo os que significa "make directories" (criar diretórios). Ela é usada para criar diretórios no sistema de arquivos.
            
        for i in range(num_segmentos):
            start_time = i * duracao_segmento
            end_time = min((i + 1) * duracao_segmento, duracao_total)
            segmento = video.subclip(start_time, end_time)
            segmento_path = os.path.join(pasta_destino, f"{base_name}_segmento_{i+1}.mp4")
            segmento.write_videofile(segmento_path, codec="libx264")

        print("Corte de vídeo concluído!")
    except Exception as e:
        print("Ocorreu um erro:", e)

def selecionar_video(): 
    root = Tk() # TK() Criar a janela principal ou tk.Tk()
    root.withdraw()  # Oculta a janela principal se você não desejar exibi-la
    file_path = filedialog.askopenfilename(title="Selecione um vídeo") # askopenfilename   exibe uma janela de diálogo na qual o usuário pode navegar pelo sistema de arquivos e selecionar um arquivo
    return file_path # ele retorna a caixa para procurar o arquivo de MP4

if __name__ == "__main__":
    video_path = selecionar_video() #  selecionar_video() e a funçao que vai trazer o video selecionado
    
    if not video_path: # se nao voltar nenhum video
        print("Nenhum vídeo selecionado.")
    else: # se voltar esse e o caminho para salvar
        pasta_destino = r"C:\Users\mocob\Desktop\PASTAS\exerciciosPython\buscador\cortes"
        duracao_segmento = 59  # segundos
        cortar_video(video_path, pasta_destino, duracao_segmento) # a funçao cortar_video eleprecisa de 3 parametros
        # video_path = selecionar o video | pasta_destino = onde sera salvo | duracao_segmento = quantos segundos sera cortadoo video


