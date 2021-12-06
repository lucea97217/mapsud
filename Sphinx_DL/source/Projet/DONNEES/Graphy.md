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


calcul du nombre optimum de sorties pour payer le tarif le moins élevé lors d'un itinéraire entre deux points A et B.

    def k_opti(S):
        #si la fonction retourne -1 c'est qu'il n'y a pas 
        #d'itinéraire possible
        if S ==-1:
            return S

            return len(S)-1



## CLASSE GRAPHIQUE

Creation de la classe graphique

Elle permet d'afficher le compte rendu final du projet via la fonction graph_rang(DEPART,ARRIVEE,nbSorties,APIkey).

(Création d'une APIkey personnelle nécessaire ! voir page de présentation du projet pour avoir un tutoriel).

Elle affiche à l'écran un graphique interractif permettant à l'utilisateur de sélectionner une entrée A et une sortie B, ainsi que k le nombre maximum de sorties intermédiaires autorisées, pour le trajet optimisant le tarif entre A et B.

Apparaît alors à l'écran une carte cliquable avec l'itinéraire optimal surligné, ainsi que plusieurs informations sur celui-ci, comme la durée estimé, la distance, ou encore le tarif prévu pour le péage. Apparaît également le diagramme en baton comparant les tarifs selon la contrainte k.
    
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

    # Initialisation d'une liste d'entiers
    # Allant de 1 à 10
    # Pour l'initialisation de la contrainte de sorties
    k=[]
    for i in range(11):
        k.append(i)


## EXEMPLE 

Nous obtenons alors le graphe interactif décris plus haut, sur lequel nous pouvons sélectionner notre point de depart A et d'arrivée B, ainsi que notre contrainte de nombre de sorties intermédiares maximum autorisées.

Nous avons la carte cliquable avec l'itinéraire, ainsi que le diagramme comparant l'évolution du tarif selon la contrainte.

Voici la syntaxe, et un exemple :

    interact(graphique.graph_rang,DEPART= tabOpti(df), ARRIVEE= tabOpti(df),nbSorties = k, APIkey='#####################################')
    
<img src="https://github.com/lucea97217/Projetgroupe6/blob/23a68b81a13c988690123226e56a5d861a5c6af1/Sphinx_DL/source/Projet/DONNEES/Capture/exemple_prog_graph.png" width="400" />

