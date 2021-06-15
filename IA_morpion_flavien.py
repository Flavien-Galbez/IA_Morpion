# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:43:09 2019

@author: Flavien
"""

dim_grille = 3

def Actions (grille):
    listeAction=[]
    for i in range (dim_grille):
        for j in range (dim_grille):
            if grille[i][j]==0:
                listeAction.append([i,j])
    return listeAction

def Result(grille,action,valeur):
    grille[action[0]][action[1]]=valeur
    return grille
    
def Terminal_Test (grille):
    #On test pour les deux participants
    for valeur_case in (1,2):
        #On test chaque ligne
        for i in range (dim_grille):
            test = True
            for j in range (dim_grille):
                if grille[i][j]!=valeur_case:
                    test = False
            if (test):
                return valeur_case
        #On test chaque colonne
        for j in range (dim_grille):
            test = True
            for i in range (dim_grille):
                if grille[i][j]!=valeur_case:
                    test = False
            if (test):
                return valeur_case
        #On test les 2 diagonnales
        test1 = True
        test2 = True
        for i in range (dim_grille):
            if grille[i][i]!=valeur_case:
                test1=False
            if grille[i][dim_grille-1-i]!=valeur_case:
                test2=False
        if (test1 or test2):
                return valeur_case
    return 0

def Utility (grille):
    if Terminal_Test(grille)==1:
        return 1
    if Terminal_Test(grille)==2:
        return -1
    return 0
    