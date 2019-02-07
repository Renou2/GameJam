import sys, pygame
from pygame.locals import *
import math

class Bloc(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed, vector ,type):
        pygame.sprite.Sprite.__init__(self)
        self.xori = x
        self.yori = y
        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.rect.x=x-5
        self.rect.y=y-4
        self.pos = image.get_rect().move(x, y)
        self.vector = vector
        self.type = type
    def update(self):
        newpos = self.calcnewpos(self.pos,self.vector)
        self.pos = self.pos.move(self.vector)
        self.rect=self.pos
        (angle,z) = self.vector
        if self.speed != 0 and self.pos.y >1000 and self.type == 9:#respawn au point de départ
            self.pos.y = self.yori
        if self.speed != 0 and self.pos.x <self.xori -100  and self.type == 6:#boucle HORIZONTALE entre xori et xori-100
            self.vector = (3,0)
        if self.speed != 0 and self.pos.x >self.xori  and self.type == 6:
            self.vector = (-3,0)
        if self.speed != 0 and self.pos.y  < self.yori -100  and self.type == 7:#boucle VERTICALE entre yori et yori-100
            self.vector = (0,3)
        if self.speed != 0 and self.pos.y >self.yori and self.type == 7:
            self.vector = (0,-3)
    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
