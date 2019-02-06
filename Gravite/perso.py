
import sys, pygame
vec = pygame.math.Vector2
from pygame.locals import *
pygame.init()
import tableau
from math import *
GRAVITE = 9.81



class Personnage(pygame.sprite.Sprite):
    def __init__(self, image):
        self.speed = 15
        self.image = image
        self.rect = image.get_rect()
        self.position = vec(0,0)
        self.pos = pygame.Rect(0, 0, 25, 25)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print(12)
            self.acc.x = -0,5
        if keys[pygame.K_RIGHT]:
            self.acc.x = 0,5
        self.vel += self.acc

        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        self.rect= self.pos
        self.rect.y-=12


#def verifCollide(perso, listesprite):
#    for sprite in listesprite:
#        #print(sprite)
#        if  pygame.sprite.collide_rect(perso,sprite) :
#            return sprite
#    return None
