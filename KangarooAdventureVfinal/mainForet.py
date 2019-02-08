
import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
from tableau import Tableau
from perso import Personnage
from bloc import Bloc
from math import *
from perso import *
from sys import platform
import sys
import os

clock = pygame.time.Clock()

class chute:
    def __init__(self,coll,posblocy,heightblocy,bloctype):
        self.coll = coll
        self.posy=posblocy
        self.tailley=heightblocy
        self.bloctype=bloctype
class Horloge:
    def __init__(self,frameC):
        self.frameC = frameC



def timer(horloge,o):
    total_seconds = 180 - (horloge.frameC // 60)
    if total_seconds < 0:
        if platform == "linux" or platform == "linux2":
            commande="python3"
            savecommande="python3"
        elif platform == "win32":
            commande="py"
            savecommande="py"

        nomj=None
        if len(sys.argv)>1:
            nomj=sys.argv[1]
        commande=commande+" vueFinNiveau.py " +nomj+" "+str(o.score)+" "+str(o.compteurpiece)+" "+"0"
        pygame.quit()
        os.system(commande)
        quit()



    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = smallText.render(output_string, True,(210, 210, 210) )
    horloge.frameC += 1
    return text







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

def collipicanimal(LISTE, o, listetab, screen, bloc):
    if bloc.type == 6 or bloc.type == 7 or bloc.type == 3 or bloc.type == 9:
        o.score-=75
        LISTE.update()
        Tableau.initPerso(listetab[numtab], o, screen)
        screen.blit(listetab[numtab].background , (0,0))
        LISTE.draw(screen)
        screen.blit(o.image, o.pos)
        piece = pygame.image.load('image/piece.png')
        piece = pygame.transform.scale(piece, (20, 20))
        smallText = pygame.font.Font("freesansbold.ttf",15)
        nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
        screen.blit(piece,(0,5))
        screen.blit(nbpiece,(20,10))
        scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
        screen.blit(scA,(870,35))
        screen.blit(timer(horloge,o),(870,10))


def gestioncollDroite(listes,o):
    coll = False
    for bloc in listes:
        copyJ=o.rect.copy()
        copyJ.x+=o.speed
        if collision(copyJ,bloc.rect):
            coll=True
            collipicanimal(LISTE, o, listetab, screen, bloc)
            if bloc.type == 8:
                for i in range(100):
                    o.pos.x -=0.1
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    piece = pygame.image.load('image/piece.png')
                    piece = pygame.transform.scale(piece, (20, 20))
                    smallText = pygame.font.Font("freesansbold.ttf",15)
                    nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
                    screen.blit(piece,(0,5))
                    screen.blit(nbpiece,(20,10))
                    scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
                    screen.blit(scA,(870,35))
                    screen.blit(timer(horloge,o),(870,10))
                    pygame.display.flip()
                    pygame.time.delay(5)
            elif bloc.type ==5:
                o.compteurpiece+=1
                o.score+=75
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
            collipicanimal(LISTE, o, listetab, screen, bloc)
            if bloc.type == 8:
                for i in range(100):
                    o.pos.x +=0.1
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    piece = pygame.image.load('image/piece.png')
                    piece = pygame.transform.scale(piece, (20, 20))
                    smallText = pygame.font.Font("freesansbold.ttf",15)
                    nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
                    screen.blit(piece,(0,5))
                    screen.blit(nbpiece,(20,10))
                    scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
                    screen.blit(scA,(870,35))
                    screen.blit(timer(horloge,o),(870,10))
                    pygame.display.flip()
                    pygame.time.delay(5)
            elif bloc.type ==5:
                o.compteurpiece+=1
                o.score+=75
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
                    o.score+=75
                    listesprite.remove(bloc)
            if (o.rect.y+o.rect.height) > (bloc.rect.y+bloc.rect.height):
                #Tester si bloc.rect.y+bloc.rect.height > | < avec o.rect.y+o.rect.height

                print('COLL BAS')
                print(o.rect.y+o.rect.height)
                print(bloc.rect.y+bloc.rect.height)
                o.pos.y = bloc.rect.y+bloc.rect.height+10
                coll = True
                collipicanimal(LISTE, o, listetab, screen, bloc)

                while verifCollide(o,listesprite) == None:

                    k = pygame.key.get_pressed()
                    pygame.event.pump()
                    if(k[K_LEFT]):
                        gestioncollGauche(listesprite,o)
                        LISTE.update()
                        LISTE.draw(screen)
                    elif(k[K_RIGHT]):
                        gestioncollDroite(listesprite,o)
                        LISTE.update()
                        LISTE.draw(screen)

                    print('vers le bas')
                    LISTE.update()
                    LISTE.draw(screen)
                    o.pos.y += a
                    a+=0.4

                    if o.pos.y > 750:
                        o.pos.x = listetab[numtab].xdebut
                        o.pos.y = listetab[numtab].ydebut+10
                        break

                    pygame.time.delay(5)
                    screen.blit(listetab[numtab].background , (0,0))
                    LISTE.draw(screen)
                    screen.blit(o.image, o.pos)
                    piece = pygame.image.load('image/piece.png')
                    piece = pygame.transform.scale(piece, (20, 20))
                    smallText = pygame.font.Font("freesansbold.ttf",15)
                    nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
                    screen.blit(piece,(0,5))
                    screen.blit(nbpiece,(20,10))
                    scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
                    screen.blit(scA,(870,35))
                    screen.blit(timer(horloge,o),(870,10))
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
                collipicanimal(LISTE, o, listetab, screen, bloc)
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
            collipicanimal(LISTE, o, listetab, screen, bloc)
            if verifCollide(o,listesprite) != None:
                if bloc.type ==5:
                    o.compteurpiece+=1
                    o.score+=75
                    listesprite.remove(bloc)
    if not coll:
        test=verifCollide(o,listesprite)
        a = 2
        if(test==None):
            boucle=True
        elif(test.type==5):
            o.compteurpiece+=1
            o.scoreE+=75
            listesprite.remove(bloc)
            boucle=True
        else:
            boucle=False
        while boucle :
            LISTE.update()
            LISTE.draw(screen)
            k = pygame.key.get_pressed()
            pygame.event.pump()

            if(k[K_LEFT]):
                gestioncollGauche(listesprite,o)
            elif(k[K_RIGHT]):
                gestioncollDroite(listesprite,o)


            print('vers le bas')

            o.pos.y += a
            a+=0.4
            for bloc in listesprite:
                copyJ=o.rect.copy()
                copyJ.y+=10
                if collision(copyJ,bloc.rect):
                    if bloc.type == 4:
                        print('PRENDS LA CLEF PASSE PARTOUT')
                        pastouchesol = False
                        daronnealeo=True
                        yini=o.pos.y
                        ach=22
                        acb=4
                        o.yr=0
                        o.t=0
                        while verifCollide(o,listesprite) == None:
                            k = pygame.key.get_pressed()
                            pygame.event.pump()
                            if(k[K_LEFT]):
                                gestioncollGauche(listesprite,o)
                                gestionTombage(listesprite,o)
                                ok = False
                                break
                            elif(k[K_RIGHT]):
                                gestioncollDroite(listesprite,o)
                                gestionTombage(listesprite,o)
                                ok = False
                                break

                            print('vers le haut')

                            if(o.pos.y>yini-260 and daronnealeo):
                                o.pos.y -= ach
                                ach-=0.8
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
                            nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
                            screen.blit(piece,(0,5))
                            screen.blit(nbpiece,(20,10))
                            scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
                            screen.blit(scA,(870,35))
                            screen.blit(timer(horloge,o),(870,10))
                            #for item in LISTE:
                            #pygame.draw.rect(screen,(255,0,0), item.rect)
                            pygame.display.flip()

                            if collisionchute(listesprite,o).coll:
                                print('TOUCHE')
                                a = collisionchute(listesprite,o)
                                if a.bloctype==4:
                                    pastouchesol = False
                                    daronnealeo=True
                                    yini=o.pos.y
                                    o.pos.y-=20
                                    ach=22
                                    acb=4
                                    o.yr=0
                                    o.t=0



            if o.pos.y > 720:
                o.pos.x = listetab[numtab].xdebut
                o.pos.y = listetab[numtab].ydebut+10
                break

            pygame.time.delay(15)


            screen.blit(listetab[numtab].background , (0,0))
            LISTE.draw(screen)
            screen.blit(o.image, o.pos)
            piece = pygame.image.load('image/piece.png')
            piece = pygame.transform.scale(piece, (20, 20))
            smallText = pygame.font.Font("freesansbold.ttf",15)
            nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
            screen.blit(piece,(0,5))
            screen.blit(nbpiece,(20,10))
            scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
            screen.blit(scA,(870,35))
            screen.blit(timer(horloge,o),(870,10))
            #for item in LISTE:
                #pygame.draw.rect(screen,(255,0,0), item.rect)
            pygame.display.flip()
            test=verifCollide(o,listesprite)
            if(test==None):
                boucle=True
            elif(test.type==5):
                o.compteurpiece+=1
                o.score+=75
                listesprite.remove(bloc)
                boucle=True
            else:
                boucle=False

        x=collisionchute(listesprite,o)
        o.pos.y = x.posy-(o.rect.height+1)


GRAVITE = 9.80



numtab = 0
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption('The Infernal Kangaroo''s Adventure')

perso = pygame.image.load('image/sprite_kangoo0.png').convert_alpha()
perso = pygame.transform.smoothscale(perso,(50,50))
listesprite = pygame.sprite.Group()
o = Personnage(perso)

tab1 = Tableau('fonds/fond_foret.png', 0, 0, o, 25,675,960,990,0,1000)
tab2 = Tableau('fonds/fond_foret.png', 0, 1, o,  25,675,960,990,0,1000 )
tab3 = Tableau('fonds/fond_foret.png', 0, 2,  o, 25,505,960,990,0,1000 )
tab4 = Tableau('fonds/fond_foret.png', 0, 3,  o, 25,652,960,990,0,1000 )
tab5 = Tableau('fonds/fond_foret.png', 0, 4,  o, 25,675,960,990,0,1000 )
tab6 = Tableau('fonds/fond_foret.png', 0, 5,  o, 25,52,945,990,0,1000 )
tab7 = Tableau('fonds/fond_foret.png', 0, 6,  o, 25,52,945,990,0,1000 )
tab8 = Tableau('fonds/fond_foret.png', 0, 7,  o, 25,405,945,990,0,1000 )
tab9 = Tableau('fonds/fond_foret.png', 0, 8,  o, 25,505,945,990,0,1000 )
tab10 = Tableau('fonds/fond_foret.png', 0, 9,  o, 25,505,945,990,0,1000 )
tab11 = Tableau('fonds/fond_foret.png', 0, 10,  o, 25,60,945,990,0,1000 )
tab12 = Tableau('fonds/fond_foret.png', 0, 11,  o, 25,635,945,990,0,1000 )
tab13 = Tableau('fonds/fond_foret.png', 0, 12,  o, 25,545,945,990,0,1000 )
tab14 = Tableau('fonds/fond_foret.png', 0, 13,  o, 25,125,945,990,0,1000 )
tab14 = Tableau('fonds/fond_foret.png', 0, 14,  o, 25,670,945,990,0,1000 )
listetab =[tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14]



#affichageTableau(listetab[i])


LISTE = Tableau.dessinerTableau(listetab[numtab], screen, listesprite)
Tableau.initPerso(listetab[numtab], o, screen)

pygame.key.set_repeat(20, 10)
v_init = 2
angle_init = pi/3
v_x = cos(angle_init)*v_init
v_y = sin(angle_init)*v_init

piece = pygame.image.load('image/piece.png')
piece = pygame.transform.scale(piece, (20, 20))
smallText = pygame.font.Font("freesansbold.ttf",15)
nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))

horloge = Horloge(0)

pygame.mixer.music.load("music/musique_foret.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)


while 1:
    LISTE.update()
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        v_init = 2
        angle_init = pi/3
        v_x = cos(angle_init)*v_init
        v_y = sin(angle_init)*v_init

        if event.type == KEYDOWN:
            LISTE.update()
            if k[K_UP]:
                k = pygame.key.get_pressed()
                if(o.peutsauter):
                    k = pygame.key.get_pressed()
                    pastouchesol=True
                    sauvy=o.pos.y
                    while(pastouchesol):
                        LISTE.update()
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
                            pastouchesol = False
                            daronnealeo=True
                            yini=o.pos.y
                            if a.bloctype==4:
                                o.pos.y-=10
                                ach=22
                                acb=4
                                o.yr=0
                                o.t=0
                                while verifCollide(o,listesprite) == None:
                                    k = pygame.key.get_pressed()
                                    pygame.event.pump()
                                    if(k[K_LEFT]):
                                        gestioncollGauche(listesprite,o)
                                        gestionTombage(listesprite,o)
                                        ok = False
                                        break
                                    elif(k[K_RIGHT]):
                                        gestioncollDroite(listesprite,o)
                                        gestionTombage(listesprite,o)
                                        ok = False
                                        break

                                    print('vers le haut')

                                    if(o.pos.y>yini-260 and daronnealeo):
                                        o.pos.y -= ach
                                        ach-=0.8
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
                                    nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
                                    screen.blit(piece,(0,5))
                                    screen.blit(nbpiece,(20,10))
                                    scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
                                    screen.blit(scA,(870,35))
                                    screen.blit(timer(horloge,o),(870,10))
                                    #for item in LISTE:
                                      #pygame.draw.rect(screen,(255,0,0), item.rect)
                                    pygame.display.flip()

                                    if collisionchute(listesprite,o).coll:
                                        print('TOUCHE')
                                        a = collisionchute(listesprite,o)
                                        if a.bloctype==4:
                                            pastouchesol = False
                                            daronnealeo=True
                                            yini=o.pos.y
                                            o.pos.y-=20
                                            ach=22
                                            acb=4
                                            o.yr=0
                                            o.t=0

                            else:
                                b=verifCollide(o,listesprite)
                                if b != None:
                                    if b.type == 5:
                                        o.compteurpiece+=1
                                        o.score+=75
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
                        nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
                        screen.blit(piece,(0,5))
                        screen.blit(nbpiece,(20,10))
                        scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
                        screen.blit(scA,(870,35))
                        screen.blit(timer(horloge,o),(870,10))
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
        o.score+=1000+((numtab*100)//2)+numtab*15
        LISTE = Tableau.dessinerTableau(listetab[numtab], screen, listesprite)
        Tableau.initPerso(listetab[numtab], o, screen)

    nbpiece = smallText.render((" x " + str(o.compteurpiece)),1,(210, 210, 210))
    screen.blit(listetab[numtab].background , (0,0))
    LISTE.draw(screen)
    screen.blit(o.image, o.pos)
    screen.blit(piece,(0,5))
    screen.blit(nbpiece,(20,10))
    scA = smallText.render(("Score:"+str(o.score)),1,(210, 210, 210))
    screen.blit(scA,(870,35))
    screen.blit(timer(horloge,o),(870,10))
    #for item in LISTE:
        #pygame.draw.rect(screen,(255,0,0), item.rect)
    pygame.display.flip()


    clock.tick(60)
