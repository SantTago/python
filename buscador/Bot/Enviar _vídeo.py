
import webbrowser
import time
import pyautogui


# URL do YouTube
url = "https://www.youtube.com"

# Abrir o navegador no YouTube
webbrowser.open(url)

# Aguarde alguns segundos para que o YouTube seja carregado
time.sleep(5)

    
def corder(x=0,y=0):
    
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()

corder(1197,133) # Criar 
time.sleep(5)

corder(1151,188) # Enviar video
time.sleep(10)

corder(686,536) # selecionar video

# Feche o navegador (opcional)
# pyautogui.hotkey('ctrl', 'w')  # Feche a guia do navegador
