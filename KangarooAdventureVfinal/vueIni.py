import pygame
from pygame.locals import *
from sys import platform
import os


def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((630, 500))
    pygame.display.set_caption('The Infernal Kangaroo''s Adventure - Acceuil')

    xk =-150
    yk =350


    #Panel de button
    x=260
    y=150
    largB=100
    hautB=50

    y2=220

    y3=290

    fond = pygame.image.load('fonds/foret.jpg').convert()
    # fond = pygame.transform.scale(fond, (400, 300))
    fond = fond.convert_alpha()

    bjouer=pygame.draw.rect(screen, (200,200,200),(x,y,largB,hautB))
    bregle=pygame.draw.rect(screen, (200,200,200),(x,y2,largB,hautB))
    bcredit=pygame.draw.rect(screen, (200,200,200),(x,y3,largB,hautB))

    kangoo = pygame.image.load('image/kangoo0.png').convert_alpha()
    kangoo2 = pygame.image.load('image/kangoo1.png').convert_alpha()
    kangoo = pygame.transform.smoothscale(kangoo, (150,150))
    kangoo2 = pygame.transform.smoothscale(kangoo2, (150,150))
    # Test sur l'os
    if platform == "linux" or platform == "linux2":
        commande="python3"
        savecommande="python3"
    elif platform == "win32":
        commande="py"
        savecommande="py"

    screen.blit(fond, (0, 0))
    pygame.mixer.music.load("music/musique_acceuil.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.15)
    clock = pygame.time.Clock()

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
                        quit()
                    elif bregle.collidepoint(event.pos):
                        print("vous avez clicker sur Regles")
                        commande=commande+" vueRegle.py"
                        pygame.quit()
                        os.system(commande)
                    elif bcredit.collidepoint(event.pos):
                        print("vous avez clicker sur Credit")
                        commande=commande+" vueCredits.py"
                        os.system(commande)
                        commande=savecommande


        screen.blit(fond, (0, 0))
        if -120 < xk < -50 or 0<xk <50 or 100 < xk < 150 or 200<xk<250 or 300<xk<350 or 400<xk<450 :
            screen.blit(kangoo, (xk, yk))
        else :
            screen.blit(kangoo2, (xk, yk))

        xk = xk +1

        if xk >650 :
            xk = -150

        mouse = pygame.mouse.get_pos()
        smallText = pygame.font.Font("freesansbold.ttf",20)

        titreText = pygame.font.Font("leadcoat.ttf",50)

        nomJeu1 = titreText.render("The Infernal Kangaroo's",1,(40, 40, 40))
        nomJeu2 = titreText.render("Adventure",1,(40, 40, 40))
        screen.blit(nomJeu1, (90, 30))
        screen.blit(nomJeu2, (200, 80))

        if x+largB > mouse[0] > x and y+hautB > mouse[1] > y:
            bjouer=pygame.draw.rect(screen, (255, 153, 0),(x ,y,largB,hautB))
        else:
            bjouer=pygame.draw.rect(screen, (204, 122, 0),(x,y,largB,hautB))

        textBJouer = smallText.render("JOUER",1,(40, 40, 40))
        screen.blit(textBJouer, (x+15,y+15) )

        if x+largB > mouse[0] > x and y2+hautB > mouse[1] > y2:
            bregle=pygame.draw.rect(screen, (255, 153, 0),(x ,y2,largB,hautB))
        else:
            bregle=pygame.draw.rect(screen, (204, 122, 0),(x,y2,largB,hautB))

        textBRegle = smallText.render("RÉGLES",1,(40, 40, 40))
        screen.blit(textBRegle, (x+10,y2+15) )

        if x+largB > mouse[0] > x and y3+hautB > mouse[1] > y3:
            bcredit=pygame.draw.rect(screen, (255, 153, 0),(x ,y3,largB,hautB))
        else:
            bcredit=pygame.draw.rect(screen, (204, 122, 0),(x,y3,largB,hautB))

        textBCred = smallText.render("CRÉDITS",1,(40, 40, 40))
        screen.blit(textBCred, (x+7,y3+15) )

        pygame.display.flip()
        pygame.time.delay(5)

if __name__ == '__main__': main()
