# -*- coding: utf-8 -*-
"""
Ce programme sert a stocker les différentes fonctions utilisées dans le programme principal
@author: Hector Irrmann
Created on Fri Dec 11 08:26:42 2020
To Do: rajouter des mots dans la liste et les ordonner
"""

from random import randint

def freponse():                                     #Renvoi le mot à trouver
    listeMots=["ordinateur","abeille","python"]
    a=randint(0,2)
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





def fEssai(lettre,proposition,lettretrouve):
    if lettre not in proposition:
        proposition=proposition+lettre
        if lettre in Mot:
            lettretrouve=lettretrouve+lettre
        else:
            chance=chance-1
            

        

def fAffiche(listeLettre):
    reponse=listeLettre[0]
    for i in Mot:
        if i in lettretrouve:
            reponse=reponse+i
        else:
            reponse=reponse+" _"

def fChance():

    


