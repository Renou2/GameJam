import pygame
from pygame.locals import *

def estInscrit(nomJ):
    f = open("joueurs.txt",'r')
    lignes  = f.readlines()
    f.close()
    estpresent=False;

    for ligne in lignes:
        if ligne == (nomJ+"\n"):
            estpresent=True;
    return estpresent




def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((630, 300))
    pygame.display.set_caption('Nom du jeu')


    fond = pygame.image.load('fond.png').convert()
    fond = pygame.transform.smoothscale(fond, (630, 300))
    fond = fond.convert_alpha()

    x=20
    y=240
    largB=150
    hautB=50

    binscrit=pygame.draw.rect(fond, (204, 122, 0),(x,y,largB,hautB))

    arial = pygame.font.SysFont("comicsansms.tff",30)
    arial.set_bold(False)
    textBins = arial.render("Déja Inscrit",1,(40, 40, 40))
    fond.blit(textBins, (x+15,y+15) )

    input_box = pygame.Rect(190, 240, 200, 50)
    active = False
    text = ''
    color_inactive = pygame.Color(204, 122, 0 )
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    screen.blit(fond, (0, 0))
    pygame.display.update()

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    print("vous avez clicker sur la boite")
                elif binscrit.collidepoint(event.pos):
                    print("buton ins")
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        if not estInscrit(text):
                            fichierJ = open("joueurs.txt", "a")
                            fichierJ.write(text+"\n")
                            fichierJ.close()
                            return
                        else:
                            print("est déja inscrit")

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = arial.render(text, True, (10,10,10))
        fond.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.draw.rect(fond, color, input_box, 2)
        screen.blit(fond, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
