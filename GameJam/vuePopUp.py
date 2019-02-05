import pygame
from pygame.locals import *
from sys import platform
import sys
import os

pygame.init()

frame = pygame.display.set_mode((600, 300), RESIZABLE)

x=190
x2=400
y=200
largBut=80
hautBut=30

background = "background_popup.jpg"
fond = pygame.image.load(background).convert_alpha()
frame.blit(fond, (0,0))

image = "interrogation.png"
icone = pygame.image.load(image).convert_alpha()
icone = pygame.transform.scale(icone, (80,160))
frame.blit(icone, (30,70))
pygame.display.flip()

smallText = pygame.font.Font("freesansbold.ttf",20)

textVerif = smallText.render("Ce pseudo existe déjà, est ce bien vous ?", 1, (40,40,40))
frame.blit(textVerif,[600/4, 300/4])
btnOui = pygame.draw.rect(frame, (200,200,200),(x,y,largBut,hautBut))
btnNon = pygame.draw.rect(frame, (200,200,200),(x2,y,largBut,hautBut))
pygame.display.flip()

if platform == "linux" or platform == "linux2":
    commande="python3"
    savecommande="python3"
elif platform == "win32":
    commande="py"
    savecommande="py"

if len(sys.argv)>1:
    nomj=sys.argv[1]
else:
    nomj="ladaronnealeo"

continuer = 1
while continuer:
    for event in pygame.event.get():
	       if event.type == QUIT:
		             continuer = 0
	       elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if btnNon.collidepoint(event.pos):
                        print("Vous avez clicker sur oui")
                        commande=commande+" vueChoixNiv.py " +nomj
                        pygame.quit()
                        os.system(commande)
                        quit()
                    elif btnOui.collidepoint(event.pos):
                        print("Vous avez clicker sur non")
                        commande=commande+" vueChoixPerso.py"
                        pygame.quit()
                        os.system(commande)
                        quit()

    mouse = pygame.mouse.get_pos()

    if x+largBut > mouse[0] > x and y+hautBut > mouse[1] > y:
        btnOui=pygame.draw.rect(frame, (255, 153, 0),(x,y,largBut,hautBut))
    else:
        btnOui=pygame.draw.rect(frame, (204, 122, 0),(x,y,largBut,hautBut))

    if x2+largBut > mouse[0] > x2 and y+hautBut > mouse[1] > y:
        btnNon=pygame.draw.rect(frame, (255, 153, 0),(x2,y,largBut,hautBut))
    else:
        btnNon=pygame.draw.rect(frame, (204, 122, 0),(x2,y,largBut,hautBut))

    textBtnNon = smallText.render("Non",1,(40,40,40))
    textBtnOui = smallText.render("Oui", 1, (40,40,40))
    frame.blit(textBtnNon, (x+20,y+5))
    frame.blit(textBtnOui,(x2+20,y+5) )
    pygame.display.flip()
