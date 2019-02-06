
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


def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True

def gestioncollDroite(listes,o):
    coll = False
    for bloc in listes:
        copyJ=o.rect.copy()
        copyJ.x+=o.speed
        if collision(copyJ,bloc.rect):
            coll=True
    if not coll :
        o.pos.x+=o.speed

def gestioncollGauche(listes,o):
    coll = False
    for bloc in listesprite:
        copyJ=o.rect.copy()
        copyJ.x-=o.speed
        if collision(copyJ,bloc.rect):
            coll=True
    if not coll :
        o.pos.x-=o.speed

def collisionbas(listes,o):
    coll = False
    for bloc in listesprite:
        if o.rect.colliderect(bloc.rect):
            if bloc.rect.top < o.rect.bottom: #Tester si bloc.rect.y+bloc.rect.height > | < avec o.rect.y+o.rect.height
                print('COLL BAS')
                coll=True

        if coll:
            o.pos.y-5
    return coll


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
                    sauvy=o.pos.y
                    while(pastouchesol):
                        o.ya=sauvy
                        k = pygame.key.get_pressed()
                        old_x = o.pos.x
                        old_y = o.pos.y

                        #//On calcule la valeur relative de y:
                        o.yr=(int)((v_y*o.t)-((GRAVITE*o.t*o.t)/2000))
                        #//On calcule maintenant les valeurs absolues
                        o.ya = o.ya - o.yr
                        o.pos.y=o.ya
                        if(collisionbas(listesprite,o)):
                            o.yr=0
                            o.t=0
                            o.pos.y=old_y
                            pastouchesol=False

                        #o.pos.y=o.ya
                        o.t+=10

                        k = pygame.key.get_pressed()
                        pygame.event.pump()

                        if o.pos.x > 1000:
                            o.pos.x = 0


                        if(k[K_LEFT]):
                                gestioncollGauche(listesprite,o)
                        elif(k[K_RIGHT]):
                                gestioncollDroite(listesprite,o)

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
            gestioncollDroite(listesprite,o)


    elif k[K_LEFT]:
        if o.gauche:
            gestioncollGauche(listesprite,o)

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
