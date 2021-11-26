#%%

from données.py import tarif

tarif(1.2)

#%%

sortie_intermédiaire( 11 , 27 , A_ )


# %%

#################################################################################################

# Les An correspondent aux tronçons d'autoroutes avant intersection avec une autre.
# Nous nous en servons pour ordonner les sorties.
# An = [ Liste0, Liste1, Liste2 ]
# Liste 0 = liste des sorties
# Liste 1 = tronçons d'autouroutes connecté à An par la gauche  (premier élèment de Liste0)
# Liste 2 = tronçons d'autouroutes connecté à An par la droite  (dernier élément de Liste0) 

A0 = [ [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11 ] , [] , [1, 2] ]    # A9 Nord

A1 = [ [ 12, 13, 14, 15, 16, 19 ] , [0, 2] , [] ]   # A9 Sud

A2 = [ [ 20, 21, 22, 23, 24, 25 ] , [0, 1] , [3, 4] ]   # A61 Est

A3 = [ [ 26, 27, 29, 30 ] , [2, 4] , [] ]   # A66

A4 = [ [ 31, 33, 35, 36, 37, 38, 39, 40, 41, 42] , [2, 3] , [] ]   # A61 Ouest

A_ = [A0, A1, A2, A3, A4]

# On créer une fonction qui retourne la liste des sorties intermédiaires
# situées entre deux points i et j

def sortie_intermédiaire (i, j, A_) :     # i et j numéros arrangés des sorties départ et arrivée

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

###########################################################################################

#%%

def trajet_optimal (A, B) :      # A, B les entrée et sortie = numéros "arrangées"


