import pygame
import os
from pygame.locals import *
from constantes import *
from sys import platform


pygame.init()

frame = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), RESIZABLE)

x=(largeur_fenetre/2.4)
y=(hauteur_fenetre/1.5)
largBut=80
hautBut=30
fond = pygame.image.load(image).convert_alpha()
frame.blit(fond, (0,0))
pygame.display.flip()

if platform == "linux" or platform == "linux2":
    commande="python3"
elif platform == "win32":
    commande="py"

smallText = pygame.font.Font("freesansbold.ttf",15)
bigText = pygame.font.Font("leadcoat.ttf",30)

titreRegles = bigText.render("Regles du jeu", 1, (204, 122, 0))

frame.blit(titreRegles, [largeur_fenetre/2.7, hauteur_fenetre/7])

entrerRegles0 = smallText.render("Dans ce jeu, votre but sera de récupérer les cinqs", 1, (10,10,10))
entrerRegles1 = smallText.render("trésors cachés dans les différents mondes. Vous ", 1, (10,10,10))
entrerRegles2 = smallText.render("aurez  trois minutes pour collecter un maximum de", 1, (10,10,10))
entrerRegles3 = smallText.render("points et ainsi passez au niveau suivant.", 1, (10,10,10))


frame.blit(entrerRegles0,[largeur_fenetre/5, hauteur_fenetre/4])
frame.blit(entrerRegles1,[largeur_fenetre/5, hauteur_fenetre/3])
frame.blit(entrerRegles2,[largeur_fenetre/5, hauteur_fenetre/2.5])
frame.blit(entrerRegles3,[largeur_fenetre/5, hauteur_fenetre/2.1])
pygame.display.flip()

buttRetourAcceuil=pygame.draw.rect(frame, (200,200,200),(x,y,largBut,hautBut))

pygame.display.flip()
pygame.display.update()

continuer = 1
while continuer:
    for event in pygame.event.get():
	       if event.type == QUIT:
		       continuer = 0
	       elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if buttRetourAcceuil.collidepoint(event.pos):
                        print("Vous avez clicker sur retour")
                        commande = commande+" vueIni.py"
                        pygame.quit()
                        os.system(commande)
                        quit()


    mouse = pygame.mouse.get_pos()

    if x+largBut > mouse[0] > x and y+hautBut > mouse[1] > y:
        buttRetourAcceuil=pygame.draw.rect(frame, (255, 153, 0),(x,y,largBut,hautBut))
    else:
        buttRetourAcceuil=pygame.draw.rect(frame, (204, 122, 0),(x,y,largBut,hautBut))

    textBretour = smallText.render("RETOUR",1,(40,40,40))
    frame.blit(textBretour, (x+7,y+5))
    pygame.display.flip()
