import sys, pygame
from pygame.locals import *
pygame.init()
from sys import exit
import perso
from bloc import Bloc

#Init fond
screen = pygame.display.set_mode((1000, 1000))
fond = pygame.image.load('sky.jpg')
screen.blit(fond, (0,0))

#>Init perso
person = pygame.image.load('perso.png')
o = perso.Personnage(person,200,300,10)

#Init Bloc
imbloc = pygame.image.load('Rectangle_.png')
b = Bloc(imbloc, 900, 900, 1, (-1,-1))
b.rect.width=1
b.rect.height=1

o.rect.width=25
o.rect.height=25

#Init Groupe
g = pygame.sprite.Group()
g.add(b)

pygame.key.set_repeat(400, 30)
while 1:
    g.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                o.moveDown()
                if  pygame.sprite.collide_rect(o,b) :
                    b.vector = (0,0)
                    o.moveUp()
            if event.key == K_UP:
                o.moveUp()
                if  pygame.sprite.collide_rect(o,b) :
                    b.vector = (0,0)
                    o.moveDown()
            if event.key == K_LEFT:
                o.moveLeft()
                if  pygame.sprite.collide_rect(o,b) :
                    b.vector = (0,0)
                    o.moveRight()
            if event.key == K_RIGHT:
                o.moveRight()
                if  pygame.sprite.collide_rect(o,b) :
                    b.vector = (0,0)
                    o.moveLeft()
            if event.key == K_ESCAPE :
                pygame.display.quit()
                pygame.quit()
                exit(0)
    g.draw(fond)

    #s = pygame.sprite.spritecollideany(o, g)

    print(b.vector)
    #print(b.rect )
    #print(o.rect )
    screen.blit(b.image, b.pos)
    screen.blit(o.image, o.pos)
    #else : b.vector = (-1,-1)
    pygame.display.flip()

pygame.time.delay(1)
