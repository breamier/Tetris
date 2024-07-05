from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.end_game = False
        self.score = 0
        # Sound Effect by <a href="https://pixabay.com/users/floraphonic-38928062/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=186888">floraphonic</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=186888">Pixabay</a>
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.mp3")
        # Sound Effect by <a href="https://pixabay.com/users/liecio-3298866/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=190035">LIECIO</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=190035">Pixabay</a>
        self.clear_sound = pygame.mixer.Sound("sounds/clear.mp3")
        #Sound Effect by <a href="https://pixabay.com/users/n2kstudio-17715924/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=163649">N2kStudio</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=163649">Pixabay</a>
        pygame.mixer.music.load("sounds/music1.mp3")
        pygame.mixer.music.play(-1)

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        block = self.blocks[random.randrange(len(self.blocks))]
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 21, 81)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 320, 350)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 320, 330)
        else:
            self.next_block.draw(screen, 330, 330)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_valid() == False:
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_valid() == False:
            self.current_block.move(0, -1)
    
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_valid() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_completed_rows()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
            self.clear_sound.play()
        if self.block_valid() == False:
            self.end_game = True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotate()
        else:
            self.rotate_sound.play()
    
    def block_inside(self):
        tiles = self.current_block.get_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def block_valid(self):
        tiles = self.current_block.get_positions()
        for position in tiles:
            if self.grid.is_empty(position.row, position.column) == False:
                return False
        return True
    
    def reset_game(self):
        self.grid.clear_grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
    
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared > 0:
            self.score += lines_cleared * 50
        self.score += move_down_points

