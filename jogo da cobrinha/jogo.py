import pygame
import sys
import random

# Inicialização do Pygame
pygame.init() 

# Configurações
WIDTH, HEIGHT = 1280, 720 # resoluçao da tela 
PLAYER_SIZE = 50 # Determina o tamanho (largura e altura) do jogador (o objeto controlado pelo jogador).
ENEMY_SIZE = 40 #  Determina o tamanho dos inimigos (os elementos que o jogador deve evitar ou atirar).
BULLET_SIZE = 10 #  Determina o tamanho dos tiros (os objetos disparados pelo jogador para atacar os inimigos).
PLAYER_SPEED = 5 # Define a velocidade de movimento do jogador. Quanto maior o valor, mais rápido o jogador se moverá.
BULLET_SPEED = 10 # Define a velocidade dos tiros disparados pelo jogador. Quanto maior o valor, mais rápido os tiros se moverão.
ENEMY_SPEED = 3 #  Define a velocidade de movimento dos inimigos. Quanto maior o valor, mais rápido os inimigos se moverão em direção ao jogador.


# Cores

WHITE = (0, 255, 0)   # cor do poder
BLACK = (0, 0, 0)  # preto
RED = (255, 0, 0)  # vermelho
GREEN = (0, 255, 0)  # verde
BLUE = (0, 0, 255)  # azul
YELLOW = (255, 255, 0)  # amarelo
ORANGE = (255, 165, 0)  # laranja
PURPLE = (128, 0, 128)  # roxo
PINK = (255, 192, 203)  # rosa claro
CYAN = (0, 255, 255)  # ciano
BROWN = (165, 42, 42)  # marrom
GRAY = (128, 128, 128)  # cinza


# Configuração da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("jogo do Gael")

clock = pygame.time.Clock() # para controlar a taxa de quadros por segundo (FPS) do seu jogo.

# Classe para a nave do jogador
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - PLAYER_SIZE // 2
        self.y = HEIGHT - PLAYER_SIZE - 20
        self.bullets = []

    def move(self, direction):
        if direction == "left":
            self.x -= PLAYER_SPEED
        elif direction == "right":
            self.x += PLAYER_SPEED

        self.x = max(0, min(self.x, WIDTH - PLAYER_SIZE))

    def shoot(self):
        self.bullets.append(Bullet(self.x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, self.y))

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x + ENEMY_SIZE // 2, self.y + ENEMY_SIZE // 2), ENEMY_SIZE // 2) # pygame.draw.rect()  é usada para desenhar um retângulo na tela, e é assim que a forma do jogador é criada.
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()

            if bullet.y < 0:
                self.bullets.remove(bullet)

# Classe para os tiros do jogador
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= BULLET_SPEED

    def draw(self):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, BULLET_SIZE, BULLET_SIZE))
            
# Classe para o jogador
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - PLAYER_SIZE // 2
        self.y = HEIGHT - PLAYER_SIZE - 20
        self.bullets = []
        self.enemies_eliminated = 0

    def check_collisions(self, enemies):
        enemies_to_remove = []

        for enemy in enemies:
            for bullet in self.bullets:
                if (
                    enemy.y + ENEMY_SIZE >= bullet.y
                    and bullet.x < enemy.x + ENEMY_SIZE
                    and bullet.x + BULLET_SIZE > enemy.x
                ):
                    enemies_to_remove.append(enemy)
                    self.bullets.remove(bullet)
                    self.enemies_eliminated += 1

        for enemy in enemies_to_remove:
            if enemy in enemies:
                enemies.remove(enemy)


    def move(self, direction):
        if direction == "left":
            self.x -= PLAYER_SPEED
        elif direction == "right":
            self.x += PLAYER_SPEED

        self.x = max(0, min(self.x, WIDTH - PLAYER_SIZE))

    def shoot(self):
        self.bullets.append(Bullet(self.x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, self.y))

    def draw(self):
        # Pontos para criar um triângulo equilátero
        points = [
            (self.x, self.y - PLAYER_SIZE),                    # Ponto superior
            (self.x - PLAYER_SIZE // 1, self.y + PLAYER_SIZE), # Ponto inferior esquerdo
            (self.x + PLAYER_SIZE // 1, self.y + PLAYER_SIZE)  # Ponto inferior direito
        ]

        pygame.draw.polygon(screen, RED, points)  # Desenha o triângulo preto

        for bullet in self.bullets:
            bullet.move()
            bullet.draw()
            if bullet.y < 0: 
                self.bullets.remove(bullet)

# Classe para os inimigos
class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.y = 0

    def move(self):
        self.y += ENEMY_SPEED

    def draw(self):
        # Desenhe a aranha preta
        pygame.draw.circle(screen, BLUE, (self.x + ENEMY_SIZE // 2, self.y + ENEMY_SIZE // 2), ENEMY_SIZE // 2)

    # No loop principal
    player = Player()
    
        
    # Exibir o contador de inimigos eliminados na tela
    font = pygame.font.Font(None, 36) # pygame.font para renderizar o texto e exibi-lo na tela
    text = font.render(f"Eliminados: {player.enemies_eliminated}", True, RED) # BLACK cor do contador
    screen.blit(text, (10, 10)) # Isso renderiza o texto com o número de inimigos eliminados e o exibe na posição (10, 10) na tela.

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# programa principal
def main():
    player = Player()
    enemies = []
    enemies_to_remove = []  # Lista para inimigos que precisam ser removidos

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left") # esquerda
        if keys[pygame.K_RIGHT]:
            player.move("right") # certa
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Preencher a tela com a cor amarela
        screen.fill(YELLOW) 
        
        player.check_collisions(enemies)
        
        # Movendo e desenhando os inimigos
        for enemy in enemies:
            enemy.move()
            enemy.draw()

            if enemy.y > HEIGHT: # ALTURA 
                #inimigo.y
                enemies_to_remove.append(enemy)

        # Removendo inimigos que precisam ser removidos
        for enemy in enemies_to_remove:
            if enemy in enemies:
                enemies.remove(enemy)

        # Criando novos inimigos
        if random.randint(0, 100) < 3:
            enemies.append(Enemy())

        # Verificando colisões
        for enemy in enemies:   
            for bullet in player.bullets: # bullet => bala
                if (
                    enemy.y + ENEMY_SIZE >= bullet.y
                    and bullet.x < enemy.x + ENEMY_SIZE
                    and bullet.x + BULLET_SIZE > enemy.x
                ):
                    enemies_to_remove.append(enemy)
                    player.bullets.remove(bullet)
                    player.enemies_eliminated += 1  # Aumenta o contador de inimigos eliminados

        # Desenhar jogador
        player.draw()

        # Exibir o contador de inimigos eliminados na tela
        font = pygame.font.Font(None, 36)
        text = font.render(f"Eliminados: {player.enemies_eliminated}", True, RED)
        screen.blit(text, (10, 10))

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)

        # Limpar a tela
        screen.fill(BLACK)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
