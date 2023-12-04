from tkinter import messagebox, Tk
import pygame
import sys

from util.constants import *
from models import box

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))

grid = []
queue = []
path = []

# Create the Grid
for i in range(COLS):
    arr = []
    for j in range(ROWS):
        arr.append(box.Box(i, j))
    grid.append(arr)

# Set neighbours
for i in range(COLS):
    for j in range(ROWS):
        grid[i][j].set_neighbours(grid)

start_box = grid[0][0]
start_box.start = True
start_box.visted = True
queue.append(start_box)


def main():
    begin_search = False
    target_box_set = False

    searching = True
    target_box = None

    while True:

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse Motions
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                # Draw Wall
                if event.buttons[0]:
                    i = x // BOX_WIDTH
                    j = y // BOX_HEIGTH
                    grid[i][j].wall = True

                #Set Target
                if event.buttons[2] and not target_box_set:
                    i = x // BOX_WIDTH
                    j = y // BOX_HEIGTH

                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True

            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True

        if begin_search:
            if len(queue) > 0 and searching:
                current_box = queue.pop(0)
                current_box.visited = True

                if current_box == target_box:
                    searching = False

                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior

                else:
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box
                            queue.append(neighbour)

            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There's No Solution!")
                    searching = False
        
        WINDOW.fill((0, 0, 0))

        for i in range(COLS):
            for j in range(ROWS):
                box = grid[i][j]
                box.draw(WINDOW, (50, 50, 50))

                if box.queued:
                    box.draw(WINDOW, (200, 0, 0))
                if box.visited:
                    box.draw(WINDOW, (0, 200, 0))

                if box in path:
                    box.draw(WINDOW, (0, 0, 200))

                if box.start:
                    box.draw(WINDOW, (0, 200, 200))
                if box.wall:
                    box.draw(WINDOW, (40, 90, 90))
                if box.target:
                    box.draw(WINDOW, (200, 200, 0))


        pygame.display.update()


if __name__ == '__main__':
    main()