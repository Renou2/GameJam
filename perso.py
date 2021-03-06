import sys, pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

class Personnage(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.pos = pygame.Rect(200, 300, 110, 110)
        self.v_x = 1.5
        self.v_saut = -4
        self.v_gravitation = 0.08
        self.v_y = self.v_saut
        self.var = self.pos.y
        self.speed = 5
        
    def deplacement(self):
        if event.type == KEYDOWN:
            if k[K_UP]:
                self.pos.y += self.v_y

                self.v_y += self.v_gravitation

                if self.v_y > 5:
                    self.v_y = self.v_saut

            if k[K_RIGHT]:
                self.pos.x += self.speed

                if k[K_RIGHT] and k[K_UP]:
                    self.pos.x += self.v_x
                    self.pos.y += self.v_y
                    
                    self.v_y += self.v_gravitation
                     
                    if self.v_y > 5:
                        self.v_y = self.v_saut

            if k[K_LEFT]:
                self.pos.x -= self.speed
                   
                if k[K_LEFT] and k[K_UP]:
                    self.pos.x -= self.v_x
                    self.pos.y += self.v_y
                    
                    self.v_y += self.v_gravitation

                     
                    if self.v_y > 5:
                        self.v_y = self.v_saut
                
        elif event.type == KEYUP:
               
            if k[K_UP]:

                a = self.var - self.pos.y
                print(a)
                b = 0
                
                while b < a:
                    self.pos.y += 1
                    b = b + 1
                    
                    screen.blit(fond, (0,0))
                    screen.blit(o.image, o.pos)
                    pygame.display.flip()
                
                self.v_y = self.v_saut
                self.var = self.pos.y
            
                

screen = pygame.display.set_mode((600, 600))

fond = pygame.image.load('brick-wall.png')
perso = pygame.image.load('perso.png')
o = Personnage(perso)

screen.blit(fond, (0,0))
screen.blit(o.image, o.pos)

pygame.display.flip()

pygame.key.set_repeat(20, 10)
while 1:
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
          o.deplacement()
          
    screen.blit(fond, (0,0))
    screen.blit(o.image, o.pos)

    pygame.display.flip()
    clock.tick(60)
