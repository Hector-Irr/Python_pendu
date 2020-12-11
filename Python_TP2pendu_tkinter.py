# -*- coding: utf-8 -*-
"""
@author: Hector Irrmann
Created on Fri Dec 11 08:26:25 2020
To Do: toute interface graphique
"""
#création de l'interface graphique
from tkinter import Tk, Entry, Button, Canvas, label

fenetre = Tk()
label =label(fenetre, text="Hello")
fenetre.title('Pendu python Tkinter')


# importation des fonctions nécessaires
from ma_lib import freponse
from ma_lib import fLettres
from ma_lib import fMot

#création des variables nécessaires au programme
chance=8
n=0
gagner=False

reponse=""
proposition=""
lettreTrouve=""

mot=freponse()
listeLettre=fLettres(mot)
Mot=fMot(listeLettre)

#affichage du mot à trouver avec des '_' pour les lettres inconnues        
for i in mot:
    if n==0:
        reponse=reponse+i
        n=n+1
    else :
        reponse=reponse+" _"
print(reponse)

#boucle qui permet de demander des lettres au joueur jusqu'à ce que le mot soit complet
#ou que le nombre de chance tombe à 0
while chance>0 :
    
    lettre=input("Quelle est la lettre que vous souhaitez essayer ? ")
    if lettre in proposition:
        print("Vous avez déjà essayé la lettre ",lettre," essayez-en une autre!")
    elif len(lettre)>1:
        print("Vous ne devez inscrire qu'une lettre à la fois!")
    else:
        proposition=proposition+lettre
        if lettre in Mot:
            lettreTrouve=lettreTrouve+lettre
        else:
            chance=chance-1
   
    reponse=listeLettre[0]
    for i in Mot:
        if i in lettreTrouve:
            reponse=reponse+i
            
        else:
            reponse=reponse+" _"
    print(reponse)
    if "_" not in reponse:
        gagner=True
        break
    print("Il vous reste ",chance," chance(s).") 
    
    
#affiche si le joueur a gagné ou perdu et la fin de la partie
if gagner==True:
    print("Vous avez gagné!")
else:
    print("Vous avez perdu! Le mot a trouver était:",mot)
print("La partie est terminée!")






fenetre.mainloop()






























