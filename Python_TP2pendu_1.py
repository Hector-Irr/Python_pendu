# -*- coding: utf-8 -*-
"""

C'est le programme principal qui permet de réaliser un pendu en version console
@author: Hector Irrmann
Created on Fri Nov 27 08:06:49 2020
To Do: rajouter un systeme de points et permettre de rejouer sans relancer le programme
"""
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


























