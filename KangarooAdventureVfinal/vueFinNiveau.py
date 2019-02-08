import pygame
from pygame.locals import *
from sys import platform
import sys
import os

class Joueur():
         def __init__(self):
            self.score = 0
            self.nom = 0

def main():
     # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('The Infernal Kangaroo''s Adventure')

    # Test sur l'os
    if platform == "linux" or platform == "linux2":
        commande="python3"
        savecommande="python3"
    elif platform == "win32":
        commande="py"
        savecommande="py"


    pygame.init()
    nomj=None
    score=None
    niveau=None
    compteurpiece=None
    if len(sys.argv)>1:
        nomj=sys.argv[1]
        score=sys.argv[2]
        compteurpiece=sys.argv[3]
        niveau=sys.argv[4]
    else:
        nomj="ArriéreGrandeDaronneDeLeo"

    fichierC = open("compteJoueurs.txt", "r")
    fichierCopie = open("compteJoueursCopie.txt", "w")
    lignes  = fichierC.readlines()
    cptligne=0
    ScNivList=[]
    compteurpiece=int(compteurpiece)
    pieceobtenus=compteurpiece
    for ligne in lignes:
        if ligne == (nomj+"!\n"):
            cptligne=1
            fichierCopie.write(nomj+"!\n")

        elif cptligne==1:
            pieces=int(ligne.split(":")[1])
            compteurpiece+=pieces
            fichierCopie.write("Pieces:"+str(compteurpiece)+"\n")
            cptligne=2

        elif cptligne ==2: #pointsprog
            fichierCopie.write(ligne)
            cptligne=3

        elif cptligne ==3: #medaille
            fichierCopie.write(ligne)
            cptligne=4

        elif cptligne ==4: #skin
            fichierCopie.write(ligne)
            cptligne =5

        elif cptligne ==5: #score
            cptligne=6
            s=ligne.split(":")
            scorelistS=s[1].split(",")
            i=0
            scores=[]
            while(i<len(scorelistS)):
                scores.append(int(scorelistS[i]))
                i+=1
            ScNivList=scores

            scores[int(niveau)]=score
            lecrire="Score:"
            x=0
            while(x<len(scores)):
                lecrire+=str(scores[x])+","
                x+=1
            lecrire = lecrire[:-1]
            lecrire +="\n"
            fichierCopie.write(lecrire)

        elif cptligne ==6: #ScoreGeneral
            cptligne=0
            cp=0
            scoreG=0
            while(cp<len(ScNivList)):
                scoreG+=int(ScNivList[cp])
                cp+=1
            fichierCopie.write("ScoreGeneral:"+str(scoreG)+"\n")
        else:
            fichierCopie.write(ligne)

    fichierC.close()
    fichierCopie.close()
    os.remove("compteJoueurs.txt")
    os.rename("compteJoueursCopie.txt", "compteJoueurs.txt")



    fond = pygame.image.load('fonds/background_popup.jpg').convert()
    fond = pygame.transform.smoothscale(fond, (800, 750))
    fond = fond.convert_alpha()

    arial = pygame.font.SysFont("comicsansms.tff",35)
    arial.set_bold(False)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                commande=commande+" vueChoixNiv.py " +nomj
                pygame.quit()
                os.system(commande)
                quit()

        txt_a = arial.render("Score:"+score, True, (10,10,10))
        fond.blit(txt_a, (50,50))
        txt_b = arial.render("Pseudo:"+nomj, True, (10,10,10))
        fond.blit(txt_b, (50,100))
        txt_c = arial.render("Piéces Obtenus:"+str(pieceobtenus), True, (10,10,10))
        fond.blit(txt_c, (50,150))



        screen.blit(fond, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
