"""
Created on Tue Apr 16 13:43:09 2019

@author: Flavien
"""


import numpy as np

def actions(tab): # retourne une matrice indiquant quels coups sont possibles
    t = len(tab[0])
    result=[[False for i in range(t)] for j in range(t)]
    for i in range(t):
        for j in range(t):
            if(tab[i][j]==0) :
                result[i][j]=True
    return result

def terminalTestMorpion(tab): # Permet de tester si le jeu est terminer et donne une valeur selon le gagnant +1/-1 ou 0 si égalité ou non terminé
    t=len(tab[0])
    resultVal=0
    # Faire un test vrai/faux permets de tester la différence entre une égalité ou un état final mais surtout simplifie les usage futur de cette fonction
    result=False
    # Toutes les cases sont remplies ?
    pos=actions(tab)
    test=True
    for i in range(t):
        for j in range(t):
            if(pos[i][j]): test=False
    if(test): result=True
    # Victoire avec les lignes ?
    for i in range(t):
        test = True
        value = tab[i][0]
        for j in range(1,t):
            if tab[i][j]!=value or value==0 : test = False
        if test :
            result=True
            resultVal=value
    # Victoire avec les colonnes ?
    for j in range(t):
        test = True
        value = tab[0][j]
        for i in range(1,t):
            if tab[i][j]!=value or value==0 : test = False
        if test :
            result=True
            resultVal=value
    # Victoire avec les diagonnales ?
    testd1=True
    testd2=True
    valued1=tab[0][0]
    valued2=tab[0][t-1]
    for i in range(1,t):
        if(tab[i][i]!=valued1 or valued1==0): testd1=False
        if(tab[i][t-1-i]!=valued2 or valued2==0): testd2=False
    if(testd1):
        result = True
        resultVal=valued1
    elif(testd2):
        result = True
        resultVal=valued2   
    return [result,resultVal]


def minmax(tab,depth,alpha,beta): #Algorithme de MinMax
    t=len(tab[0])
    bestMove=None
    bestScore=-np.inf #Permet d'avoir un bestScore cohérent avec un premier bestScore > à cette valleur d'initialisation
    pos=actions(tab)
    for i in range(t):
        for j in range(t):
            if(pos[i][j]):
                tab[i][j]=1
                mScore=MIN(tab,depth-1,alpha,beta)
                # Ligne faccultative permettant d'observer le comportement de l'IA
                print('i: '+str(i+1)+' j: '+str(j+1)+' score: '+str(mScore))
                if(mScore>bestScore):
                    bestMove=[i,j]
                    bestScore=mScore
                tab[i][j]=0
    tab[bestMove[0]][bestMove[1]]=1

def MAX(tab,depth,alpha,beta): # Maximisation
    t=len(tab[0])
    r=terminalTestMorpion(tab)
    if (r[0]): return r[1]
    elif (depth==0) :return 0
    else :
        bestScore=-np.inf #Permet d'avoir un besrScore cohérent avec un premier bestScore > à cette valleur d'initialisation
        pos=actions(tab)
        for i in range(t):
            for j in range(t):
                if(pos[i][j]):
                    tab[i][j]=1
                    mScore=MIN(tab,depth-1,alpha,beta)
                    if(mScore>bestScore):
                        bestScore=mScore
                        alpha=max(alpha,mScore)
                    tab[i][j]=0
                    if alpha>=beta : break
        return bestScore

def MIN(tab,depth,alpha,beta): # Minimisation
    t=len(tab[0])
    r=terminalTestMorpion(tab)
    if (r[0]): return r[1]
    elif (depth==0) :return 0
    else :
        worstScore=np.inf #Permet d'avoir un worstScore cohérent avec un premier worstScore < à cette valleur d'initialisation
        pos=actions(tab)
        for i in range(t):
            for j in range(t):
                if(pos[i][j]):
                    tab[i][j]=-1
                    mScore=MAX(tab,depth-1,alpha,beta)
                    if(mScore<worstScore):
                        worstScore=mScore
                        beta=min(beta,mScore)
                    tab[i][j]=0
                    if alpha>=beta : break
        return worstScore
                    
def tourJoueur(tab): # Permet à l'utilisateur de jouer son coup en vérifiant si la case est libre
        t=len(tab[0])
        i=-1
        j=-1
        action_possible=actions(tab)
        while(True):
            while(i<0 or i>=t or j<0 or j>=t):
                i=int(input("Entrer numero de ligne a jouer (1 à 3) : "))-1
                j=int(input("Entrer numero de colonne a jouer (1 à 3) : "))-1
            if(action_possible[i][j]):
                tab[i][j]=-1
                break
            else :
                i=-1
                j=-1
        return tab
    
def AfficherGrille(tab): # Affichage de la grille du morpion
    for i in range(len(tab[0])):
        for j in range(len(tab[::][0])):
            if(tab[i][j])==1: print('X',end='')
            elif(tab[i][j])==-1 : print('O',end='')
            else : print(' ',end='')
            if (j!= len(tab[::][0])-1):print(' | ',end='')
        print()
    print()
    
def jeuMorpion(): # Programme du jeu
    t=3
    tab=[[0 for _ in range(t)] for _ in range(t)]
    premier=''
    while(not (premier=='1' or premier=='0')): premier=input("Voulez vous commencer ?\n 0-NON\n 1-OUI\n")
    AfficherGrille(tab)
    while(not terminalTestMorpion(tab)[0]) :
        #Tour joueur s'il commence en premier
        if premier=='1' :
            tab=tourJoueur(tab)
            AfficherGrille(tab)
        if terminalTestMorpion(tab)[0] : break
        #Tour IA
        minmax(tab,10,-np.inf,np.inf)
        AfficherGrille(tab)
        if terminalTestMorpion(tab)[0] : break
        #Tour joueur s'il commence en deuxième
        if premier=='0' :
            tab=tourJoueur(tab)
            AfficherGrille(tab)        
    if(terminalTestMorpion(tab)[1]==1) : print("Victoire de l'IA !")
    elif(terminalTestMorpion(tab)[1]==-1) : print("Victoire de l'humain !") 
    else : print("Egalité !")
    
jeuMorpion()

