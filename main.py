import pygame
from sys import exit
from game import Game
from colors import Colors

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

# Window Screen
pygame.init()

font_title = pygame.font.Font(None, 40)
score_surface = font_title.render("Score", True, Colors.WHITE) 
next_surface = font_title.render("Next Block", True, Colors.WHITE) 
game_over_surface = font_title.render("GAME OVER", True, Colors.RED)

score_rect = pygame.Rect(375, 120, 180, 50)
next_rect = pygame.Rect(375, 290, 180, 150)

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
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.end_game == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.end_game == False:
            game.move_down()
    
    screen.fill(Colors.FUCHSIA)
    # Add position of Score
    score_value_surface = font_title.render(str(game.score), True, Colors.BACKGROUND)
    screen.blit(score_surface, (425, 90, 100, 100))
    pygame.draw.rect(screen, Colors.WHITE, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    screen.blit(next_surface, (395, 250, 100, 200))
    pygame.draw.rect(screen, Colors.WHITE,  next_rect, 0, 10)

    if game.end_game == True:
        screen.blit(game_over_surface, (380, 450, 100, 100))
    
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
