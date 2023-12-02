"""
Para cortar um vídeo em vários segmentos 
de 59 segundos de duração, você pode usar 
a biblioteca moviepy em conjunto com o ffmpeg. 
Aqui está um exemplo de código que faz isso:

Certifique-se de ter a biblioteca moviepy instalada 
antes de executar o código. Você pode instalar a 
biblioteca usando o comando pip install moviepy.

Certifique-se também de ter o ffmpeg instalado em 
seu sistema e acessível pelo Python. Você pode baixar 
o ffmpeg em https://ffmpeg.org/download.html.
"""

from tkinter import Tk, filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def cortar_video(video_path, pasta_destino, duracao_segmento):
    try:
        video = VideoFileClip(video_path)
        duracao_total = video.duration
        num_segmentos = int(duracao_total // duracao_segmento)

        base_name = os.path.splitext(os.path.basename(video_path))[0]

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

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
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione um vídeo")
    return file_path

if __name__ == "__main__":
    video_path = selecionar_video()
    
    if not video_path:
        print("Nenhum vídeo selecionado.")
    else:
        pasta_destino = r"C:\Users\mocob\Desktop\PASTAS\exerciciosPython\buscador\cortes"
        duracao_segmento = 59  # segundos
        cortar_video(video_path, pasta_destino, duracao_segmento)


