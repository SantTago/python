import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações
WIDTH, HEIGHT = 400, 600
PLAYER_SIZE = 50
OBSTACLE_SIZE = 30
PLAYER_SPEED = 5
OBSTACLE_SPEED = 3

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configuração da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodging Game")

clock = pygame.time.Clock()

# Classe para o jogador
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - PLAYER_SIZE // 2
        self.y = HEIGHT - PLAYER_SIZE - 20

    def move(self, direction):
        if direction == "left":
            self.x -= PLAYER_SPEED
        elif direction == "right":
            self.x += PLAYER_SPEED

        self.x = max(0, min(self.x, WIDTH - PLAYER_SIZE))

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))

# Classe para os obstáculos
class Obstacle:
    def __init__(self):
        self.x = random.randint(0, WIDTH - OBSTACLE_SIZE)
        self.y = 0

    def move(self):
        self.y += OBSTACLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, OBSTACLE_SIZE, OBSTACLE_SIZE))

def main():
    player = Player()
    obstacles = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        # Movendo e desenhando os obstáculos
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw()

            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)

        # Criando novos obstáculos
        if random.randint(0, 100) < 2:
            obstacles.append(Obstacle())

        # Verificando colisões
        for obstacle in obstacles:
            if (
                obstacle.y + OBSTACLE_SIZE >= player.y
                and player.x < obstacle.x + OBSTACLE_SIZE
                and player.x + PLAYER_SIZE > obstacle.x
            ):
                running = False

        # Desenhar jogador
        player.draw()

        pygame.display.flip()
        screen.fill(WHITE)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
