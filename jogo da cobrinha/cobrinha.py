import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações
WIDTH, HEIGHT = 640, 480
FPS = 10

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configuração da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Função para desenhar a cobra

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(*segment, 10, 10))


# Função principal
def main():
    snake = [(100, 50), (90, 50), (80, 50)]
    snake_dir = (10, 0)

    food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake_dir = (0, -10)
        if keys[pygame.K_DOWN]:
            snake_dir = (0, 10)
        if keys[pygame.K_LEFT]:
            snake_dir = (-10, 0)
        if keys[pygame.K_RIGHT]:
            snake_dir = (10, 0)

        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, new_head)

        if snake[0] == food:
            food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
        else:
            snake.pop()

        # Desenhar na tela
        screen.fill(WHITE)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (*food, 10, 10))

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
