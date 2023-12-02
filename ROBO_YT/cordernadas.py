import pyautogui

# Aguarde alguns segundos para dar tempo de você mover o mouse para a posição desejada
print("Mova o mouse para a posição desejada...")
pyautogui.sleep(7)

# Obtenha as coordenadas atuais do cursor
x, y = pyautogui.position()

# Imprima as coordenadas
print(f"Coordenadas da tela: X={x}, Y={y}")
