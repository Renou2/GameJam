import sys, pygame
from pygame.locals import *
from math import *
pygame.init()

clock = pygame.time.Clock()

GRAVITE = 8.81
PI = 3.14

class Personnage(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.pos = pygame.Rect(200, 700, 110, 110)
        #posAbsolue
        self.xa = 200
        self.ya = 700
        self.t=0
        #posrelative
        self.xr = 0
        self.yr = 0
        self.v_x = 1.5
        self.v_saut = -6
        self.v_y = self.v_saut
        self.peutsauter=True
        self.speed = 5
        self.droite=False
        self.gauche=False










screen = pygame.display.set_mode((1000, 900))

fondm = pygame.image.load('brick-wall.png').convert()
fondm = pygame.transform.smoothscale(fondm, (1000, 900))
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

def dessiner_niveau(surface, niveau):

    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                screen.blit(block, (i*50, j*50))

perso = pygame.image.load('perso.png').convert()
o = Personnage(perso)

screen.blit(o.image, o.pos)

pygame.display.flip()

#pygame.key.set_repeat(20, 10)
t = 0
v_init = 2
angle_init = pi/3
v_x = cos(angle_init)*v_init
v_y = sin(angle_init)*v_init
pygame.key.set_repeat(5, 5)
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
                        if(k[K_LEFT]):
                            o.pos.x-=o.speed
                        elif(k[K_RIGHT]):
                            o.pos.x+=o.speed
                        if o.pos.x > 1000:
                            o.pos.x = 0
                        if(o.pos.y>700):
                            o.yr=0
                            o.ya = 700
                            o.t=0
                            pastouchesol=False
                        pygame.time.delay(10)
                        screen.blit(fondm, (0,0))
                        screen.blit(o.image, o.pos)
                        dessiner_niveau(screen, niveau)
                        pygame.display.flip()
                        

                    pygame.event.clear()


            elif(k[K_LEFT] ):
                o.pos.x-=o.speed
            elif(k[K_RIGHT]):
                o.pos.x+=o.speed

        if event.type == KEYUP:
            if k[K_UP]:
                o.peutsauter=False
                print('lacherHaut---UP')

            elif k[K_LEFT] :
                o.gauche=False
                print('lacherHaut---LEFT')
            elif k[K_RIGHT] :
                o.droite=False
                print('lacherHaut---RIGHT')


    if o.pos.x > 1000:
        o.pos.x = 0

    if o.pos.y < 700:
        o.pos.y = o.pos.y + 5
        o.ya=o.pos.y

    if o.pos.y>690:
        o.peutsauter=True

 #DEBUT NEWTON
#     #posAbsolue a 0
#     o.ya = 700
#     #//On calcule la valeur relative de y:
#     o.yr=(int)((v_y*t)-((GRAVITE*t*t)/2000))
#
#     #//On calcule maintenant les valeurs absolues
#     o.ya = o.ya - o.yr
#     o.pos.y=o.ya
#     t+=10
#     if(o.pos.y>700):
#         o.yr=0
#         o.ya = 700
#         o.pos.y=o.ya
#         t=0
#
#     pygame.time.delay(10)
# #FIN NEWTON






    screen.blit(fondm, (0,0))
    screen.blit(o.image, o.pos)
    dessiner_niveau(screen, niveau)
    pygame.display.flip()

    clock.tick(60)
