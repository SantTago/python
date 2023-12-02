from pygame.locals import *
import pygame



#Passo 3: Inicializar o Pygame
#Antes de começar a utilizar o Pygame, é necessário inicializá-lo:

pygame.init()

#Passo 4: Configurar a janela do jogo
#Defina as configurações da janela do jogo, como 
# tamanho, título e cor de fundo:

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Caixa de Login")
background_color = (255, 255, 255)  # Branco
                  #(255,  0,  0)  # Vermelho
                    #(0, 0, 255)  # Azul

#Passo 5: Criar a classe para a caixa de login
#Crie uma classe para a caixa de login, que será responsável por 
# exibir e controlar a entrada de dados do usuário:
class LoginBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (220, 220, 220)  # Cinza claro
        self.text = ""
        self.font = pygame.font.Font(None, 32)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # Aqui você pode fazer o tratamento dos dados de login
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Preto
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
#Passo 6: Criar o loop principal do jogo
#Crie um loop principal que irá executar o jogo:
def main():
    clock = pygame.time.Clock()
    running = True

    login_box = LoginBox(300, 250, 200, 40)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            login_box.handle_event(event)

        screen.fill(background_color)
        login_box.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

#Passo 7: Executar o jogo
#Chame a função `main()` para executar o jogo:

#Agora você pode executar o código e verá uma janela 
# com uma caixa de login. Ao clicar na caixa de login,
# você poderá digitar o texto e pressionar Enter para 
# exibir o texto no console. Você pode adicionar as funcionalidades 
# de autenticação de login de acordo com suas necessidades.
    
if __name__ == "__main__":
    main()