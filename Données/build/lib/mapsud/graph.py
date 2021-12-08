#%%
from numpy import string_
import pandas as pd
import openrouteservice
from openrouteservice import convert
import folium
import matplotlib.pyplot as plt
from ipywidgets import interact

##############################################################
#%%


# Nous avons convertit le pdf des tarifs en word.
# Puis effectué un copier-coller du tableau tarif depuis word dans VS-Code.

L1 = [ 0 ]
L2 = [ 0 , 0 ]
L3 = [ 0 , 0 , 0 ]
L4 = [ 0 , 0 , 0 , 0 ]
L5 = [ -1 , -1 , -1 , -1 , -1 ]
L6 = [ 1.6 , 1.6 , 1.6 , 1.6 , 1.6 , 1.6 ]
L7 = [ 3.6 , 3.6 , 3.6 , 3.6 , 3.6 , 3.6 , 1.9 ]
L8 = [ 4.7 , 4.7 , 4.7 , 4.7 , 4.7 , 4.7 , 3.3 , 1 ]
L9 = [ 5.6 , 5.6 , 5.6 , 5.6 , 5.6 , 5.6 , 3.6 , 1.4 , 0.7 ]
L10 = [ 8.4 , 8.4 , 8.4 , 8.4 , 8.4 , 8.4 , 5.6 , 3.3 , 2.7 , 2 ]
L11 = [ 8.5 , 8.5 , 8.5 , 8.5 , 8.5 , 8.5 , 5.7 , 3.4 , 2.8 , 2.1 , 0.4 ]
L12 = [ 10.6 , 10.6 , 10.6 , 10.6 , 10.6 , 10.6 , 8.5 , 5.7 , 4.1 , 3.6 , 1.9 , 1.5 ]
L13 = [ 11.5 , 11.5 , 11.5 , 11.5 , 11.5 , 11.5 , 9.1 , 6.7 , 5.9 , 4.1 , 2.6 , 2.2 , 0.7 ]
L14 = [ 14.9 , 14.9 , 14.9 , 14.9 , 14.9 , 14.9 , 11.9 , 9.5 , 9.2 , 7.7 , 5 , 4.2 , 3.1 , 1.9 ]
L15 = [ 15.2 , 15.2 , 15.2 , 15.2 , 15.2 , 15.2 , 12.3 , 9.7 , 9.3 , 8.4 , 6.1 , 5.4 , 3.7 , 2.9 , 1 ]
L16 = [ 17.1 , 17.1 , 17.1 , 17.1 , 17.1 , 17.1 , 15 , 12.1 , 11.8 , 10.3 , 8.8 , 7.5 , 5.9 , 4.7 , 2.5 , 1.5 ]
L17 = [ 18.8 , 18.8 , 18.8 , 18.8 , 18.8 , 18.8 , 16.2 , 13.8 , 13.5 , 11.8 , 9.6 , 9.2 , 7.1 , 5.9 , 3.1 , 2.6 , -1 ]
L18 = [ -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 ]
L19 = [ 18.8 , 18.8 , 18.8 , 18.8 , 18.8 , 18.8 , 16.2 , 13.8 , 13.5 , 11.8 , 9.6 , 9.2 , 7.1 , 5.9 , 3.1 , 2.6 , 0.8 , -1 , 0.8 ]   # Modification Boulout fermé <--> Espagne : 0.8

L20 = [ 10.8 , 10.8 , 10.8 , 10.8 , 10.8 , 10.8 , 8.6 , 6 , 4.1 , 3.4 , 2.4 , 1.8 , 2.9 , 3.4 , 6.9 , 7.6 , 9 , 10.3 , -1 , 10.3 ]
L21 = [ 14.7 , 14.7 , 14.7 , 14.7 , 14.7 , 14.7 , 12 , 9.5 , 8.1 , 7.4 , 5.4 , 4.4 , 6.2 , 7.2 , 10.3 , 10.9 , 12.9 , 14.2 , -1 , 14.2 , 2.4 ]
L22 = [ 15.1 , 15.1 , 15.1 , 15.1 , 15.1 , 15.1 , 12.6 , 10.4 , 9.1 , 8.1 , 6.2 , 5.2 , 7.5 , 8.1 , 10.6 , 11.4 , 13.8 , 14.3 , -1 , 14.3 , 3.4 , 0.7 ]
L23 = [ 17.2 , 17.2 , 17.2 , 17.2 , 17.2 , 17.2 , 15.3 , 12.8 , 10.8 , 10 , 8.8 , 7.8 , 9.4 , 10 , 12.4 , 13.8 , 15.7 , 16.8 , -1 , 16.8 , 5.1 , 2.5 , 1.7 ]
L24 = [ 18.3 , 18.3 , 18.3 , 18.3 , 18.3 , 18.3 , 15.8 , 13.7 , 12.1 , 11.1 , 10.2 , 9.1 , 10.2 , 11.5 , 13.9 , 14 , 16.5 , 17.9 , -1 , 17.9 , 6.4 , 3.8 , 2.8 , 1.3 ]
L25 = [ 20.3 , 20.3 , 20.3 , 20.3 , 20.3 , 20.3 , 18.5 , 15.9 , 14.1 , 13.4 , 12 , 10.7 , 12.4 , 13 , 15.7 , 16.6 , 18.5 , 20.2 , -1 , 20.2 , 8.4 , 5.5 , 4.6 , 3.2 , 2 ]
L26 = [ 20.5 , 20.5 , 20.5 , 20.5 , 20.5 , 20.5 , 19.3 , 16.3 , 15 , 13.8 , 12.5 , 11.6 , 13.2 , 14.1 , 16.6 , 17.1 , 20 , 20.7 , -1 , 20.7 , 9.4 , 7.2 , 6 , 4.4 , 3.3 , 0.9 ]
L27 = [ 22 , 22 , 22 , 22 , 22 , 22 , 20 , 18.4 , 16.9 , 15.8 , 14.5 , 13.8 , 14.8 , 15.6 , 18.1 , 18.5 , 20.6 , 21.6 , -1 , 21.6 , 11.3 , 8.6 , 8 , 6.1 , 4.9 , 2.8 , 1.7 ]
L28 = [ 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 20.7 , 18.6 , 17.6 , 16.6 , 14.9 , 14.6 , 15.5 , 16.4 , 18.7 , 19.2 , 21 , 22 , -1 , 22 , 12.5 , 10 , 8.6 , 7.5 , 6 , 4.2 , 3.4 , 1.1 ]
L29 = [ 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 20.7 , 18.6 , 17.6 , 16.6 , 14.9 , 14.6 , 15.5 , 16.4 , 18.7 , 19.2 , 21 , 22 , -1 , 22 , 12.5 , 10 , 8.6 , 7.5 , 6 , 4.2 , 3.4 , 1.1 , -1 ]
L30 = [ 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 20.7 , 18.6 , 17.6 , 16.6 , 14.9 , 14.6 , 15.5 , 16.4 , 18.7 , 19.2 , 21 , 22 , -1 , 22 , 12.5 , 10 , 8.6 , 7.5 , 6 , 4.2 , 3.4 , 1.1 , -1 , -1 ]
L31 = [ 21.2 , 21.2 , 21.2 , 21.2 , 21.2 , 21.2 , 19.2 , 16.8 , 14.5 , 14.1 , 13.1 , 11.8 , 13.6 , 14.3 , 16.5 , 17.5 , 20 , 21.2 , -1 , 21.2 , 9.1 , 6.6 , 5.8 , 4.3 , 3.2 , 1 , 1 , 3 , 4.5 , 4.5 , 4.5 ]
L32 = [ 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 21.2 , 18.8 , 17.1 , 16.3 , 14.9 , 13.9 , 15 , 16 , 18.8 , 18.9 , 21.6 , 22.7 , -1 , 22.7 , 11.3 , 9.1 , 8 , 5.4 , 4.2 , 2 , 2.4 , 4.4 , 5.5 , 5.5 , 5.5 , 1.3 ]
L33 = [ 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 23.7 , 21.2 , 18.8 , 17.1 , 16.3 , 14.9 , 13.9 , 15 , 16 , 18.8 , 18.9 , 21.6 , 22.7 , -1 , 22.7 , 11.3 , 9.1 , 8 , 5.4 , 4.2 , 2 , 2.4 , 4.4 , 5.5 , 5.5 , 5.5 , 1.3 , -1 ]
L34 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , -1 ]
L35 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 ]
L36 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 ]
L37 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 , 0 ]
L38 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 , 0 , 0 ]
L39 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 , 0 , 0 , 0 ]
L40 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 , 0 , 0 , 0 , 0 ]
L41 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 , 0 , 0 , 0 , 0 , 0 ]
L42 = [ 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 24.3 , 21.8 , 19.4 , 17.7 , 16.9 , 15.5 , 14.5 , 15.6 , 16.6 , 19.4 , 19.5 , 22.2 , 23.3 , -1 , 23.3 , 11.9 , 9.7 , 8.6 , 6 , 4.8 , 2.4 , 2.8 , 5 , 6.1 , 6.1 , 6.1 , 1.7 , -1 , 0 , -1 , 0 , 0 , 0 , 0 , 0 , 0 , -1 ]

TARIF = [ L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18, L19, L20, L21, L22, L23, L24, L25, L26, L27, L28, L29, L30, L31, L32, L33, L34, L35, L36, L37, L38, L39, L40, L41, L42 ]


#%%
#fonction calcul tarifs
def tarif (i,j) :   # i,j = numéros "arrangés" des sorties d'autouroutes

    if ( 0 <= i <= 42) and ( 0 <= j <= 42 ) :

        if i == j :
            print("Erreur : sortie = entrée")
        else :
            n = max(i,j)
            m = min(i,j)
            a = TARIF[n-1][m]
            
            return( a )   # Si a = -1, alors il n'existe pas de trajet

    else :
        print("Erreur : numéro incorrecte")

    

#%%
####################### IMPORT TABLEAU COORDONNEES ##############################
# Initialisation table de base
df = pd.read_csv("https://raw.githubusercontent.com/lucea97217/mapsud/main/Donn%C3%A9es/coordonnees.csv", sep=",")
# Supression des index
del df["index"]

# Fonction qui définit le tableau optimal
# En se basant sur les numéros arrangés 
# Afin que le programme fonctionne tout le temps
def tabOpti(df):
    # Ici on a repris Y de algo_tarifs
    # Correspondant à la liste des numéros arrangés
    # Des péages dont nous pouvons entrer et sortir

    Y = [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 33, 35, 36, 37, 38, 39, 40, 41, 42 ]
    df_nom=[]

    # On insère alors dans df_nom tout les noms de gare
    # Correspondants aux numéros arrangés de Y
    for i in range(len(Y)):
        df_nom.append(df["NOMGARE"][Y[i]])
    return df_nom


# %%

#################################################################################################

# Les An correspondent aux tronçons d'autoroutes avant intersection avec une autre.
# Nous nous en servons pour ordonner les sorties.
# An = [ Liste0, Liste1, Liste2 ]
# Liste 0 = liste des sorties
# Liste 1 = tronçons d'autouroutes connecté à An par la gauche  (premier élèment de Liste0)
# Liste 2 = tronçons d'autouroutes connecté à An par la droite  (dernier élément de Liste0) 

Y = [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 33, 35, 36, 37, 38, 39, 40, 41, 42 ]   # Ensemble des sorties valides

A0 = [ [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11 ] , [] , [1, 2] ]    # A9 Nord

A1 = [ [ 12, 13, 14, 15, 16, 19 ] , [0, 2] , [] ]   # A9 Sud

A2 = [ [ 20, 21, 22, 23, 24, 25 ] , [0, 1] , [3, 4] ]   # A61 Est

A3 = [ [ 26, 27, 29, 30 ] , [2, 4] , [] ]   # A66

A4 = [ [ 31, 33, 35, 36, 37, 38, 39, 40, 41, 42 ] , [2, 3] , [] ]   # A61 Ouest

A_ = [A0, A1, A2, A3, A4]

# On créer une fonction qui retourne la liste des sorties intermédiaires
# situées entre deux points i et j

def sortie_intermédiaire (i, j) :     # i et j numéros arrangés des sorties départ et arrivée

    S = []              # le futur return des sorties intermédiaires

    e = 0    # tampon             # on récupére les portions d'autoroutes dans
    for z in range( len(A_) ) :   # lesquelles sont stocké i et j  ( = A0, A1, ..., A4)

        if i in A_[z][0] :
            a = z              # i est stocké dans Aa[0] = A_[a][0]
            e += 1
        
        if j in A_[z][0] :
            b = z              # j est stocké dans Ab[0] = A_[b][0]
            e += 1

    if e != 2 :              # i et j sont introuvable dans les données
        return("Erreur")



    else :       # On va récupérer les sorties intermédiaires et les ranger dans S

        if a == b :
            m = min(i,j)
            n = max(i,j)

            for k in range ( len(A_[a][0]) ) :
                if  m <  A_[a][0][k] < n :
                    S.append( A_[a][0][k] )


        else :   # a != b

            e = 0   # tampon
        # Les quatre premiers if correspondent au cas où Aa et Ab sont connectés

        # On récupére les sorties de Aa
            if b in A_[a][1] :    # Si Aa gauche est connecté à Ab
                e = 1

                for k in range ( len(A_[a][0]) ) :
                    if A_[a][0][k] < i :
                        S.append( A_[a][0][k] )

            if b in A_[a][2] :    # Si Aa droite est connecté à Ab
                e = 1

                for k in range ( len(A_[a][0]) ) :
                    if A_[a][0][k] > i :
                        S.append( A_[a][0][k] )

        # On récupére les sorties de Ab
            if a in A_[b][1] :   # Si Ab gauche est connecté à Aa

                for k in range ( len(A_[b][0]) ) :
                    if A_[b][0][k] < j :
                        S.append( A_[b][0][k] )

            if a in A_[b][2] :   # Si Ab droite est conecté à Aa

                for k in range ( len(A_[b][0]) ) :
                    if A_[b][0][k] > j :
                        S.append( A_[b][0][k] )


            if e == 0 :  # A2 se trouve entre Aa et Ab  (voir graphique sur papier)

            # On récupère les sorties de A2
                for k in range ( len(A_[2][0]) ) :
                    S.append( A_[2][0][k] )

            # On récupére les sorties de Aa
                if a == 0 :   # Aa droite est connecté à A2

                    for k in range ( len(A_[a][0]) ) :
                        if A_[a][0][k] > i :
                            S.append( A_[a][0][k] )

                else :   # Aa gauche est connecté à A2

                    for k in range ( len(A_[a][0]) ) :
                        if A_[a][0][k] < i :
                            S.append( A_[a][0][k] )

            # On récupére les sorties de Ab
                if b == 0 :   # Ab droite est connecté à A2

                    for k in range ( len(A_[b][0]) ) :
                        if A_[b][0][k] > j :
                            S.append( A_[b][0][k] )

                else :   # Ab gauche est connecté à A2

                    for k in range ( len(A_[b][0]) ) :
                        if A_[b][0][k] < j :
                            S.append( A_[b][0][k] )

        return(S)


#%%

# Fonction algorithme une sortie, voir papier

def comparaison (A, B, Liste, Li) :

    alpha = tarif(A, B)
    W = [A, B]
    for (k, c1) in Liste :
        for (l, c2, Z) in Li :
            # Si il existe un trajet possible entre A et k, puis entre k et B
            if k == l :
                if ( c1 != -1 ) and ( c2 != -1 ) :  

                    if c1 + c2 < alpha :
                        alpha = c1 + c2
                        W = Z.copy()
                        W.insert(0, A)

                    if ( c1 + c2 == alpha ) and ( len(Z) < len(W)-1 ) :
                        W = Z.copy()
                        W.insert(0, A)


    return( alpha, W )


#%%

################################# ALGO TARIF OPTIMAL ##############################


  # Fonction retournant la liste des tarifs, et des trajets optimaux associées, pour q sorties max autorisées.
  # q allant de 0 au maximum envisageable
def trajet_optimal (A, B) :   # A, B les entrée et sortie = numéros "arrangées"
    # Y = ensemble des sorties possibles
    if (A == B) or (A not in Y) or (B not in Y) :  
        return(False)
    # Ensemble des solutions avec contrainte (tarif + trajet optimaux)
    S = []   
    # n-ième élément : contrainte n sorties max
    L = []
    # préambule : 0 sortie autorisé
    a = tarif(A, B)
    if a == -1 :       # Aucun trajet existant
        return(-1)     # Cas (29-30) et (41-42)
    W = [A, B]
    S.append( ( round(a,1), W, 0 ) )
    # première étape : 1 sortie autorisée
    I = sortie_intermédiaire (A, B)
    if len(I) >= 1 :
        Liste1 = []
        L0 = []
        for k in I :
            Liste1.append( ( k, tarif(A,k) ) )
            # Tarif + trajet optimal entre k et B, avec 0 arrêt possible
            L0.append ( ( k, tarif(k,B), [k,B] ) )     
        L.append(L0)
        # Tarif + trajet optimal entre A et B avec 1 arrêt possible
        (a, W) = comparaison (A, B, Liste1, L0)   
        S.append( (round(a,1), W, 1) )
    # deuxième étape : >= 2 sorties autorisées
    # 1) Préambule à la boucle while
    if len(I) >= 2 :
        Liste2 = []
        for k in I :
            I_ = sortie_intermédiaire (k, B)
            L_ = []
            for i in I_ :
                L_.append( ( i, tarif(k,i) ) )
            Liste2.append( (k, L_) )
    # 2) Calcul des tarifs et trajets optimaux
    t = 1
    while t < len(I) :
        t += 1
        n = len(L) - 1
        M = L[n]
        Lbis = []
        # 1ère connection, voir papier
        for k in I :
            for (l, N) in Liste2 :
                if k == l :
                      
                    # Tarif + trajet optimal entre k et B, avec t-1 arêts possibles, où 1 <= t-1 : étape de la boucle
                    (a, W) = comparaison( k, B, N, M )   
                    Lbis.append( ( k, a, W ) )
        L.append(Lbis)
        # 2ème connection, voir papier
          
        # Tarif + trajet optimal entre A et B avec t arrêts possibles
        (a, W) = comparaison( A, B, Liste1, Lbis )   
        S.append( (round(a,1), W, t) )
    return(S)


# Petite fonction supprimant les "doublons" de la fonction ci-dessus
# Retourne S = [ ... ( tarif(réel), trajet(liste), contrainte sortie(entier) ) ... ],
def trajet_optimal_min (A, B) :   # A, B les entrée et sortie = numéros "arrangées", à valeurs dans Y = ensemble des sorties valides
                                # Y = [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 33, 35, 36, 37, 38, 39, 40, 41, 42 ]
    S = trajet_optimal (A, B)
    if S == False :
        return(False)
    if S == -1 :
        return(-1)
    n = len(S) - 1
    while True :
        if n == 0 :                  # La meilleur solution est le direct entre A et B
             return( S )
        (a, W, t) = S[n]
        if (a, W, t-1) == S[n-1] :   # On supprime le dernier élément, car c'est un doublon
            del S[n]
        else :                       # S est devenue "irréductible"
            return( S )
        n = n-1

# Fonction qui calcule le nombre de sortie optimal
# On pose S = trajet_optimal_min(i,j)

def k_opti(S):
#si la fonction retourne -1 c'est qu'il n'y a pas 
#d'itinéraire possible
    if S ==-1:
        return S

    return len(S)-1


#%%
################################# CALCUL DE COORDONNEES ##########################################

class loca:
    #recherche des coordonnées en fonction du nom de la gare
    def nomCoord(char):
        y= -1
        for i in range(len(df)):
            if df["NOMGARE"][i]==char:
                y=i
        if y==-1:
            return "ERREUR : Ce nom n'a pas été trouvé"
        else:
            return y

    #recherche du nom de la gare en fonction du numéro arrangé
    def indCoord(i):
        #on vérifie que i est bien de type entier
        if isinstance(i,int)== True and 0<=i<=42:

            return df["NOMGARE"][i]

        else: 
            return "veuillez inserer un entier entre 0 et 42"

    #recherche des coordonnées dans l'ordre lattitude longitude
    # d'un péage en fonction du numéro arrangé
    def latLong(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['Y'][i],df['X'][i]
        else:
            return 'élément inconnu'

    #recherche des coordonnées dans l'ordre longitude lattitude
    # d'un péage en fonction du numéro arrangé
    def longLat(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['X'][i],df['Y'][i]
        else:
            return 'élément inconnu'

    #recherche de la lattitude d'un péage
    #en fonction de son numéro arrangé
    def Lat(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['Y'][i]
        else:
            return 'élément inconnu'

    #recherche de la lattitude d'un péage
    #en fonction de son numéro arrangé
    def long(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['X'][i]
        else:
            return 'élément inconnu'



#calcul du nombre optimum de sorties
#Pour payer le tarif le moins élevé d'un péage à un autre.



def histo(DEPART,ARRIVEE):

    # Si les noms correspondent au mêmes gares
    # Alors on affiche un plan vide
    if DEPART == ARRIVEE:
        name_axe_x = "Nombre de sortie maximale autorisée"
        name_axe_y = "prix (€)"
        d = {name_axe_x: [], name_axe_y: []}
        plt.bar(d[name_axe_x],d[name_axe_y])
        print(" Pas d'itinéraire possible.")
        return plt.show()


    R = trajet_optimal_min(loca.nomCoord(DEPART),loca.nomCoord(ARRIVEE))
    name_axe_x = "Nombre de sorties"
    name_axe_y = "prix (€)"
    d = {name_axe_x: [], name_axe_y: []}
    for n in range(len(R)):
        d[name_axe_x].append(R[n][2])
        d[name_axe_y].append(R[n][0])

    # Si le trajet est gratuit on affiche alors un point de coordonnées (0,0)
    if d[name_axe_y]==[0] and d[name_axe_x]==[0]:

        plt.scatter(d[name_axe_x],d[name_axe_y])
        plt.xlabel(name_axe_x, size = 16)
        plt.ylabel(name_axe_y, size = 16)
        return plt.show()

    # Sinon on affiche la distribution des prix en fonction du nombre des sorties
    # Jusqu'à arriver au nombre de sorties optimal
    plt.bar(d[name_axe_x],d[name_axe_y])
    plt.xlabel(name_axe_x, size = 16)
    plt.ylabel(name_axe_y, size = 16)
    return plt.show()

     


#################################################################################
#%%
######################## GRAPHE INTERACTIF #####################################

# Creation classe graphique
# Elle permet d'afficher un graphe interactif 
class graphique:
    # Pas d'initialisation
    def __init__(self) -> None:
        pass

    def graph_rang(DEPART,ARRIVEE,nbSorties,APIkey):
    # Ici on devra insérer 2 chaines de caractères
    # Correspondant à des noms de gares connus
    # Avec une contrainte de nombre de sorties (nbSorties)


        if isinstance(DEPART,str)==True and isinstance(ARRIVEE,str)==True:
        #Verification des variables
            if DEPART == ARRIVEE:
            # Evidemment dans ce cas il n'y a pas de trajet
                return 'Trajet impossible'
            else:
                # On utilise nomCoord présentée ultérieurement
                i = loca.nomCoord(DEPART)
                j = loca.nomCoord(ARRIVEE)

                S = trajet_optimal_min(i,j)
                # On traite le cas où il n'y a pas d'itinéraire possible
                if k_opti(S)==-1:

                    # On affiche alors une carte vide
                    m = folium.Map(location=[loca.Lat(i),loca.long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
                    print("Pas d'itinéraire possible")
                    return m 
                
                # Si l'utilisateur insère un contrainte supérieure
                # Au nombre de sortie optimum 
                # On réinitialise alors la contrainte

                elif nbSorties >= k_opti(S):
                    nbSorties = k_opti(S)

        
                else:
                
                # Sinon la contrainte reste inchangée

                    nbSorties=nbSorties

                # On spécifie tout de même l'itinéraire optimal

                print("Itinéraire optimal de "+ str(k_opti(S)) +" "+"sorties.")


                # On liste les sorties à l'aide des numéros arrangés
                li = trajet_optimal_min(i,j)[nbSorties][1]
                locationList=[]
                # Dans locationList nous insérons les coordonnées 
                # Correspondant numéros arrangés de li
                for point in range(len(li)):
                    locationList.append(loca.latLong(li[point]))
                
                # Création de l'itinéraire entre 
                # Le point de départ et le point d'arrivée
                coords = (loca.longLat(i),loca.longLat(j))

                # Utilisation de openrouteservice
                # Il faudra ici utiliser une clef API

                client = openrouteservice.Client(key=APIkey)

                # Ici on calculera l'itinéraire entre nos deux points
                # En utilisant preference="fastest" 
                # Afin d'être sur de rester sur l'autoroute 
                res = client.directions(coords,preference="fastest")
                geometry = client.directions(coords)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                # Fonction pour rendre l'itinéraire cliquable
                # On insère les information de distance 
                # De durée et de coût du trajet
                distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
                duration_txt = "<h4> <b>Durée :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
                price_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+ str(round((trajet_optimal_min(i,j)[nbSorties][0])/round(res['routes'][0]['summary']['distance']/1000,1),2))+" € /km. Soit </strong>"+str((trajet_optimal_min(i,j)[nbSorties][0]))+" €  </strong>" +"</h4></b>"
                
                # Initialisation carte
                m = folium.Map(location=[loca.Lat(i),loca.long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt+price_txt,max_width=300)).add_to(m)

                # Initialision des points correspondants aux péages
                for loc in range(len(locationList)):

                    folium.Marker(
                        locationList[loc],
                        popup=df["NOMGARE"][li[loc]],
                        icon=folium.Icon(icon_color='black',icon='road')
                    ).add_to(m)

                histo(DEPART,ARRIVEE)
                return m
        else:
            return "Vos variables n'ont pas le bon format ou utilisez la fonction 'nomCoord'"

    # Fonction calcul distance entre deux points en passant par l'autoroute
    def distance(i,j):

        coords = ((loca.long(i),loca.Lat(i)),(loca.long(j),loca.Lat(j)))
        client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
        res = client.directions(coords, preference="fastest")
        dist=float(round(res['routes'][0]['summary']['distance']/1000,1))
        return dist

##############################################################################
#%%

############### INITIALISATION DES DONNEES CARTE AVEC WIDGETS #########################

# Initialisation d'une liste d'entiers
# Allant de 1 à 10
# Pour l'initialisation de la contrainte de sorties
k=[]
for i in range(11):
    k.append(i)

############################## FIN ##########################################
