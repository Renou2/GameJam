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
    screen = pygame.display.set_mode((800, 750))
    pygame.display.set_caption('The Infernal Kangaroo''s Adventure')

    # Test sur l'os
    if platform == "linux" or platform == "linux2":
        commande="python3"
        savecommande="python3"
    elif platform == "win32":
        commande="py"
        savecommande="py"


    pygame.init()

    if platform == "linux" or platform == "linux2":
        commande="python3"
        savecommande="python3"
    elif platform == "win32":
        commande="py"
        savecommande="py"

    if len(sys.argv)>1:
        nomj=sys.argv[1]
    else:
        nomj="ArriéreGrandeDaronneDeLeo"

    nomscore = []

    f = open("compteJoueurs.txt",'r')
    lignes  = f.readlines()
    f.close()
    for ligne in lignes:
        ok = ligne.find('!')
        ok2 = ligne.find('ScoreGeneral')
        if ok != -1:
            nomscore.append(ligne)
            print('OK NOM')
        if ok2 != -1:
            nomscore.append(ligne)
            print('OK SCORE')

    SampleList = []
    i = 0
    jcourantNom=None
    jcourant=None
    if len(sys.argv)>1:
        jcourantNom=sys.argv[1]

    while i < (len(nomscore)):
        if i % 2 == 0:
            j = Joueur()
            j.nom = nomscore[i][:-2]
        if i % 2 == 1:
            j.score = int(nomscore[i].split(":")[1])
            if(jcourantNom==j.nom):
                jcourant=Joueur()
                jcourant.nom=j.nom
                jcourant.score=j.score
            SampleList.append(j)
        i = i+1

    SampleList.sort(key = lambda v: -v.score)

    fond = pygame.image.load('fonds/background_popup.jpg').convert()
    fond = pygame.transform.smoothscale(fond, (800, 750))
    fond = fond.convert_alpha()

    arial = pygame.font.SysFont("comicsansms.tff",35)
    arial.set_bold(False)

    screen.blit(fond, (0, 0))
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        txt_a = arial.render("Score", True, (10,10,10))
        fond.blit(txt_a, (50,50))
        txt_b = arial.render("Pseudo", True, (10,10,10))
        fond.blit(txt_b, (200,50))

        x = 50
        y = 150
        for i in range(len(SampleList)):
            txt_a = arial.render(str(SampleList[i].score), True, (10,10,10))
            fond.blit(txt_a, (x,y))
            a = str(SampleList[i].nom)
            txt_b = arial.render(a, True, (10,10,10))
            fond.blit(txt_b, (x+150,y))
            x = 50
            y = y+50
            if i>=10:
                break

        txt_a = arial.render(str(jcourant.score), True, (10,10,10))
        fond.blit(txt_a, (x,y))
        txt_b = arial.render(jcourant.nom + " ---->Votre Score ", True, (10,10,10))
        fond.blit(txt_b, (x+150,y))

        screen.blit(fond, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
