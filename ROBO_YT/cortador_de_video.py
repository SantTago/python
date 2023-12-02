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

        while start_time < duracao_total:
            if end_time > duracao_total:
                end_time = duracao_total

            segmento = video.subclip(start_time, end_time)
            segmento_path = os.path.join(pasta_destino, f"{base_name}_segmento_{start_time}_{end_time}.mp4")
            segmento.write_videofile(segmento_path, codec="libx264")

            start_time = end_time
            end_time += duracao_segmento

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
    duracao_segmento = 59  # segundos

    while True:
        videos_para_cortar = buscar_videos_na_pasta(pasta_videos)

        if not videos_para_cortar:
            print("Nenhum vídeo encontrado na pasta.")
            break
        else:
            for video_path in videos_para_cortar:
                cortar_video(video_path, pasta_destino, duracao_segmento)

        # Aguarde um período antes de verificar novamente
        time.sleep(60)  # Verifique a cada 60 segundos
