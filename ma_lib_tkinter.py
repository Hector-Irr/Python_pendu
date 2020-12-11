# -*- coding: utf-8 -*-
"""
Ce programme sert a stocker les différentes fonctions utilisées dans le programme principal
@author: Hector Irrmann
Created on Fri Dec 11 08:26:42 2020
To Do: rajouter et faire fonctionner les fonctions pour tkinter
"""
from tkinter import Tk, Entry, Button, Canvas, Label, StringVar
from random import randint

def freponse():                                     #Renvoi le mot à trouver
    listeMots=["jour","mois","poste","annee","python","abeille","ordinateur"]
    a=randint(0,6)
    mot=listeMots[a]
    return mot



def fLettres(mot):      #Renvoi une liste avec toutes les lettres du mot séparées
    l1=[]
    for i in mot:
        l1.append(i)
    return l1


def fMot (listeLettre):     #Renvoi une chaine de caractère avec toutes les lettres du mot sauf la première
    var=""
    for i in listeLettre[1:]:
        var=var+i
    return var



def fEssai(lettre,proposition,lettretrouve): #renvoi les lettres trouvées
    if lettre not in proposition:
        proposition=proposition+lettre
        if lettre in Mot:
            lettretrouve=lettretrouve+lettre
            messagebox.showinfo('Bien joué!')
            essai.set('')
        else:
            messagebox.showinfo('Le mot mystère ne contient pas cette lettre')
            essai.set('')
    else:
        messagebox.showinfo('Vous avez déjà essayé cette lettre, veuillez en essayer une autre')
        essai.set('')
        
    
    return lettretrouve
            


def fAffiche(listeLettre):       #renvoi le mot mystère avec des '_' pour les lettres qu'on ne connait pas
    reponse=listeLettre[0]
    for i in Mot:
        if i in lettretrouve:
            reponse=reponse+i
        else:
            reponse=reponse+" _"
    return reponse


def fChance(chance):                   #pour l'instant pas grand chose
    if chance==8:
        return 

    


