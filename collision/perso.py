import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit

class Personnage(pygame.sprite.Sprite):
    def __init__(self, image, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.rect.x=25
        self.rect.y=25
        self.pos = image.get_rect().move(width, height)
    def moveLeft(self):
        self.pos = self.pos.move(-(self.speed), 0)
        self.rect=self.pos
    def moveRight(self):
        self.pos = self.pos.move((self.speed), 0)
        self.rect=self.pos
    def moveUp(self):
        self.pos = self.pos.move(0, -(self.speed))
        self.rect=self.pos
    def moveDown(self):
        self.pos = self.pos.move(0, (self.speed))
        self.rect=self.pos
