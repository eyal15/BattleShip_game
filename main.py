# let user deploy his ships
# create server and clients
# transfer info between clients

import pygame
import numpy as np
from ship import Ship

pygame.init()
text_font = pygame.font.SysFont('monospace', 30)


def grid(win, cells, size, pos):
    global text_font
    for row, col in np.ndindex(cells.shape):
        pygame.draw.rect(win, 'white', ((col+pos[0])*size, (row+pos[1])*size, size-1, size-1))

    # letter = 'A'
    # for i in range(15):
    #     text = text_font.render(letter, True, 'white')
    #     win.blit(text, (i+13, i+3))
    #     letter = chr(ord(letter) + 1)


def create_ships(win):
    ships = [Ship(200, 60, 80), Ship(200, 160, 40), Ship(200, 220, 40), Ship(200, 280, 20), Ship(200, 320, 20)]
    for ship in ships:
        ship.draw(win)
    return ships


def main():
    win = pygame.display.set_mode((800, 800))

    cells = np.zeros((14, 14))
    win.fill('black')
    grid(win, cells, 20, (13, 3))
    grid(win, cells, 20, (13, 20))
    ships = create_ships(win)
    ship_deploying = ''
    ship_index = ''

    pygame.display.flip()
    pygame.display.update()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if ship_deploying != '' and 260 <= pos[0] <= 540 and 60 <= pos[1] <= 340:
                    ships[ship_index].erase(win)
                    ships[ship_index].set_pos(pos)
                    ships[ship_index].draw(win)
                    pygame.display.flip()
                    ship_deploying = ''
                else:
                    for index, ship in enumerate(ships):
                        if ship.rect.collidepoint(pos[0], pos[1]):
                            if not ship_deploying == '':
                                pygame.draw.rect(win, 'black', ship_deploying.rect, width=1)
                            ship_deploying = ship
                            ship_index = index
                            pygame.draw.rect(win, 'green', ship_deploying.rect, width=1)
                            pygame.display.flip()


main()
