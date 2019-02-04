import pygame
import os
from pygame.locals import *
from constantes import *


pygame.init()

frame = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), RESIZABLE)

icone = pygame.image.load(image).convert()
frame.blit(icone, (0,0))
pygame.display.flip()

smallText = pygame.font.Font("freesansbold.ttf",20)

titreRegles = smallText.render("Règles du jeu", 1, (40,40,40))
nom
frame.blit(regles, (100,100))
pygame.display.flip()

continuer = 1
while continuer:
    continue
