
![Capture](relative/path/to/img.png?raw=true "Capture1") 


# Algo_tarifs

    from donnees import tarif
    
Cette partie concerne l'algorithme recherchant le trajet optimal entre deux sorties d'autoroutes.
Etant donnée une entrée A et une sortie B, il apparaît parfois préférable de ne pas faire un direct entre A et B pour minimiser le tarif.
Quitter l'autoroute lors d'une sortie intermédiaire, puis re-rentrer immédiatement après, diminue parfois le coût du trajet global.

La partie ci-dessous recherche donc le chemin optimal entre A et B, avec la contrainte k sorties intermédiares maximum autorisées. Si k=0, alors l'itinéraire correspond à un direct entre A et B. Si k=1, alors nous nous autorisons maximum une sortie intermédiare, etc ...
Il existe une contrainte q à partir de laquelle le trajet optimal entre A et B ne pourra plus être amélioré. C'est à dire que s'accorder une contrainte plus élevé ne permettra pas de trouver un itinéraire moins coûteux.


1) Dans un premier temps, nous aurons besoin, étant donnée une entrée A et une sortie B, de récupérer l'ensemble des sorties intermédiares entre A et B.

Nous commençons par ordonner les sorties d'autoroutes :
    

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

On crée ensuite la fonction qui retourne la liste des sorties intermédiaires situées entre deux points i et j :

 
    def sortie_intermédiaire (i, j) :       #i et j numéros arrangés des sorties départ et arrivée 
    
    S = [ ]              # le futur return des sorties intermédiaires

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


2) Nous pouvons maintenant créer la fonction calculant le trajet optimal entre A et B, avec la contrainte k allant de 0 au maximum envisageable :

       # Fonction algorithme une sortie, voir papier

        def comparaison (A, B, Liste, Li) :

        alpha = tarif(A, B)
        W = [A, B]
        for (k, c1) in Liste :
            for (l, c2, Z) in Li :

                if k == l :
                    if ( c1 != -1 ) and ( c2 != -1 ) :   # Si il existe un trajet possible entre A et k, puis entre k et B

                        if c1 + c2 < alpha :
                            alpha = c1 + c2
                            W = Z.copy()
                            W.insert(0, A)

                        if ( c1 + c2 == alpha ) and ( len(Z) < len(W)-1 ) :
                            W = Z.copy()
                            W.insert(0, A)


        return( alpha, W )
        

        # Fonction trajet optimal

        def trajet_optimal (A, B) :   # A, B les entrée et sortie = numéros "arrangées"

        if (A == B) or (A not in Y) or (B not in Y) :   # Y = ensemble des sorties possibles
            return(False)

        S = []   # Ensemble des solutions avec contrainte (tarif + trajet optimaux)
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
                L0.append ( ( k, tarif(k,B), [k,B] ) )     # Tarif + trajet optimal entre k et B, avec 0 arrêt possible

            L.append(L0)
            (a, W) = comparaison (A, B, Liste1, L0)   # Tarif + trajet optimal entre A et B avec 1 arrêt possible
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

                        (a, W) = comparaison( k, B, N, M )   # Tarif + trajet optimal entre k et B, avec t-1 arêts possibles, où 1 <= t-1 : étape de la boucle
                        Lbis.append( ( k, a, W ) )
        
            L.append(Lbis)
            # 2ème connection, voir papier
            (a, W) = comparaison( A, B, Liste1, Lbis )   # Tarif + trajet optimal entre A et B avec t arrêts possibles
            S.append( (round(a,1), W, t) )

        return(S)

Exemple : trajets optimaux entre Vendargues(0) et Sesquières(42). Pour chaque contrainte k allant de 0 au maximum enviseagble, on retrouve le tarif, et le trajet optimal :

    trajet_optimal (0, 42)

# -------Capture1.png--------

Fonction supprimant les "doublons" de la fonction ci-dessus. C'est à dire les itinéraires correspondant à une contrainte k supérieur à la contrainte q optimal.

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
            

Exemple : trajets optimaux entre Vendargues(0) et Sesquières(42) :

    trajet_optimal_min (0, 42)
    
# -------Capture.png--------

