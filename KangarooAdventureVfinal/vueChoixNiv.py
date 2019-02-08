import pygame
from pygame.locals import *
from sys import platform
import sys
import os


class Compte():
    def __init__(self, pieces ,points,medailles,skinpath,score,scoreg):
        self.pieces = pieces
        self.points = points
        self.medailles=medailles
        self.skin= skinpath
        self.score= score
        self.scoreglobal = scoreg

    def afficher(self):
        print(self.pieces)
        print(self.points)
        print(self.medailles)
        print(self.skin,end='')
        print(self.score)
        print(self.scoreglobal)


def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('The Infernal Kangaroo''s Adventure - ChoixNiveau')
    #Variable compte
    pieces=0
    pointsprog=0
    medaille=[]
    skinp=""
    scores=[]
    scoreG=0;
    compte = Compte(pieces ,pointsprog,medaille,skinp,scores,scoreG)



    #Recherche des attributs du compte
    nomj=None
    if len(sys.argv)>1:
        nomj=sys.argv[1]
        fichierC = open("compteJoueurs.txt", "r")
        ligne  = fichierC.readline()
        trouve=False
        while(not trouve):
            if ligne == (nomj+"!\n"):
                trouve=True
                #Récupération des piéces
                ligne=fichierC.readline()
                pieces=int(ligne.split(":")[1])
                #Récupération des points
                ligne=fichierC.readline()
                pointsprog=int(ligne.split(":")[1])

                #Récupération des medailles
                ligne=fichierC.readline()
                interm=ligne.split(":")[1]

                for h in range(0,15):
                    medaille.append(int(interm.split(",")[h]))

                #Récupération des skin
                ligne=fichierC.readline()
                skinp=ligne.split(":")[1]
                skinp=skinp[:-1]
                #Récupération du score
                ligne=fichierC.readline()
                s=ligne.split(":")
                scorelistS=s[1].split(",")
                i=0
                while(i<len(scorelistS)):
                    scores.append(int(scorelistS[i]))
                    i+=1
                #Récupération du score général
                ligne=fichierC.readline()
                scoreG=int(ligne.split(":")[1])




            else:
                ligne=fichierC.readline()

        fichierC.close()

    else:
        nomj="ladaronnealeo"



    compte = Compte(pieces ,pointsprog,medaille,skinp,scores,scoreG)


    #Panel de button

    fond = pygame.image.load('fonds/serpentin.png').convert()
    fond = pygame.transform.scale(fond, (800, 600))
    fond = fond.convert_alpha()

    x=150
    y=80
    largB=100
    hautB=70
    colorB = pygame.Color(255, 148, 77 )

    bniv1=pygame.draw.rect(fond, colorB,(x,y+20,largB,hautB))
    fondniv1 = pygame.image.load('fonds/fond_foret.png').convert()
    fondniv1 = pygame.transform.scale(fondniv1, (largB,hautB))


    bniv2=pygame.draw.rect(fond, colorB,(x+230,y-5,largB,hautB))
    fondniv2 = pygame.image.load('fonds/fond_glacier.png').convert()
    fondniv2 = pygame.transform.scale(fondniv2, (largB,hautB))

    bniv3=pygame.draw.rect(fond, colorB,(x+210,y+190,largB,hautB))
    fondniv3 = pygame.image.load('fonds/fond_grotte.png').convert()
    fondniv3 = pygame.transform.scale(fondniv3, (largB,hautB))

    bniv4=pygame.draw.rect(fond, colorB,(x,y+220,largB,hautB))
    fondniv4 = pygame.image.load('fonds/fond_nuage.png').convert()
    fondniv4 = pygame.transform.scale(fondniv4, (largB,hautB))


    bniv5=pygame.draw.rect(fond, colorB,(x+80,y+410,largB,hautB))
    fondniv5 = pygame.image.load('fonds/fond_volcan.png').convert()
    fondniv5 = pygame.transform.scale(fondniv5, (largB,hautB))

    skin = pygame.image.load(compte.skin)
    skin = pygame.transform.scale(skin, (100, 100))

    brankG=pygame.draw.rect(fond, colorB,(750,0,60,60))
    rankG= pygame.image.load('image/medaille.png')
    rankG = pygame.transform.scale(rankG, (60, 60))

    piece = pygame.image.load('image/piece.png')
    piece = pygame.transform.scale(piece, (20, 20))

    # innitialisation des images des médailles
    imgMedOr = pygame.image.load('image/pieceorgrisée.png')

    imgMedBronze = pygame.image.load('image/piecebronzegrisée.png')

    imgMedArgent = pygame.image.load('image/pieceargentgrisée.png')


    # Test sur l'os
    if platform == "linux" or platform == "linux2":
        commande="python3"
        savecommande="python3"
    elif platform == "win32":
        commande="py"
        savecommande="py"

    screen.blit(fond, (0, 0))
    pygame.display.update()
    pygame.mixer.music.load("music/musique_choix.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.15)

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if bniv1.collidepoint(event.pos):
                        print("vous avez clicker sur niv1")
                        commande=commande+" mainForet.py " +nomj
                        pygame.quit()
                        os.system(commande)
                        quit()

                    elif bniv2.collidepoint(event.pos):
                        print("vous avez clicker sur niv2")
                        print("vous avez clicker sur niv1")
                        commande=commande+" mainIce.py " +nomj
                        pygame.quit()
                        os.system(commande)
                        quit()

                    elif bniv3.collidepoint(event.pos):
                        print("vous avez clicker sur niv3")
                        print("vous avez clicker sur niv1")
                        commande=commande+" mainGrotte.py " +nomj
                        pygame.quit()
                        os.system(commande)
                        quit()

                    elif bniv4.collidepoint(event.pos):
                        print("vous avez clicker sur niv4")
                        print("vous avez clicker sur niv1")
                        commande=commande+" mainNuage.py " +nomj
                        pygame.quit()
                        os.system(commande)
                        quit()

                    elif bniv5.collidepoint(event.pos):
                        print("vous avez clicker sur niv1")
                        commande=commande+" mainVolcan.py " +nomj
                        pygame.quit()
                        os.system(commande)
                        quit()
                    elif brankG.collidepoint(event.pos):
                        commande=commande+" vueClassementGlobal.py " +nomj
                        os.system(commande)
                        commande=savecommande


        mouse = pygame.mouse.get_pos()
        smallText = pygame.font.Font("freesansbold.ttf",15)
        bigText = pygame.font.Font("freesansbold.ttf",20)
        textnomj = bigText.render("Nom:"+nomj,1,(210, 210, 210))



        #blit des fonds
        screen.blit(fond, (0, 0))
        screen.blit(fondniv1, (x,y+20))
        screen.blit(fondniv2, (x+230,y-5))
        screen.blit(fondniv3, (x+210,y+190))
        screen.blit(fondniv4, (x,y+220))
        screen.blit(fondniv5, (x+80,y+410))




        # blit des médailles nvx1
        f =0
        # si le joueur possède ce type de médaille pour se niveau alors prendre l'image non grisée
        if compte.medailles[f] == 1 :
            imgMedBronze = pygame.image.load('image/piecebronze.png')
        if compte.medailles[f+1] == 1 :
            imgMedArgent = pygame.image.load('image/pieceargent.png')
        if compte.medailles[f+2] == 1 :
            imgMedOr = pygame.image.load('image/pieceor.png')
        # ajouter 3 pour la vérification du prochain niveau
        f = f+3
        # redimmensionnment de l'image
        imgMedOr = pygame.transform.scale(imgMedOr, (60, 60))
        imgMedBronze = pygame.transform.scale(imgMedBronze, (60, 60))
        imgMedArgent = pygame.transform.scale(imgMedArgent, (60, 60))
        # ajout et positionnement de l'image dans la fenetre
        screen.blit(imgMedBronze, (x-5,y-40))
        screen.blit(imgMedArgent, (x+25,y-40))
        screen.blit(imgMedOr, (x+55,y-40))
        # réinitialisation de l'image en mode 'griser'
        imgMedOr = pygame.image.load('image/pieceorgrisée.png')
        imgMedBronze = pygame.image.load('image/piecebronzegrisée.png')
        imgMedArgent = pygame.image.load('image/pieceargentgrisée.png')

        # blit des médailles nvx2
        # si le joueur possède ce type de médaille pour se niveau alors prendre l'image non grisée
        if compte.medailles[f] == 1 :
            imgMedBronze = pygame.image.load('image/piecebronze.png')
        if compte.medailles[f+1] == 1 :
            imgMedArgent = pygame.image.load('image/pieceargent.png')
        if compte.medailles[f+2] == 1 :
            imgMedOr = pygame.image.load('image/pieceor.png')
        # ajouter 3 pour la vérification du prochain niveau
        f = f+3
        # redimmensionnment de l'image
        imgMedOr = pygame.transform.scale(imgMedOr, (60, 60))
        imgMedBronze = pygame.transform.scale(imgMedBronze, (60, 60))
        imgMedArgent = pygame.transform.scale(imgMedArgent, (60, 60))
        # ajout et positionnement de l'image dans la fenetre
        screen.blit(imgMedBronze, (x+220,y-60))
        screen.blit(imgMedArgent, (x+250,y-60))
        screen.blit(imgMedOr, (x+280,y-60))
        # réinitialisation de l'image en mode 'griser'
        imgMedOr = pygame.image.load('image/pieceorgrisée.png')
        imgMedBronze = pygame.image.load('image/piecebronzegrisée.png')
        imgMedArgent = pygame.image.load('image/pieceargentgrisée.png')

        # blit des médailles NVX3
        # si le joueur possède ce type de médaille pour se niveau alors prendre l'image non grisée
        if compte.medailles[f] == 1 :
            imgMedBronze = pygame.image.load('image/piecebronze.png')
        if compte.medailles[f+1] == 1 :
            imgMedArgent = pygame.image.load('image/pieceargent.png')
        if compte.medailles[f+2] == 1 :
            imgMedOr = pygame.image.load('image/pieceor.png')
        # ajouter 3 pour la vérification du prochain niveau
        f = f+3
        # redimmensionnment de l'image
        imgMedOr = pygame.transform.scale(imgMedOr, (60, 60))
        imgMedBronze = pygame.transform.scale(imgMedBronze, (60, 60))
        imgMedArgent = pygame.transform.scale(imgMedArgent, (60, 60))
        # ajout et positionnement de l'image dans la fenetre
        screen.blit(imgMedBronze, (x+200,y+140))
        screen.blit(imgMedArgent, (x+230,y+140))
        screen.blit(imgMedOr, (x+260,y+140))
        # réinitialisation de l'image en mode 'griser'
        imgMedOr = pygame.image.load('image/pieceorgrisée.png')
        imgMedBronze = pygame.image.load('image/piecebronzegrisée.png')
        imgMedArgent = pygame.image.load('image/pieceargentgrisée.png')


        # blit des médailles nvx4
        # si le joueur possède ce type de médaille pour se niveau alors prendre l'image non grisée
        if compte.medailles[f] == 1 :
            imgMedBronze = pygame.image.load('image/piecebronze.png')
        if compte.medailles[f+1] == 1 :
            imgMedArgent = pygame.image.load('image/pieceargent.png')
        if compte.medailles[f+2] == 1 :
            imgMedOr = pygame.image.load('image/pieceor.png')
        # ajouter 3 pour la vérification du prochain niveau
        f = f+3
        # redimmensionnment de l'image
        imgMedOr = pygame.transform.scale(imgMedOr, (60, 60))
        imgMedBronze = pygame.transform.scale(imgMedBronze, (60, 60))
        imgMedArgent = pygame.transform.scale(imgMedArgent, (60, 60))
        # ajout et positionnement de l'image dans la fenetre
        screen.blit(imgMedBronze, (x-10,y+170))
        screen.blit(imgMedArgent, (x+20,y+170))
        screen.blit(imgMedOr, (x+50,y+170))
        # réinitialisation de l'image en mode 'griser'
        imgMedOr = pygame.image.load('image/pieceorgrisée.png')
        imgMedBronze = pygame.image.load('image/piecebronzegrisée.png')
        imgMedArgent = pygame.image.load('image/pieceargentgrisée.png')

        # blit des médailles nvx5
        # si le joueur possède ce type de médaille pour se niveau alors prendre l'image non grisée
        if compte.medailles[f] == 1 :
            imgMedBronze = pygame.image.load('image/piecebronze.png')
        if compte.medailles[f+1] == 1 :
            imgMedArgent = pygame.image.load('image/pieceargent.png')
        if compte.medailles[f+2] == 1 :
            imgMedOr = pygame.image.load('image/pieceor.png')
        # redimmensionnment de l'image
        imgMedOr = pygame.transform.scale(imgMedOr, (60, 60))
        imgMedBronze = pygame.transform.scale(imgMedBronze, (60, 60))
        imgMedArgent = pygame.transform.scale(imgMedArgent, (60, 60))
        # ajout et positionnement de l'image dans la fenetre
        screen.blit(imgMedBronze, (x+70,y+350))
        screen.blit(imgMedArgent, (x+100,y+350))
        screen.blit(imgMedOr, (x+130,y+350))
        # réinitialisation de l'image en mode 'griser'
        imgMedOr = pygame.image.load('image/pieceorgrisée.png')
        imgMedBronze = pygame.image.load('image/piecebronzegrisée.png')
        imgMedArgent = pygame.image.load('image/pieceargentgrisée.png')

        nbpiece = smallText.render((" x " + str(compte.pieces)),1,(210, 210, 210))

        screen.blit(textnomj, (660,275))
        screen.blit(skin,(650,300))
        screen.blit(rankG,(750,0))
        screen.blit(piece, (670,30))
        screen.blit(nbpiece, (690,30))

        pygame.display.flip()

if __name__ == '__main__': main()
