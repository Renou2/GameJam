
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

class chute:
    def __init__(self,coll,posblocy,heightblocy,bloctype):
        self.coll = coll
        self.posy=posblocy
        self.tailley=heightblocy
        self.bloctype=bloctype


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
            if bloc.type == 8:
                for i in range(100):
                    o.pos.x -=0.1
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    pygame.display.flip()
                    pygame.time.delay(5)
            elif bloc.type ==5:
                o.compteurpiece+=1
                listesprite.remove(bloc)
    if not coll :
        o.pos.x+=o.speed

def gestioncollGauche(listes,o):
    coll = False
    for bloc in listesprite:
        copyJ=o.rect.copy()
        copyJ.x-=o.speed
        if collision(copyJ,bloc.rect):
            coll=True
            if bloc.type == 8:
                for i in range(100):
                    o.pos.x +=0.1
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    pygame.display.flip()
                    pygame.time.delay(5)
            elif bloc.type ==5:
                o.compteurpiece+=1
                listesprite.remove(bloc)

    if not coll :
        o.pos.x-=o.speed

def collisionbas(listes,o,listetab,numtab,screen,LISTE):
    a = 2
    coll = False
    for bloc in listesprite:
        if o.rect.colliderect(bloc.rect):
            if verifCollide(o,listesprite) != None:
                if bloc.type ==5:
                    o.compteurpiece+=1
                    listesprite.remove(bloc)
            if (o.rect.y+o.rect.height) > (bloc.rect.y+bloc.rect.height):
                #Tester si bloc.rect.y+bloc.rect.height > | < avec o.rect.y+o.rect.height

                print('COLL BAS')
                print(o.rect.y+o.rect.height)
                print(bloc.rect.y+bloc.rect.height)
                o.pos.y = bloc.rect.y+bloc.rect.height+10
                coll = True


                while verifCollide(o,listesprite) == None:


                    k = pygame.key.get_pressed()
                    pygame.event.pump()

                    if(k[K_LEFT]):
                        gestioncollGauche(listesprite,o)
                    elif(k[K_RIGHT]):
                        gestioncollDroite(listesprite,o)

                    print('vers le bas')

                    o.pos.y += a
                    a+=0.4

                    if o.pos.y > 750:
                        o.pos.x = listetab[numtab].xdebut
                        o.pos.y = listetab[numtab].ydebut+10
                        break

                    pygame.time.delay(15)
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    pygame.draw.rect(screen,(0,255,0), o.rect)
                    #for item in LISTE:
                        #pygame.draw.rect(screen,(255,0,0), item.rect)
                    pygame.display.flip()

                o.pos.y -=10

    return coll

def collisionchute(listes,o):

    blocposy = 0
    bloctailley = 0
    bloctype=None
    coll=False
    for bloc in listesprite:
        if o.rect.colliderect(bloc.rect):
            if (o.rect.y+o.rect.height) < (bloc.rect.y+bloc.rect.height):
                coll=True
                blocposy=bloc.rect.y
                bloctailley=bloc.rect.height
                bloctype=bloc.type

    c = chute(coll,blocposy,bloctailley,bloctype)


    return c

def gestionTombage(listes,o):

    coll = False
    for bloc in listesprite:
        copyJ=o.rect.copy()
        copyJ.y+=10
        if collision(copyJ,bloc.rect):
            coll=True
            if verifCollide(o,listesprite) != None:
                if bloc.type ==5:
                    o.compteurpiece+=1
                    listesprite.remove(bloc)
    if not coll:
        a=2
        while verifCollide(o,listesprite) == None:

            k = pygame.key.get_pressed()
            pygame.event.pump()

            if(k[K_LEFT]):
                gestioncollGauche(listesprite,o)
            elif(k[K_RIGHT]):
                gestioncollDroite(listesprite,o)

            print('vers le bas')

            o.pos.y += a
            a+=0.4

            if o.pos.y > 720:
                o.pos.x = listetab[numtab].xdebut
                o.pos.y = listetab[numtab].ydebut+10
                break

            pygame.time.delay(15)


            screen.blit(listetab[numtab].background , (0,0))
            LISTE.draw(screen)
            screen.blit(o.image, o.pos)
            pygame.draw.rect(screen,(0,255,0), o.rect)
            #for item in LISTE:
                #pygame.draw.rect(screen,(255,0,0), item.rect)
            pygame.display.flip()

        x=collisionchute(listesprite,o)
        o.pos.y = x.posy-(o.rect.height+1)


GRAVITE = 7.01


numtab = 0
screen = pygame.display.set_mode((1000, 750))

perso = pygame.image.load('sprite_kangoo0.png').convert_alpha()
perso = pygame.transform.smoothscale(perso,(50,50))
listesprite = pygame.sprite.Group()
o = Personnage(perso)
tab1 = Tableau('fond_glacier.png', 1, 0, o, 25,675,960,990,0,1000)
tab2 = Tableau('fond_glacier.png', 1, 1, o,  25,675,960,990,0,1000 )
tab3 = Tableau('fond_glacier.png', 1, 2,  o, 25,505,960,990,0,1000 )
tab4 = Tableau('fond_glacier.png', 1, 3,  o, 25,652,960,990,0,1000 )
tab5 = Tableau('fond_glacier.png', 1, 4,  o, 25,675,960,990,0,1000 )
tab6 = Tableau('fond_glacier.png', 1, 5,  o, 25,52,945,990,0,1000 )
tab7 = Tableau('fond_glacier.png', 1, 6,  o, 25,52,945,990,0,1000 )
tab8 = Tableau('fond_glacier.png', 1, 7,  o, 25,405,945,990,0,1000 )
tab9 = Tableau('fond_glacier.png', 1, 8,  o, 25,505,945,990,0,1000 )
tab10 = Tableau('fond_glacier.png', 1, 9,  o, 25,505,945,990,0,1000 )
tab11 = Tableau('fond_glacier.png', 1, 10,  o, 25,60,945,990,0,1000 )
tab12 = Tableau('fond_glacier.png', 1, 11,  o, 25,635,945,990,0,1000 )
tab13 = Tableau('fond_glacier.png', 1, 12,  o, 25,545,945,990,0,1000 )
tab14 = Tableau('fond_glacier.png', 1, 13,  o, 25,125,945,990,0,1000 )
tab15 = Tableau('fond_glacier.png', 1, 14,  o, 25,670,945,990,0,1000 )
listetab =[tab1, tab2, tab3, tab4, tab5, tab6, tab11, tab12, tab13, tab14, tab15, tab1, tab2, tab3, tab4, tab5, tab6, tab11, tab12, tab13, tab14, tab15]



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

                        if collisionchute(listesprite,o).coll:
                            a = collisionchute(listesprite,o)

                            daronnealeo=True
                            yini=o.pos.y
                            if a.bloctype==4:
                                o.pos.y-=10
                                ach=4
                                acb=4
                                o.yr=0
                                o.t=0
                                while verifCollide(o,listesprite) == None:
                                    k = pygame.key.get_pressed()
                                    pygame.event.pump()
                                    if(k[K_LEFT]):
                                        gestioncollGauche(listesprite,o)
                                    elif(k[K_RIGHT]):
                                        gestioncollDroite(listesprite,o)

                                    print('vers le haut')

                                    if(o.pos.y>yini-100 and daronnealeo):
                                        o.pos.y -= ach
                                        ach+=0.5
                                        print('a')
                                    else:
                                        o.pos.y += acb
                                        acb+=0.5
                                        daronnealeo=False

                                    if o.pos.y > 750:
                                        o.pos.x = listetab[numtab].xdebut
                                        o.pos.y = listetab[numtab].ydebut+10
                                        break
                                    pygame.time.delay(15)
                                    screen.blit(listetab[numtab].background , (0,0))
                                    LISTE.draw(screen)
                                    screen.blit(o.image, o.pos)
                                    pygame.draw.rect(screen,(0,255,0), o.rect)
                                    #for item in LISTE:
                                      #pygame.draw.rect(screen,(255,0,0), item.rect)
                                    pygame.display.flip()

                            else:
                                b=verifCollide(o,listesprite)
                                if b != None:
                                    if b.type == 5:
                                        o.compteurpiece+=1
                                        listesprite.remove(b)

                                o.yr=0
                                o.t=0
                                o.pos.y = a.posy-(o.rect.height+1)
                                break
                                print('Collision en CHUTE libre')

                        elif(collisionbas(listesprite,o,listetab,numtab,screen,LISTE)):
                            o.yr=0
                            o.t=0
                            pastouchesol=False
                            print('Collision en bas')


                        #o.pos.y=o.ya
                        o.t+=10

                        k = pygame.key.get_pressed()
                        pygame.event.pump()

                        if o.pos.x > 1000:
                            o.pos.x = 0
                        if o.pos.y > 750:
                            o.pos.x = listetab[numtab].xdebut
                            o.pos.y = listetab[numtab].ydebut
                            o.yr=0
                            o.t=0
                            break



                        if(k[K_LEFT]):
                                gestioncollGauche(listesprite,o)
                        elif(k[K_RIGHT]):
                                gestioncollDroite(listesprite,o)

                        pygame.time.delay(15)
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
            gestionTombage(listesprite,o)


    elif k[K_LEFT]:
        if o.gauche:
            gestioncollGauche(listesprite,o)
            gestionTombage(listesprite,o)

    if o.pos.x > 1000:
        o.pos.x = 0

    if o.pos.y > 750 or o.pos.y<0:
        o.pos.x = listetab[numtab].xdebut
        o.pos.y = listetab[numtab].ydebut+10

    pygame.time.delay(15)

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
    #for item in LISTE:
        #pygame.draw.rect(screen,(255,0,0), item.rect)
    pygame.display.flip()


    clock.tick(60)
