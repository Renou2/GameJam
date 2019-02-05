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
    pygame.display.set_caption('Nom du jeu')
    #Variable compte
    pieces=0
    pointsprog=0
    medaille=[]
    skinp=""
    scores=[]
    scoreG=0;
    compte = Compte(pieces ,pointsprog,medaille,skinp,scores,scoreG)



    #Recherche des attributs du compte

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

                #Récupération des skin
                ligne=fichierC.readline()
                skinp=ligne.split(":")[1]
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
    compte.afficher()



    #Panel de button

    fond = pygame.image.load('serpentin.png').convert()
    fond = pygame.transform.scale(fond, (800, 600))
    fond = fond.convert_alpha()

    x=150
    y=80
    largB=100
    hautB=50
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

    skin = pygame.image.load('bonhomme.png')
    skin = pygame.transform.scale(skin, (100, 100))

    rankG= pygame.image.load('medaille.png')
    rankG = pygame.transform.scale(rankG, (60, 60))


    # Test sur l'os
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if bniv1.collidepoint(event.pos):
                        print("vous avez clicker sur niv1")

                    elif bniv2.collidepoint(event.pos):
                        print("vous avez clicker sur niv2")

                    elif bniv3.collidepoint(event.pos):
                        print("vous avez clicker sur niv3")

                    elif bniv4.collidepoint(event.pos):
                        print("vous avez clicker sur niv4")

                    elif bniv5.collidepoint(event.pos):
                        print("vous avez clicker sur niv5")




        mouse = pygame.mouse.get_pos()
        smallText = pygame.font.Font("freesansbold.ttf",25)

        textnomj = smallText.render(nomj,1,(210, 210, 210))
        fond.blit(textnomj, (670,270) )

        #blit des fonds
        screen.blit(fond, (0, 0))
        screen.blit(fondniv1, (x,y+20))
        screen.blit(fondniv2, (x+230,y-5))
        screen.blit(fondniv3, (x+210,y+190))
        screen.blit(fondniv4, (x,y+220))
        screen.blit(fondniv5, (x+80,y+410))



        screen.blit(skin,(700,300))
        screen.blit(rankG,(750,0))
        pygame.display.flip()

if __name__ == '__main__': main()
