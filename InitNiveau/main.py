
import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
from tableau import Tableau
from perso import Personnage
from bloc import Bloc
clock = pygame.time.Clock()

GRAVITE = 0.08


numtab = 0
screen = pygame.display.set_mode((1000, 1000))

perso = pygame.image.load('perso.png')
listesprite = pygame.sprite.Group()
o = Personnage(perso)
tab1 = Tableau('sky2.jpg', 0, 0, o, 200,600,500,1000,0,500 )
tab2 = Tableau('sky.jpg', 0, 1, o,  200,600,500,1000,0,500 )
tab3 = Tableau('foret.jpg', 0, 2,  o, 200,600,500,1000,0,500 )
listetab =[tab1, tab2, tab3]



#affichageTableau(listetab[i])


LISTE = Tableau.dessinerTableau(listetab[numtab], screen, listesprite)
Tableau.initPerso(listetab[numtab], o, screen)

pygame.key.set_repeat(20, 10)
while 1:
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        o.deplacement(event, listesprite)
        if Tableau.verifSortie(listetab[numtab], o):
            LISTE.empty()
            #LISTE.clear(screen, listetab[numtab].background)
            numtab+=1
            LISTE = Tableau.dessinerTableau(listetab[numtab], screen, listesprite)
            Tableau.initPerso(listetab[numtab], o, screen)

    o.peutsauter=True

    pygame.display.flip()


    clock.tick(30)
