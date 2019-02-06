
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
    def __init__(self,coll,posblocy,heightblocy):
        self.coll = coll
        self.posy=posblocy
        self.tailley=heightblocy
    

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

def collisionbas(listes,o,listetab,numtab,screen,LISTE):
    a = 2
    coll = False
    for bloc in listesprite:
        if o.rect.colliderect(bloc.rect):
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
                    a+=0.2
                    
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    #pygame.draw.rect(screen,(0,255,0), o.rect)
                    #for item in LISTE:
                        #pygame.draw.rect(screen,(255,0,0), item.rect)
                    pygame.display.flip()

                o.pos.y -=10
                
    return coll

def collisionchute(listes,o):

    blocposy = 0
    bloctailley = 0
    coll=False
    for bloc in listesprite:
        if o.rect.colliderect(bloc.rect):
            if (o.rect.y+o.rect.height) < (bloc.rect.y+bloc.rect.height):
                coll=True
                blocposy=bloc.rect.y
                bloctailley=bloc.rect.height
                

                                
    c = chute(coll,blocposy,bloctailley)
    
    return c



def gestionTombage(listes,o):

    coll = False
    for bloc in listesprite:
        copyJ=o.rect.copy()
        copyJ.y+=10
        if collision(copyJ,bloc.rect):
            coll=True
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
            a+=0.2
                    
            screen.blit(listetab[numtab].background , (0,0))
            LISTE.draw(screen)
            screen.blit(o.image, o.pos)
            #pygame.draw.rect(screen,(0,255,0), o.rect)
            #for item in LISTE:
                #pygame.draw.rect(screen,(255,0,0), item.rect)
            pygame.display.flip()

            if o.pos.y > 1000:
                o.pos.x = 200
                o.pos.y = 600
                break

        o.pos.y -=10
        


GRAVITE = 7.81


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

                        if collisionchute(listesprite,o).coll:
                            a = collisionchute(listesprite,o)
                            o.yr=0
                            o.t=0
                            o.pos.y = a.posy-(o.rect.height+1)
                            pastouchesol=False

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

                        if o.pos.y > 1000:
                            o.pos.x = 200
                            o.pos.y = 600
                            o.yr=0
                            o.t=0
                            break
                            


                        if(k[K_LEFT]):
                                gestioncollGauche(listesprite,o)
                        elif(k[K_RIGHT]):
                                gestioncollDroite(listesprite,o)

                        pygame.time.delay(10)
                        screen.blit(listetab[numtab].background , (0,0))
                        LISTE.draw(screen)
                        screen.blit(o.image, o.pos)
                        #pygame.draw.rect(screen,(0,255,0), o.rect)
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

    if o.pos.y > 1000:
        o.pos.x = 200
        o.pos.y = 600

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
    #pygame.draw.rect(screen,(0,255,0), o.rect)
    #for item in LISTE:
        #pygame.draw.rect(screen,(255,0,0), item.rect)
    pygame.display.flip()


    clock.tick(60)
