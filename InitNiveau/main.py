
import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
from tableau import Tableau
from perso import Personnage
from bloc import Bloc
from table import Table
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


screen = pygame.display.set_mode((1000, 1000))

perso = pygame.image.load('perso.png')
listesprite = pygame.sprite.Group()
o = Personnage(perso,0,0,15)
tab1 = Tableau('sky2.jpg', 0, 0, o, 200,600,500,0,600,100 )
tab2 = Tableau('brick-wall.png', 0, 1, o,  0,200,500,500,600,600 )
tab3 = Tableau('sky.jpg', 0, 2,  o, 0,200,500,500,600,600 )
listetab =[tab1, tab2, tab3]



#affichageTableau(listetab[i])


Tableau.dessinerTableau(listetab[0], screen, listesprite)
pygame.display.flip()

pygame.key.set_repeat(20, 10)
while 1:
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        o.deplacement(event, listesprite)

    screen.blit(o.image, o.pos)
    o.peutsauter=True



    clock.tick(30)
