
import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
from tableau import Tableau
from perso import Personnage
from bloc import Bloc
from math import *
from perso import *
clock = pygame.time.Clock()

numtab = 0
screen = pygame.display.set_mode((1000, 750))

perso = pygame.image.load('perso.png')
o = Personnage(perso)
tab1 = Tableau('sky2.jpg', 0, 0, o, 200,300,500,1000,0,500 )
tab2 = Tableau('sky.jpg', 0, 1, o,  200,600,500,1000,0,500 )
tab3 = Tableau('foret.jpg', 0, 2,  o, 200,600,500,1000,0,500 )
listetab =[tab1, tab2, tab3]

BLACK = (0, 0, 0)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 180

#affichageTableau(listetab[i])


LISTE = Tableau.dessinerTableau(listetab[numtab], screen)
Tableau.initPerso(listetab[numtab], o, screen)

pygame.key.set_repeat(20, 10)
v_init = 2
angle_init = pi/3
v_x = cos(angle_init)*v_init
v_y = sin(angle_init)*v_init

while 1:
    #TIMER
    total_seconds = frame_count // frame_rate
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [875, 0])
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()
    #FINTIMER
    o.update()
    collide = pygame.sprite.spritecollide(o, LISTE, False)
    if collide:
        o.pos.y = collide[0].rect.top-25
        o.vel.y = 0



    #if Tableau.verifSortie(listetab[numtab], o):
    #    LISTE.empty()
    #    #LISTE.clear(screen, listetab[numtab].background)
    #    numtab+=1
    #    LISTE = Tableau.dessinerTableau(listetab[numtab], screen, listesprite)
    #    Tableau.initPerso(listetab[numtab], o, screen)



    screen.blit(listetab[numtab].background , (0,0))
    LISTE.draw(screen)
    screen.blit(o.image, o.pos)
    pygame.display.flip()


    #clock.tick(60)
