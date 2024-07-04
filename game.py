from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.end_game = False

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        block = self.blocks[random.randrange(len(self.blocks))]
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

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
        self.grid.clear_completed_rows()
        if self.block_valid() == False:
            self.end_game = True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotate()
    
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
