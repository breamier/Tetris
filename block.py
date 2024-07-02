from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_shift = 0
        self.column_shift = 0
        self.state = 0
        self.colors = Colors.get_colors()

    def draw(self, screen):
        tiles = self.get_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def move(self, rows, columns):
        self.row_shift += rows
        self.column_shift += columns
    
    def rotate(self):
        self.state += 1
        if self.state == len(self.cells):
            self.state = 0
    
    def undo_rotate(self):
        self.state -= 1
        if self.state == 0:
            self.state = len(self.cells) - 1
    
    def get_positions(self):
        tiles = self.cells[self.state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_shift, position.column + self.column_shift)
            moved_tiles.append(position)
        return moved_tiles