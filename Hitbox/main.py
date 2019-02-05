
import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
from tableau import Tableau
from perso import Personnage
from bloc import Bloc
clock = pygame.time.Clock()

GRAVITE = 0.08

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

#block = pygame.Surface((50, 50))
#block.fill(255)
imbloc = pygame.image.load('brick-wall.png')
screen = pygame.display.set_mode((1000, 1000))
fond = pygame.image.load('sky.jpg')
screen.blit(fond, (0,0))


#Fonction pour dessiner un tableau
def dessiner_niveau(surface, niveau, listesprite):

    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                b = Bloc(imbloc, i*50, j*50, 0, (0,0))
                listesprite.add(b)
                screen.blit(b.image, b.pos)
                #pygame.draw.rect(fond, (0, 0, 0, 0), b.rect)

#----------------------------------------------------------------


tab1 = Tableau('abc.png',0,600,500,0,600,100 )
tab2 = Tableau('brick-wall.png',0,200,500,500,600,600 )
tab3 = Tableau('sky.jpg',0,200,500,500,600,600 )
listetab =[tab1, tab2, tab3]
i = 0;
screen = pygame.display.set_mode((1000, 1000))
#affichageTableau(listetab[i])
perso = pygame.image.load('perso.png')
pos_pers = perso.get_rect()
listesprite = pygame.sprite.Group()
o = Personnage(perso,tab1.xdebut,tab1.ydebut-250,15)

screen.blit(o.image, o.pos)
pygame.display.flip()

pygame.key.set_repeat(20, 10)
while 1:
    k = pygame.key.get_pressed()

    #if o.pos.y < 400:
    #    o.pos.y += 2
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()

        o.deplacement(event, listesprite)

    screen.blit(o.image, o.pos)
    #if o.pos.y==400:
    o.peutsauter=True
        #print(o.pos.y)

    dessiner_niveau(screen, niveau, listesprite)
    pygame.display.flip()

    clock.tick(30)
