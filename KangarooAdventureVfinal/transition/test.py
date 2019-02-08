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
    def moveLeft(self, i, listetab):
        self.pos = self.pos.move(-(self.speed), 0)
        verifSortie(self, i, listetab)
    def moveRight(self, i, listetab):
        self.pos = self.pos.move((self.speed), 0)
        verifSortie(self, i, listetab)
    def moveUp(self, i, listetab):
        self.pos = self.pos.move(0, -(self.speed))
        verifSortie(self, i, listetab)
    def moveDown(self, i, listetab):
        self.pos = self.pos.move(0, (self.speed))
        verifSortie(self, i, listetab)
def affichageTableau(tab):
    screen.blit(tab.background, (0,0))
    pygame.display.flip()

def verifSortie(perso, i, listetab):

    if (perso.pos.right == listetab[i].xfin) or (perso.pos.bottom == listetab[i].yfin):
        i+=1;
        perso.pos.left = listetab[i].xdebut
        perso.pos.bottom = listetab[i].ydebut
        affichageTableau(listetab[i])
#--------------------------------------------------------
tab1 = tableau.Tableau('abc.png',0,600,600,0 )
tab2 = tableau.Tableau('brick-wall.jpg',0,200,600,600 )
listetab =[tab1, tab2]
i = 0;
screen = pygame.display.set_mode((600, 600))
affichageTableau(listetab[i])
perso = pygame.image.load('perso.png')
pos_pers = perso.get_rect()



o = Personnage(perso,tab1.xdebut,tab1.ydebut-250,5)

pygame.key.set_repeat(400, 30)
while 1:
    for event in pygame.event.get():
          if event.type == KEYDOWN:
              if event.key == K_DOWN:
                  o.moveDown(i, listetab)
              if event.key == K_UP:
                  o.moveUp(i, listetab)
              if event.key == K_LEFT:
                  o.moveLeft(i, listetab)
              if event.key == K_RIGHT:
                  o.moveRight(i, listetab)

              if event.key == K_ESCAPE :
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
    screen.blit(o.image, o.pos)

    pygame.display.flip()

pygame.time.delay(1)
