import pygame
from pygame.locals import *



def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((630, 300))
    pygame.display.set_caption('Nom du jeu')


    #Panel de button


    fond = pygame.image.load('fonds/fond.png').convert()
    fond = pygame.transform.smoothscale(fond, (630, 300))
    fond = fond.convert_alpha()
    screen.blit(fond, (0, 0))
    pygame.display.update()

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


        arial = pygame.font.SysFont("comicsansms.tff",40)
        arial.set_bold(False)
        textCred = arial.render("CRÉDITS:",1,(10, 10, 10))


        arial = pygame.font.SysFont("comicsansms.tff",30)
        credits = arial.render("Le jeu <nomdujeu> a été dévellopé dans le cadre de la gamejam",1,(20, 20, 20))
        creditsEquipe = arial.render("2019 par l'équipe <noméquipe> composée de : ",1,(20, 20, 20))
        creditsRens = arial.render("Lienard Renaud:<role> ",1,(20, 20, 20))
        creditsD = arial.render("Dutto Driss:<role>  ",1,(20, 20, 20))
        creditsRose = arial.render("Chapelle Rose:<role> ",1,(20, 20, 20))
        creditsLo = arial.render("Kemplaire Léo:<role> ",1,(20, 20, 20))
        creditsColin = arial.render("Vinot Colin:<role>" ,1,(20, 20, 20))


        fond.blit(textCred, (270,25))
        fond.blit(credits, (0,80))
        fond.blit(creditsEquipe, (0,100))
        fond.blit(creditsRens, (40,120))
        fond.blit(creditsD, (40,140))
        fond.blit(creditsRose, (40,160))
        fond.blit(creditsLo, (40,180))
        fond.blit(creditsColin, (40,200))
        screen.blit(fond, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
