import pygame
from sys import exit

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

# Window Screen
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Controls the frame rate of the game
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
