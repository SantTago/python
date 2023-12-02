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
    corder(677,552) # video
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
    time.sleep(3)

    corder(671,629) # Publicar
    time.sleep(60)

    corder(233,15) # Quit
except:
    print("\033[31mErro no caminho da postagem!\033[m")

finally:
    print("\033[32mEnvio Finalizado com Sucesso!!\033[m")