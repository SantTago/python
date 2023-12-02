import webbrowser
import time
import pyautogui


# URL do YouTube
url = "https://www.facebook.com/"

# Abrir o navegador no YouTube
webbrowser.open(url)

# Aguarde alguns segundos para que o YouTube seja carregado
time.sleep(5)

    
def corder(x=0,y=0):
    
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    
try:
    corder(76,91) #Facebook
    time.sleep(3)
    
    corder(688,552) # Video/Foto
    time.sleep(3)
    
    corder(838,549) # Reel
    time.sleep(3)
    
    corder(177,345) # Adicionar video
    time.sleep(3)
    
    corder(82,433) #area de trabalho
    time.sleep(3)
    
    corder(225,157) # pasta do video
    time.sleep(3)
    
    corder(516,656) # abrir 
    time.sleep(3)
    
    corder(213,157) # video
    time.sleep(3)
    
    corder(516,656) # abrir 
    time.sleep(3)

    corder(183,683) # avançar
    time.sleep(3)
    
    corder(183,683) # avançar
    time.sleep(3)
    
    corder(183,683) # Publicar
    time.sleep(3)

    corder(233,15) # Quit
    time.sleep(3)
except:
    print("Erro no codigo do facebook")
    
finally:
    print("FIM")