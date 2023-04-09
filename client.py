# let user deploy his ships
# create server and clients
# transfer info between clients

import pygame
import numpy as np
from ship import Ship

pygame.init()
text_font = pygame.font.SysFont('monospace', 30)


def grid(win, cells, size, pos, ships_on_board):
    [pygame.draw.rect(win, 'white', ((col+pos[0])*size, (row+pos[1])*size, size-1, size-1)) for row, col in np.ndindex(cells.shape)]
    [ship.draw(win) for ship in ships_on_board]

    global text_font
    # letter = 'A'
    # for i in range(15):
    #     text = text_font.render(letter, True, 'white')
    #     win.blit(text, (i+13, i+3))
    #     letter = chr(ord(letter) + 1)


def create_ships(win):
    ships = [Ship(200, 60, 80), Ship(200, 160, 40), Ship(200, 220, 40), Ship(200, 280, 20), Ship(200, 320, 20)]
    [ship.draw(win) for ship in ships]
    return ships


def main():
    win = pygame.display.set_mode((800, 800))

    cells = np.zeros((14, 14))
    ships_on_board = []
    win.fill('black')
    grid(win, cells, 20, (13, 3), ships_on_board)
    grid(win, cells, 20, (13, 20), ships_on_board)
    ships = create_ships(win)
    ship_deploying = ''
    ship_index = ''
    game_is_on = False

    pygame.display.flip()
    pygame.display.update()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for index, ship in enumerate(ships):
                    if ship.rect.collidepoint(pos[0], pos[1]):
                        if not ship_deploying == '':
                            continue
                        ship_deploying = ship.rect
                        ship_index = index
                        pygame.draw.rect(win, 'green', ship_deploying, width=1)
                        ship.set_pos((260, 60))
                        ship.draw(win)
                        pygame.display.flip()
            elif event.type == pygame.KEYDOWN and ship_deploying != '':
                if event.key == pygame.K_RETURN:
                    pygame.draw.rect(win, 'black', ship_deploying, width=1)
                    win.fill('black', ship_deploying)
                    pygame.display.flip()
                    ship_deploying = ''
                    ships_on_board.append(ships[ship_index])
                    continue
                else:
                    if event.key == pygame.K_UP:
                        ships[ship_index].up(win)
                    if event.key == pygame.K_DOWN:
                        ships[ship_index].down(win)
                    if event.key == pygame.K_LEFT:
                        ships[ship_index].left(win)
                    if event.key == pygame.K_RIGHT:
                        ships[ship_index].right(win)
                    grid(win, cells, 20, (13, 3), ships_on_board)
                    ships[ship_index].draw(win)
                    pygame.display.flip()


main()
