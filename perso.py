import sys, pygame
from pygame.locals import *
pygame.init()

class Personnage:
    def __init__(self, image, width, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(width, height)
    def moveLeft(self):
        self.pos = self.pos.move(-(self.speed), 0)
    def moveRight(self):
        self.pos = self.pos.move((self.speed), 0)
    def moveUp(self):
        self.pos = self.pos.move(0, -(self.speed))
    def moveDown(self):
        self.pos = self.pos.move(0, (self.speed))

screen = pygame.display.set_mode((600, 600))

fond = pygame.image.load('brick-wall.jpg')
screen.blit(fond, (0,0))

perso = pygame.image.load('perso.png')

pos_pers = perso.get_rect()

pygame.display.flip()

o = Personnage(perso,0,0,3)

pygame.key.set_repeat(400, 30)
while 1:
    screen.blit(fond, o.pos, o.pos)
    for event in pygame.event.get():
          if event.type == KEYDOWN:
              if event.key == K_DOWN:
                  o.moveDown()
              if event.key == K_UP:
                  o.moveUp()
              if event.key == K_LEFT:
                  o.moveLeft()
              if event.key == K_RIGHT:
                  o.moveRight()

    screen.blit(o.image, o.pos)

    pygame.display.flip()
    pygame.time.delay(1)
