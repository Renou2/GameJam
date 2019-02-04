import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
import tableau

class Personnage:
    def __init__(self, image, width, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(width, height)
    def moveLeft(self):
        self.pos = self.pos.move(-(self.speed), 0)
    def moveRight(self, i):
        self.pos = self.pos.move((self.speed), 0)
        if (self.pos.right > 900) and(self.pos.top <0):
            i+=1;
            self.pos.left = 0
            self.pos.bottom = 900
            affichageTableau(listetab[i])
    def moveUp(self, i):
        self.pos = self.pos.move(0, -(self.speed))
        if (self.pos.right > 900) and(self.pos.top <0):
            i+=1;
            self.pos.left = 0
            self.pos.bottom = 900
            affichageTableau(listetab[i])
    def moveDown(self):
        self.pos = self.pos.move(0, (self.speed))

def affichageTableau(tab):
    screen.blit(tab.background, (0,0))
    pygame.display.flip()
#--------------------------------------------------------
tab1 = tableau.Tableau('abc.png',0,900,900,0 )
tab2 = tableau.Tableau('brick-wall.jpg',0,900,900,0 )
listetab =[tab1, tab2]
i = 0;
screen = pygame.display.set_mode((900, 900))
affichageTableau(listetab[i])
perso = pygame.image.load('perso.png')
pos_pers = perso.get_rect()



o = Personnage(perso,0,0,5)

pygame.key.set_repeat(400, 30)
while 1:
    for event in pygame.event.get():
          if event.type == KEYDOWN:
              if event.key == K_DOWN:
                  o.moveDown()
              if event.key == K_UP:
                  o.moveUp(i)
              if event.key == K_LEFT:
                  o.moveLeft()
              if event.key == K_RIGHT:
                  o.moveRight(i)

              if event.key == K_ESCAPE :
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
    screen.blit(o.image, o.pos)

    pygame.display.flip()

pygame.time.delay(1)
