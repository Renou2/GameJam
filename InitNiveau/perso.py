
import sys, pygame
from pygame.locals import *
pygame.init()
import tableau
GRAVITE = 0.08



class Personnage(pygame.sprite.Sprite):
    def __init__(self, image):
        self.speed = 15
        self.image = image
        self.rect = image.get_rect()
        self.pos = pygame.Rect(200, 200, 25, 36)
        self.peutsauter=False
        self.v_x = 1.5
        self.v_saut = -6
        self.v_y = self.v_saut
    def deplacement(self, event, listesprite):
        if event.type == KEYDOWN:
            k = pygame.key.get_pressed()
#            if k[K_UP]:
#                if self.peutsauter:
#                    self.pos.y += self.v_y
#                    self.v_y += GRAVITE
#                    self.rect=self.pos
#                    #print("fleche haut")
#
#                    if self.v_y > 0:
#                        self.v_y = self.v_saut
#                        self.peutsauter=False
#                    if verifCollide(self, listesprite):
#                        self.pos.y -= self.speed
#                    #verifSortie(self, i, listetab)
            if k[K_UP]:
                self.pos.y -= self.speed
                self.rect=self.pos
                #verifSortie(self, i, listetab)
                print(verifCollide(self, listesprite))
                if  verifCollide(self, listesprite):
                    self.pos.y += self.speed

            if k[K_RIGHT]:
                self.pos.x += self.speed
                self.rect=self.pos
                #verifSortie(self, i, listetab)
                print(verifCollide(self, listesprite))
                if  verifCollide(self, listesprite):
                    self.pos.x -= self.speed

            if k[K_LEFT]:
                self.pos.x -= self.speed
                self.rect=self.pos
                #verifSortie(self, i, listetab)
                if  verifCollide(self, listesprite):
                    self.pos.x += self.speed
            if k[K_DOWN]:
                self.pos.y += self.speed
                self.rect=self.pos
                #verifSortie(self, i, listetab)
                print(verifCollide(self, listesprite))
                if  verifCollide(self, listesprite):
                    self.pos.y -= self.speed

            if k[K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit(0)

def verifCollide(perso, listesprite):
    for sprite in listesprite:
        #print(sprite)
        if  pygame.sprite.collide_rect(perso,sprite) :
            return True
    return False
