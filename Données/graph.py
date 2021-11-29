#%%
from numpy import string_
import pandas as pd
import openrouteservice
from openrouteservice import convert
import folium
import json
from algo_tarifs import *
from ipywidgets import interact

#%%
#IMPORT TABLEAU COORDONNEES
df = pd.read_csv("coordonnees.csv", sep=",")

#%%
#sion veut supprimer les index
del df["index"]

#%%
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

#%%
def indCoord(i):
    if isinstance(i,int)== True and 0<=i<=42:

        return df["NOMGARE"][i]
    
    else: 
        return "veuillez inserer un entier entre 0 et 42"

#%%

def latLong(i):
    if 0<=i<=42:
        return df['Y'][i],df['X'][i]
    else:
        return 'élément inconnu'

#%%
def longLat(i):
    if 0<=i<=42:
        return df['X'][i],df['Y'][i]
    else:
        return 'élément inconnu'
#%%
def Lat(i):
    if 0<=i<=42:
        return df['Y'][i]
    else:
        return 'élément inconnu'
#%%
def long(i):
    if 0<=i<=42:
        return df['X'][i]
    else:
        return 'élément inconnu'

#%%
def k_opti(i,j):
    if trajet_optimal_min(i,j)==False:
        k= -1
        return k
 
    return len(trajet_optimal_min(i,j))-1
#%%
class graphique:
    def __init__(self) -> None:
        pass
    def graph_rang(DEPART,ARRIVEE,nbSorties):
        if isinstance(DEPART,str)==True and isinstance(ARRIVEE,str)==True:
            if DEPART == ARRIVEE:
                return 'Trajet impossible'
            else:
                i = nomCoord(DEPART)
                j = nomCoord(ARRIVEE)

                if k_opti(i,j)==-1:

                    m = folium.Map(location=[Lat(i),long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
                    print("Pas d'itinéraire possible")
                    return m 
                elif nbSorties >= k_opti(i,j):
                    nbSorties = k_opti(i,j)
                    print("Au dessus de "+ str(nbSorties)+" " +" sorties supplémentaires le prix reste inchangé.")
        
                else:
                    nbSorties=nbSorties
                print("Itinéraire optimal de "+ str(nbSorties) +""+"sorties.")
                li = trajet_optimal_min(i,j)[nbSorties][1]
                locationList=[]
                for point in range(len(li)):
                    locationList.append(latLong(li[point]))
                coords = (longLat(i),longLat(j))
                client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
                res = client.directions(coords,preference="fastest")
                geometry = client.directions(coords)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)
                distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
                duration_txt = "<h4> <b>Durée :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
                price_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+ str(round((trajet_optimal_min(i,j)[nbSorties][0])/round(res['routes'][0]['summary']['distance']/1000,1),2))+" € /km. Soit </strong>"+str((trajet_optimal_min(i,j)[nbSorties][0]))+" €  </strong>" +"</h4></b>"
                m = folium.Map(location=[Lat(i),long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt+price_txt,max_width=300)).add_to(m)
                for loc in range(len(locationList)):

                    folium.Marker(
                        locationList[loc],
                        popup=df["NOMGARE"][li[loc]],
                        icon=folium.Icon(icon_color='black',icon='road')
                    ).add_to(m)

            
                return m
        else:
            return "Vos variables n'ont pas le bon format ou utilisez la fonction 'nomCoord'"


    def distance(i,j):
        coords = ((df["X"][i],df["Y"][i]),(df["X"][j],df["Y"][j]))
        client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
        res = client.directions(coords, preference="fastest")
        dist=float(round(res['routes'][0]['summary']['distance']/1000,1))
        return dist


#%%
k=[]
for i in range(11):
    k.append(i)
#%%

Y = [ 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 33, 35, 36, 37, 38, 39, 40, 41, 42 ]
df_nom=[]
for i in range(len(Y)):
    df_nom.append(df["NOMGARE"][Y[i]])

#%%

interact(graphique.graph_rang,DEPART= df_nom, ARRIVEE= df_nom,nbSorties = k)




# %%
trajet_optimal_min(40,42)
# %%
# %%
