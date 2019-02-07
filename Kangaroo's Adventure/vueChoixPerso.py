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
    screen = pygame.display.set_mode((630, 500))
    pygame.display.set_caption('The Infernal Kangaroo''s Adventure - ChoixPersonnage')


    fond = pygame.image.load('fonds/fond_regles.jpg').convert()
    # fond = pygame.transform.smoothscale(fond, (630, 300))
    fond = fond.convert_alpha()

    x=400
    y=370
    largB=150
    hautB=50

    charSelect = 'image/kangoo0.png'

    bvalide=pygame.draw.rect(fond, (204, 122, 0),(x,y,largB,hautB))
    bChar2=pygame.draw.rect(fond, (23, 70, 145),(450,170,150,100))
    bChar1=pygame.draw.rect(fond, (23, 70, 145),(30,170,150,100))

    arial = pygame.font.SysFont("comicsansms.tff",35)
    arial.set_bold(False)


    bigText = pygame.font.Font("leadcoat.ttf",30)


    input_box = pygame.Rect(190, 370, 200, 50)
    active = False
    text = ''
    color_inactive = pygame.Color(204, 122, 0 )
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    skin = pygame.image.load('image/kangoo0.png')
    skin = pygame.transform.scale(skin, (150, 130))

    skinf = pygame.image.load('image/bonhomme.png')
    skinf = pygame.transform.scale(skinf, (150, 100))

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
                    charSelect = 'image/kangoo0.png'
                elif bChar2.collidepoint(event.pos):
                    print("vous avez clicker sur Char2")
                    charSelect = 'image/bonhomme.png'
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

        txt_surface = arial.render(text, True, (10,10,10))


        #Surlignage du bouton
        mouse = pygame.mouse.get_pos()

        if x+largB > mouse[0] > x and y+hautB > mouse[1] > y:
            bvalide=pygame.draw.rect(fond, (255, 153, 0),(x,y,largB,hautB))
        else:
            bvalide=pygame.draw.rect(fond, (204, 122, 0),(x,y,largB,hautB))


        if 30+150 > mouse[0] > 30 and 170+100 > mouse[1] > 170:
            bChar1=pygame.draw.rect(fond, (44, 91, 165),(30,170,150,100))
        else:
            bChar1=pygame.draw.rect(fond, (23, 70, 145),(30,170,150,100))


        if 450+150 > mouse[0] > 450 and 170+100> mouse[1] > 170:
            bChar2=pygame.draw.rect(fond, (44, 91, 165),(450,170,150,100))
        else:
            bChar2=pygame.draw.rect(fond, (23, 70, 145),(450,170,150,100))

        textBins = arial.render("Valider",1,(40, 40, 40))
        fond.blit(textBins, (x+30,y+10) )



        #Blit de tout les élément
        pygame.draw.rect(fond, color, input_box, 2)
        screen.blit(fond, (0, 0))

        txtP = bigText.render("Selectionnez un personnage", 1, (204, 122, 0))
        screen.blit(txtP, (160,30) )

        screen.blit(txt_b, (input_box.x, input_box.y-30))
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        screen.blit(skin,(30,140))

        screen.blit(skinf,(450,170))

        pygame.display.flip()


if __name__ == '__main__': main()
