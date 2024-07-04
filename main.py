import pygame
from sys import exit
from game import Game

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
BACKGROUND = (102, 0, 51)

# Window Screen
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Controls the frame rate of the game
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game.end_game == True:
                game.end_game = False
                game.reset_game()
            if event.key == pygame.K_LEFT and game.end_game == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.end_game == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.end_game == False:
                game.move_down()
            if event.key == pygame.K_UP and game.end_game == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.end_game == False:
            game.move_down()
    
    screen.fill(BACKGROUND)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
