import pygame
from pygame.locals import *
from sys import platform
import os



def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Nom du jeu')


    #Panel de button
    x=150
    y=80
    largB=100
    hautB=50

    x2=150
    y2=150

    y3=220

    fond = pygame.image.load('fond.png').convert()
    fond = pygame.transform.scale(fond, (400, 300))
    fond = fond.convert_alpha()

    bjouer=pygame.draw.rect(fond, (200,200,200),(x,y,largB,hautB))
    bregle=pygame.draw.rect(fond, (200,200,200),(x2,y2,largB,hautB))
    bcredit=pygame.draw.rect(fond, (200,200,200),(x2,y3,largB,hautB))


    # Test sur l'os
    if platform == "linux" or platform == "linux2":
        commande="python3"
    elif platform == "win32":
        commande="py"


    screen.blit(fond, (0, 0))
    pygame.display.update()

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if bjouer.collidepoint(event.pos):
                        print("vous avez clicker sur jouer")
                        commande=commande+" vueChoixPerso.py"
                        pygame.quit()
                        os.system(commande)
                        return
                    elif bregle.collidepoint(event.pos):
                        print("vous avez clicker sur Regles")
                    elif bcredit.collidepoint(event.pos):
                        print("vous avez clicker sur Credit")
                        commande=commande+" vueCredits.py"
                        os.system(commande)
                        commande="py"


        mouse = pygame.mouse.get_pos()
        smallText = pygame.font.Font("freesansbold.ttf",20)

        if x+largB > mouse[0] > x and y+hautB > mouse[1] > y:
            bjouer=pygame.draw.rect(fond, (255, 153, 0),(x ,y,largB,hautB))
        else:
            bjouer=pygame.draw.rect(fond, (204, 122, 0),(x,y,largB,hautB))

        textBJouer = smallText.render("JOUER",1,(40, 40, 40))
        fond.blit(textBJouer, (x+15,y+15) )

        if x2+largB > mouse[0] > x2 and y2+hautB > mouse[1] > y2:
            bregle=pygame.draw.rect(fond, (255, 153, 0),(x2 ,y2,largB,hautB))
        else:
            bregle=pygame.draw.rect(fond, (204, 122, 0),(x2,y2,largB,hautB))

        textBRegle = smallText.render("RÉGLES",1,(40, 40, 40))
        fond.blit(textBRegle, (x2+10,y2+15) )

        if x2+largB > mouse[0] > x2 and y3+hautB > mouse[1] > y3:
            bcredit=pygame.draw.rect(fond, (255, 153, 0),(x2 ,y3,largB,hautB))
        else:
            bcredit=pygame.draw.rect(fond, (204, 122, 0),(x2,y3,largB,hautB))

        textBCred = smallText.render("CRÉDITS",1,(40, 40, 40))
        fond.blit(textBCred, (x2+7,y3+15) )

        screen.blit(fond, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
