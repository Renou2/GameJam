
import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
import tableau

clock = pygame.time.Clock()

GRAVITE = 0.08

class Personnage(pygame.sprite.Sprite):
    def __init__(self, image, width, height, speed):
        self.speed = speed
        self.image = image
        self.pos = pygame.Rect(width, height, 110, 110)
        self.peutsauter=False
        self.v_x = 1.5
        self.v_saut = -6
        self.v_y = self.v_saut
    def deplacement(self):
        if event.type == KEYDOWN:
            if k[K_UP]:
                if self.peutsauter:
                    self.pos.y += self.v_y
                    self.v_y += GRAVITE
                    print("fleche haut")

                    if self.v_y > 0:
                        self.v_y = self.v_saut
                        self.peutsauter=False

                    #verifSortie(self, i, listetab)

            if k[K_RIGHT]:
                self.pos.x += self.speed
                #verifSortie(self, i, listetab)

            if k[K_LEFT]:
                self.pos.x -= self.speed
                #verifSortie(self, i, listetab)

            if k[K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit(0)

#def affichageTableau(tab):
    #screen.blit(tab.background, (0,0))
    #pygame.display.flip()

#def verifSortie(perso, i, listetab):

    #if (perso.pos.centerx >= listetab[i].xafin) and (perso.pos.centery >= listetab[i].yafin) and (perso.pos.centerx <= listetab[i].xbfin) and (perso.pos.centery <= listetab[i].ybfin):
        #print(i)
        #if i < len(listetab):
            #i+=1
        #else : i = 0

    #perso.pos.left = listetab[i].xdebut
    #perso.pos.bottom = listetab[i].ydebut
    #affichageTableau(listetab[i])
#--------------------------------------------------------

#Création d'un tableaude mon code
niveau = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

block = pygame.Surface((50, 50))
block.fill(255)

#Fonction pour dessiner un tableau
def dessiner_niveau(surface, niveau):

    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                screen.blit(block, (i*50, j*50))

#----------------------------------------------------------------


tab1 = tableau.Tableau('abc.png',0,600,500,0,600,100 )
tab2 = tableau.Tableau('brick-wall.png',0,200,500,500,600,600 )
tab3 = tableau.Tableau('sky.jpg',0,200,500,500,600,600 )
listetab =[tab1, tab2, tab3]
i = 0;
screen = pygame.display.set_mode((1000, 1000))
#affichageTableau(listetab[i])
perso = pygame.image.load('perso.png')
pos_pers = perso.get_rect()

o = Personnage(perso,tab1.xdebut,tab1.ydebut-250,2)

screen.blit(o.image, o.pos)
pygame.display.flip()

pygame.key.set_repeat(20, 10)
while 1:
    k = pygame.key.get_pressed()

    if o.pos.y < 400:
        o.pos.y += 2
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()

        o.deplacement()

    screen.blit(o.image, o.pos)
    if o.pos.y==400:
        o.peutsauter=True
        print(o.pos.y)

    dessiner_niveau(screen, niveau)
    pygame.display.flip()

    clock.tick(60)
