# Graphy


    from numpy import string_
    import pandas as pd
    import openrouteservice
    from openrouteservice import convert
    import folium
    import json
    from algo_tarifs import *
    from ipywidgets import interact
    from histogramme import histo
    from donnees import *


## CALCUL DE COORDONNEES

recherche des coordonnées en fonction du nom de la gare

    def nomCoord(char):
    y= -1
        for i in range(len(df)):
            if df["NOMGARE"][i]==char:
                y=i
        if y==-1:
            return "ERREUR : Ce nom n'a pas été trouvé"
        else:
            return y

recherche du nom de la gare en fonction du numéro arrangé

    def indCoord(i):
        #on vérifie que i est bien de type entier
        if isinstance(i,int)== True and 0<=i<=42:

            return df["NOMGARE"][i]
    
        else: 
            return "veuillez inserer un entier entre 0 et 42"

recherche des coordonnées dans l'ordre lattitude longitude d'un péage en fonction du numéro arrangé

    def latLong(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['Y'][i],df['X'][i]
        else:
            return 'élément inconnu'

recherche des coordonnées dans l'ordre longitude lattitude d'un péage en fonction du numéro arrangé

    def longLat(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['X'][i],df['Y'][i]
        else:
            return 'élément inconnu'

recherche de la lattitude d'un péage en fonction de son numéro arrangé

    def Lat(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['Y'][i]
        else:
            return 'élément inconnu'

recherche de la longétitude d'un péage en fonction de son numéro arrangé
    
    def long(i):
        #On verifie que i correspond bien à un élément de la liste
        if 0<=i<=42:
            return df['X'][i]
        else:
            return 'élément inconnu'


calcul du nombre optimum de sorties pour payer le tarif le moins élevé lors d'un itinéraire entre deux points A et B.

    def k_opti(S):
        #si la fonction retourne -1 c'est qu'il n'y a pas 
        #d'itinéraire possible
        if S ==-1:
            return S

            return len(S)-1



## GRAPHE INTERACTIF 

Creation classe graphique

Elle permet d'afficher un graphe interactif 

class graphique:
    
    def __init__(self) -> None:
        pass

    def graph_rang(DEPART,ARRIVEE,nbSorties):
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
                i = nomCoord(DEPART)
                j = nomCoord(ARRIVEE)

                S = trajet_optimal_min(i,j)
                # On traite le cas où il n'y a pas d'itinéraire possible
                if k_opti(S)==-1:

                    # On affiche alors une carte vide
                    m = folium.Map(location=[Lat(i),long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
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
                    locationList.append(latLong(li[point]))
                
                # Création de l'itinéraire entre 
                # Le point de départ et le point d'arrivée
                coords = (longLat(i),longLat(j))

                # Utilisation de openrouteservice
                # Il faudra ici utiliser une clef API
                client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')

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
                m = folium.Map(location=[Lat(i),long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
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

    # Fonction calcul distance
    def distance(i,j):
        coords = ((df["X"][i],df["Y"][i]),(df["X"][j],df["Y"][j]))
        client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
        res = client.directions(coords, preference="fastest")
        dist=float(round(res['routes'][0]['summary']['distance']/1000,1))
        return dist


## INITIALISATION CARTE AVEC WIDGETS 

Initialisation

    k=[]
    for i in range(11):
    k.append(i)

Y = Liste des sorties 

    Y = [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 33, 35, 36, 37, 38, 39, 40, 41, 42 ]
    df_nom=[]

On insère alors dans df_nom tout les noms de gare correspondants aux numéros arrangés de Y
    
    for i in range(len(Y)):
    df_nom.append(df["NOMGARE"][Y[i]])



On obtient alors un graphe interactif, où l'on peut sélectionner notre point de depart et d'arrivée, ainsi que notre contrainte de nombre de sorties intermédiares maximum autorisé :

    interact(graphique.graph_rang,DEPART= df_nom, ARRIVEE= df_nom,nbSorties = k)

