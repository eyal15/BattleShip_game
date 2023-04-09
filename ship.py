import pygame


class Ship:

    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.width = 20
        self.height = height
        self.color = 'blue'
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def erase(self, win):
        win.fill('black', self.rect)

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def left(self, win):
        self.erase(win)
        self.set_pos((self.x - 20, self.y))
        self.draw(win)

    def right(self, win):
        self.erase(win)
        self.set_pos((self.x + 20, self.y))

    def up(self, win):
        self.erase(win)
        self.set_pos((self.x, self.y - 20))

    def down(self, win):
        self.erase(win)
        self.set_pos((self.x, self.y + 20))



