from moviepy.editor import VideoFileClip
print("\033[33m")
# Defina o nome do arquivo de entrada
video_input = "C:\\Users\\mocob\\Desktop\\PASTAS\\ROBO_YT\\videos\\Balmain.mp4"

# Defina o nome do arquivo de saída
video_output = "C:\\Users\\mocob\\Desktop\\cortes\\teste.mp4"

# Carregue o vídeo
clip = VideoFileClip(video_input)

# Redimensione o vídeo para a resolução 1080x1920
clip_resized = clip.resize(height=1080)

# Defina a área de corte para manter a proporção correta (9:16)
clip_cropped = clip_resized.crop(y1=0, y2=1920, x1=0, x2=720)

# Salve o vídeo resultante
clip_cropped.write_videofile(video_output, codec="libx264")

print(f"Vídeo cortado e redimensionado salvo como {video_output}")
