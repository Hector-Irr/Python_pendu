# -*- coding: utf-8 -*-
"""
C'est le programme principal pour la version avec affichage graphique
@author: Hector Irrmann
Created on Fri Dec 11 08:26:25 2020
To Do: fonctionnement programme avec interface graphique: 
prendre en compte ce qui est écrit dans entry, afficher image 
pendu, compter chances, changer affichage quand on a une bonne lettre
"""
#création de l'interface graphique
from tkinter import Tk, Entry, Button, Canvas, Label, StringVar

fenetre = Tk()
fenetre.title('Pendu python Tkinter')
Canvas(fenetre, width=1000, height=500, bg='gray').pack()

# importation des fonctions nécessaires
from ma_lib_tkinter import freponse, fLettres, fMot, fEssai, fAffiche

#création des variables nécessaires au programme
gagner=False


proposition=""
lettreTrouve=""
chance=8
mot=freponse()
listeLettre=fLettres(mot)
Mot=fMot(listeLettre)


essai=StringVar()
champ=Entry(fenetre, textvariable=essai, bg="white")
essaibouton=essai.get()
bouton=Button(fenetre, text="Proposer", command=fEssai(essaibouton,proposition,lettretrouve))

   
reponse=fAffiche(listeLettre)

labelreponse= Label(fenetre, text=reponse)
labelreponse.pack()

if "_" not in reponse:
    gagner=True
    
print("Il vous reste ",chance," chance(s).") 
    
    
#affiche si le joueur a gagné ou perdu et la fin de la partie
if gagner==True:
    print("Vous avez gagné!")
else:
    print("Vous avez perdu! Le mot a trouver était:",mot)
print("La partie est terminée!")



fenetre.mainloop()






























