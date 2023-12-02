

# para apagar apos ser postado 

    #Simule um clique com o botão direito do mouse nas coordenadas (x, y)
import pyautogui
import time

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
    
finally:
    print("Fim")