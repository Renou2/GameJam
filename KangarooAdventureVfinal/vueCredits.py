import pygame
from pygame.locals import *



def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((630, 500), RESIZABLE)
    pygame.display.set_caption('The Infernal Kangaroo''s Adventure - Crédits')


    #Panel de button


    fond = pygame.image.load('fonds/fondnuit.jpg').convert_alpha()
    # fond = pygame.transform.smoothscale(fond, (630, 300))
    screen.blit(fond, (0, 0))
    # pygame.display.update()

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


        smallText = pygame.font.Font("freesansbold.ttf",15)
        bigText = pygame.font.Font("leadcoat.ttf",30)
        textCred = bigText.render("Credits:", 1, (204, 122, 0))


        arial = pygame.font.SysFont("comicsansms.tff",30)
        credits = smallText.render("Le jeu The Infernal Kangaroo's Adventure a été dévelloppé ", 1, (220,220,220))
        creditsEquipe = smallText.render("dans le cadre de la gamejam 2019 par l'équipe Kangoo", 1, (220,220,220))
        creditsEquipe2 = smallText.render("Junior composée de : ", 1, (220,220,220))
        creditsRens = smallText.render("Lienard Renaud:Dev ", 1, (220,220,220))
        creditsD = smallText.render("Dutto Driss:Dev ", 1, (220,220,220))
        creditsRose = smallText.render("Chapelle Rose:Dev/Graphiste ", 1, (220,220,220))
        creditsLo = smallText.render("Kemplaire Léo:Dev ", 1, (220,220,220))
        creditsColin = smallText.render("Vinot Colin:Level Designer", 1, (220,220,220))

        screen.blit(fond, (0, 0))
        screen.blit(textCred, (270,70))
        screen.blit(credits, (80,180))
        screen.blit(creditsEquipe, (80,200))
        screen.blit(creditsEquipe2, (80,220))
        screen.blit(creditsRens, (120,240))
        screen.blit(creditsD, (120,260))
        screen.blit(creditsRose, (120,280))
        screen.blit(creditsLo, (120,300))
        screen.blit(creditsColin, (120,320))
        pygame.display.flip()

if __name__ == '__main__': main()
