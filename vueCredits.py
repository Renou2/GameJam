import pygame
from pygame.locals import *



def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Nom du jeu')


    #Panel de button


    fond = pygame.image.load('fond.png').convert()
    fond = pygame.transform.scale(fond, (400, 300))
    fond = fond.convert_alpha()
    screen.blit(fond, (0, 0))
    pygame.display.update()

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(fond, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
