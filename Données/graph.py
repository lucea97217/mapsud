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
    return trajet_optimal_min(i,j)[len(trajet_optimal_min(i,j))-1][2]
#%%
class graphique:
    def __init__(self) -> None:
        pass
    def graph_rang(char1,char2,k):
        if isinstance(char1,str)==True and isinstance(char2,str)==True:
            i = nomCoord(char1)
            j = nomCoord(char2)
            print(i,j)
            if k >= k_opti(i,j):
                k = k_opti(i,j)
                print("Au dessus de "+ str(k)+" " +" sorties supplémentaires le prix reste inchangé.")
            else:
                k=k
            
            li = trajet_optimal_min(i,j)[k][1]
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
            price_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+ str(round((trajet_optimal_min(i,j)[k][0])/round(res['routes'][0]['summary']['distance']/1000,1),2))+" € /km. </strong>" +"</h4></b>"
            m = folium.Map(location=[Lat(i),long(i)],zoom_start=10, control_scale=True,tiles="cartodbpositron")
            folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt+price_txt,max_width=300)).add_to(m)
            for loc in range(len(locationList)):

                folium.Marker(
                    locationList[loc],
                    popup=df["NOMGARE"][loc+i],
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
df_nom = list(df['NOMGARE'])
#%%
df_nom2 = df_nom[1:42]
#%%
li=[]
for j in range(43):
    li.append(j)

#%%
k=[]
for i in range(11):
    k.append(i)

#%%

interact(graphique.graph_rang,char1= df_nom, char2= df_nom2 ,k = k)
#%%
######### histogramme

nomCoord('VENDARGUES')

# %%
