
import sys
import pygame as pg
pg.init()
from sys import exit
from tableau import Tableau
from perso import Personnage
from bloc import Bloc
from math import *
from perso import *


clock = pg.time.Clock()

numtab = 0
screen = pg.display.set_mode((500, 500))

perso = pg.image.load('perso.png')
o = Personnage(perso)
tab1 = Tableau('sky2.jpg', 0, 0, o, 100,100,500,1000,0,500 )
tab2 = Tableau('sky.jpg', 0, 1, o,  200,600,500,1000,0,500 )
tab3 = Tableau('foret.jpg', 0, 2,  o, 200,600,500,1000,0,500 )
listetab =[tab1, tab2, tab3]
#affichageTableau(listetab[i])


LISTE = Tableau.dessinerTableau(listetab[numtab], screen)
Tableau.initPerso(listetab[numtab], o, screen)

pg.key.set_repeat(20, 10)
v_init = 2
angle_init = pi/3
v_x = cos(angle_init)*v_init
v_y = sin(angle_init)*v_init

while 1:
    clock.tick(60)
    o.update(LISTE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            if self.playing:
                self.playing = False
                self.running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                o.jump(LISTE)



    if o.vel.y > 0:
        hits = pg.sprite.spritecollide(o, LISTE, False)
        if hits:
            if o.pos.y < hits[0].rect.bottom:
                o.pos.y = hits[0].rect.top
                o.vel.y = 0

#    if o.vel.y < 0:
#                hits = pg.sprite.spritecollide(o, LISTE, False)
#                if hits:
#                    if o.pos.y > hits[0].rect.bottom:
#                        print(12)
#                        o.pos.y = hits[0].rect.bottom
#                        o.vel.y = 0
#                        o.acc.y = 0.5
    if o.vel.x <= 0:
        o.rect.x -= 1
        o.rect.y-=10
        collide = pg.sprite.spritecollide(o, LISTE, False)
        o.rect.x+=1
        o.rect.y += 10
        if collide:
            o.vel.x = 0.5
    if o.vel.x >= 0 :
        o.rect.x += 1
        o.rect.y-=10
        collide = pg.sprite.spritecollide(o, LISTE, False)
        o.rect.x-=1
        o.rect.y += 10
        if collide:
            o.vel.x = -0.5


    pg.draw.rect(screen,(0,255,0), o.rect)
    for item in LISTE:
        pg.draw.rect(screen,(255,0,0), item.rect)
    pg.display.flip()

    screen.blit(listetab[numtab].background , (0,0))
    LISTE.draw(screen)
    screen.blit(o.image, o.pos)
    pg.display.flip()


    #clock.tick(60)
