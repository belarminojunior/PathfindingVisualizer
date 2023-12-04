import pygame
from util.constants import *


class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j

        self.start = False
        self.wall = False
        self.target = False

        self.queued = False
        self.visited = False
        self.neighbours = []

        self.prior = None

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x * BOX_WIDTH, self.y * BOX_HEIGTH, BOX_WIDTH - 2, BOX_HEIGTH - 2))

    def set_neighbours(self, grid):

        #Horizontal neighbours
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < COLS - 1:
            self.neighbours.append(grid[self.x + 1][self.y])

        #Vertical neighbours
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < ROWS - 1:
            self.neighbours.append(grid[self.x][self.y + 1])

