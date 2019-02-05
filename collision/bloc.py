import sys, pygame
from pygame.locals import *
import math

class Bloc(pygame.sprite.Sprite):
    def __init__(self, image, width, height, speed, vector):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.rect.x=200
        self.rect.y=200
        self.width = width
        self.height = height
        self.pos = image.get_rect().move(width, height)
        self.vector = vector
    def update(self):
        newpos = self.calcnewpos(self.pos,self.vector)
        #self.pos = newpos
        self.pos = self.pos.move(self.vector)
        self.rect=self.pos
        (angle,z) = self.vector
    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
