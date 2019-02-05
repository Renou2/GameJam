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
        self.rect.x=100
        self.rect.y=100
        self.pos = image.get_rect().move(width, height)
    def moveLeft(self):
        self.pos = self.pos.move(-(self.speed), 0)
    def moveRight(self):
        self.pos = self.pos.move((self.speed), 0)
    def moveUp(self):
        self.pos = self.pos.move(0, -(self.speed))
    def moveDown(self):
        self.pos = self.pos.move(0, (self.speed))
