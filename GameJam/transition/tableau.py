import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit

class Tableau(pygame.sprite.Group):
    def __init__(self, background, xdebut, ydebut, xfin, yfin):
        pygame.sprite.RenderClear.__init__(self)
        self.width = 900
        self.height = 900
        self.background = pygame.image.load(background)
        self.xdebut = xdebut
        self.ydebut = ydebut
        self.xfin = xfin
        self.yfin = yfin
