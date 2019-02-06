import pygame
from pygame.locals import *
from sys import platform
import os

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


    fond = pygame.image.load('fonds/fond_regles.jpg').convert()
    fond = pygame.transform.smoothscale(fond, (630, 300))
    fond = fond.convert_alpha()

    x=400
    y=240
    largB=150
    hautB=50

    charSelect = 'sprite_kangoo0.png'

    bvalide=pygame.draw.rect(fond, (204, 122, 0),(x,y,largB,hautB))
    bChar2=pygame.draw.rect(fond, (200,150,100),(450,100,150,100))
    bChar1=pygame.draw.rect(fond, (200,150,100),(30,100,150,100))

    arial = pygame.font.SysFont("comicsansms.tff",35)
    arial.set_bold(False)

    police2 =pygame.font.SysFont("comicsansms.tff",40)


    input_box = pygame.Rect(190, 240, 200, 50)
    active = False
    text = ''
    color_inactive = pygame.Color(204, 122, 0 )
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    skin = pygame.image.load('image/sprite_kangoo0.png')
    skin = pygame.transform.scale(skin, (150, 100))

    skinf = pygame.image.load('image/bonhomme.png')
    skinf = pygame.transform.scale(skin, (150, 100))

    if platform == "linux" or platform == "linux2":
        commande="python3"
        savecommande="python3"
    elif platform == "win32":
        commande="py"
        savecommande="py"

    screen.blit(fond, (0, 0))
    pygame.display.update()
    pygame.mixer.music.load("ladaronnealeo.mp3")
    pygame.mixer.music.play()
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
                elif bvalide.collidepoint(event.pos):
                    print("buton val")
                    print(text)
                    if not estInscrit(text):
                        #Inscription du nom
                        fichierJ = open("joueurs.txt", "a")
                        fichierJ.write(text+"\n")
                        fichierJ.close()

                        #Instanciation du compte
                        fichierC = open("compteJoueurs.txt", "a")
                        fichierC.write(text+"!\n")
                        fichierC.write("Pieces:0\n")
                        fichierC.write("PointsProg:0\n")
                        fichierC.write("Medailles:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n")
                        fichierC.write("Skin:"+charSelect+"\n")
                        fichierC.write("Score:0,0,0,0,0\n")
                        fichierC.write("ScoreGeneral:0\n")
                        fichierC.close()


                        commande=commande+" vueChoixNiv.py " +text
                        pygame.quit()
                        os.system(commande)
                        quit()
                    else:
                        print("est déja inscrit")
                        commande=commande+" vuePopUp.py " +text
                        pygame.quit()
                        os.system(commande)
                        quit()
                elif bChar1.collidepoint(event.pos):
                    print("vous avez clicker sur Char1")
                    charSelect = 'sprite_kangoo0.png'
                elif bChar2.collidepoint(event.pos):
                    print("vous avez clicker sur Char2")
                    charSelect = 'bonhomme.png'
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:

                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_b = arial.render("Entrez votre nom", True, (10,10,10))
        fond.blit(txt_b, (input_box.x, input_box.y-30))
        txt_surface = arial.render(text, True, (10,10,10))
        fond.blit(txt_surface, (input_box.x+5, input_box.y+5))

        #Surlignage du bouton
        mouse = pygame.mouse.get_pos()

        if x+largB > mouse[0] > x and y+hautB > mouse[1] > y:
            bvalide=pygame.draw.rect(fond, (255, 153, 0),(x,y,largB,hautB))
        else:
            bvalide=pygame.draw.rect(fond, (204, 122, 0),(x,y,largB,hautB))

        textBins = arial.render("Valider",1,(40, 40, 40))
        fond.blit(textBins, (x+30,y+10) )



        #Blit de tout les élément

        txtP = police2.render("Sélectionnez un personnage", True, (10,10,10))
        fond.blit(txtP, (150,10) )

        pygame.draw.rect(fond, color, input_box, 2)
        screen.blit(fond, (0, 0))

        screen.blit(skin,(30,100))

        screen.blit(skinf,(450,100))

        pygame.display.flip()


if __name__ == '__main__': main()
