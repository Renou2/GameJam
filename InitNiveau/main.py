
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




GRAVITE = 9.81


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
v_init = 2
angle_init = pi/3
v_x = cos(angle_init)*v_init
v_y = sin(angle_init)*v_init

while 1:
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        v_init = 2
        angle_init = pi/3
        v_x = cos(angle_init)*v_init
        v_y = sin(angle_init)*v_init

        if event.type == KEYDOWN:
            if k[K_UP]:
                k = pygame.key.get_pressed()
                if(o.peutsauter):
                    k = pygame.key.get_pressed()
                    pastouchesol=True
                    while(pastouchesol):
                        k = pygame.key.get_pressed()
                        o.ya = 700
                        #//On calcule la valeur relative de y:
                        o.yr=(int)((v_y*o.t)-((GRAVITE*o.t*o.t)/2000))
                        #//On calcule maintenant les valeurs absolues
                        o.ya = o.ya - o.yr
                        o.pos.y=o.ya
                        o.t+=10

                        k = pygame.key.get_pressed()
                        pygame.event.pump()
                        if(o.pos.y>700):
                            o.yr=0
                            o.ya = 700
                            o.t=0
                            pastouchesol=False

                        if(k[K_LEFT]):
                                o.pos.x-=o.speed
                        elif(k[K_RIGHT]):
                                o.pos.x+=o.speed
                        if o.pos.x > 1000:
                            o.pos.x = 0




                        pygame.time.delay(10)
                        screen.blit(listetab[numtab].background , (0,0))
                        LISTE.draw(screen)
                        screen.blit(o.image, o.pos)
                        pygame.draw.rect(screen,(0,255,0), o.rect)
                        pygame.display.flip()


                    pygame.event.clear()

            elif(k[K_LEFT] ):
                o.gauche=True
                print(k[K_LEFT])
                o.droite=False
            elif(k[K_RIGHT]):
                o.droite=True
                o.gauche=False

        if event.type == KEYUP:
            if k[K_UP]:
                o.peutsauter=False
                o.gauche=False
                o.droite=False
                print('lacherHaut---UP')
            elif k[K_LEFT] :
                o.gauche=False
                print('lacherHaut---LEFT')
            elif k[K_RIGHT] :
                o.droite=False
                print('lacherHaut---RIGHT')


    k = pygame.key.get_pressed()
    if k[K_RIGHT]:
        if o.droite:
            if  verifCollide(o, listesprite):
                o.pos.x -= o.speed+20
            else:
                o.pos.x+=o.speed
    elif k[K_LEFT]:
        if o.gauche:
            if  verifCollide(o, listesprite):
                o.pos.x += o.speed+20
            else:
                o.pos.x-=o.speed

    if o.pos.x > 1000:
        o.pos.x = 0

    pygame.time.delay(5)

    o.peutsauter=True


    if Tableau.verifSortie(listetab[numtab], o):
        LISTE.empty()
        #LISTE.clear(screen, listetab[numtab].background)
        numtab+=1
        LISTE = Tableau.dessinerTableau(listetab[numtab], screen, listesprite)
        Tableau.initPerso(listetab[numtab], o, screen)



    screen.blit(listetab[numtab].background , (0,0))
    LISTE.draw(screen)
    screen.blit(o.image, o.pos)
    pygame.draw.rect(screen,(0,255,0), o.rect)
    for item in LISTE:
        pygame.draw.rect(screen,(255,0,0), item.rect)
    pygame.display.flip()


    clock.tick(60)
