#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#                        FASE 4
#--------------------------------------------------------
#--------------------Enviar o video------------------
#--------------------------------------------------------
while True:
    
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
        
    # Simule um clique com o botão direito do mouse
    #pyautogui.click(button='right')
    
    # Simule o atalho Ctrl + C
    # pyautogui.hotkey('ctrl', 'c')
    
    try:
        #corder(76,91) #Facebook
        #time.sleep(5)
        
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
        
        corder(254,118) # video
        time.sleep(3)
        
        corder(516,656) # abrir 
        time.sleep(3)

        corder(183,683) # avançar
        time.sleep(5)
        
        corder(259,688) # avançar
        time.sleep(5)
        
        corder(259,688) # Publicar
        time.sleep(70)

        corder(233,15) # Quit
        
    except:
        print("\033[31mAlgo deu ERRADO com as cordenadas de tock\033[m")
    finally:
        print("\033[32mCiclo Encerrado\033[m")