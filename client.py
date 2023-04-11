# transfer info between clients
# start the game
# check if anyone won
# show on boards the players moves
# if anyone won finish the game
# add clock
# add rotate button

import pygame
import numpy as np
from ship import Ship
from network import Network

pygame.init()
text_font = pygame.font.SysFont('monospace', 20)


def grid(win, cells, size, pos, ships_on_board):
    [pygame.draw.rect(win, 'white', ((col+pos[0])*size, (row+pos[1])*size, size-1, size-1)) for row, col in np.ndindex(cells.shape)]
    [ship.draw(win) for ship in ships_on_board]

    global text_font
    letter = 'A'
    for i in range(14):
        text = text_font.render(letter, True, 'white')
        win.blit(text, ((i*20)+265, 30))
        win.blit(text, (230, (i*20)+60))

        win.blit(text, ((i*20)+265, 370))
        win.blit(text, (230, (i*20)+400))
        letter = chr(ord(letter) + 1)


def create_ships(win):
    ships = [Ship(180, 60, 80), Ship(180, 160, 40), Ship(180, 220, 40), Ship(180, 280, 20), Ship(180, 320, 20)]
    [ship.draw(win) for ship in ships]
    return ships


def main():
    running = True

    n = Network()
    startPos = n.get_pos()

    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Battleship Game")
    cells = np.zeros((14, 14))
    ships_on_board = []
    win.fill('black')
    grid(win, cells, 20, (13, 3), ships_on_board)
    grid(win, cells, 20, (13, 20), ships_on_board)
    ships = create_ships(win)
    ship_deploying = ''
    ship_index = ''
    game_is_on = False

    my_board = text_font.render("My Board:", True, 'red')
    win.blit(my_board, (10, 30))
    rival_board = text_font.render("Rival Board:", True, 'red')
    win.blit(rival_board, (10, 400))

    pygame.display.flip()
    pygame.display.update()

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
                    if len(ships_on_board) < 4:
                        pygame.draw.rect(win, 'black', ship_deploying, width=1)
                        win.fill('black', ship_deploying)
                        pygame.display.flip()
                        ship_deploying = ''
                        ships_on_board.append(ships[ship_index])
                    else:
                        game_is_on = True
                        n.send("ready")
                    continue
                else:
                    if event.key == pygame.K_UP and ships[ship_index].get_y() > 60:
                        ships[ship_index].up(win)
                    if event.key == pygame.K_DOWN and ships[ship_index].get_y()+ships[ship_index].get_height() < 340:
                        ships[ship_index].down(win)
                    if event.key == pygame.K_LEFT and ships[ship_index].get_x() > 260:
                        ships[ship_index].left(win)
                    if event.key == pygame.K_RIGHT and ships[ship_index].get_x() < 520:
                        ships[ship_index].right(win)
                    grid(win, cells, 20, (13, 3), ships_on_board)
                    ships[ship_index].draw(win)
                    pygame.display.flip()


if __name__ == '__main__':
    main()
