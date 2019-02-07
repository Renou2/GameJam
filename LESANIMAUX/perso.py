
import sys, pygame
from pygame.locals import *
pygame.init()
import tableau
from math import *
GRAVITE = 9.81



class Personnage(pygame.sprite.Sprite):
    def __init__(self, image):
        self.speed = 15
        self.image = image
        #self.image_rect.center = self.rect.center
        self.rect = image.get_rect()
        self.pos = pygame.Rect(200, 200, 25, 25)
        self.xa = 200
        self.ya = 200
        self.t=0
        self.xr = 0
        self.yr = 0
        self.v_x = 1.5
        self.v_saut = -6
        self.v_y = self.v_saut
        self.peutsauter=True
        self.speed = 5
        self.droite=False
        self.gauche=False


def verifCollide(perso, listesprite):
    for sprite in listesprite:
        #print(sprite)
        if  pygame.sprite.collide_rect(perso,sprite) :
            return sprite
    return None
