#%%
from numpy import string_
import pandas as pd
import openrouteservice
from openrouteservice import convert
import folium
import json

#%%
#IMPORT TABLEAU COORDONNEES
df = pd.read_csv("coordonnees.csv", sep=",")

#%%
#sion veut supprimer les index
del df["index"]

#%%
#recherche des coordonnées en fonction du nom de la gare
def nomCoord(df,char):
    x=0
    y=0
    for i in range(len(df)):
        if df["NOMGARE"][i]==char:
            x = df["X"][i]
            y = df["Y"][i]
            y=i
    if x==0 or y ==0:
        return "ERREUR : Ce nom n'a pas été trouvé"
    else:
        return y

#%%
def indCoord(df,i):
    if isinstance(i,int)== True and 0<=i<=42:

        return df["NOMGARE"][i]
    
    else: 
        return "veuillez inserer un entier entre 0 et 42"

#%%
class graphique:
    def __init__(self) -> None:
        pass
    def graph_rang(i,j,df):
        if isinstance(i,float)==True and isinstance(j,float)==True:
            coords = ((df["X"][i],df["Y"][i]),(df["X"][j],df["Y"][j]))
            client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
            res = client.directions(coords,preference="fastest")
            geometry = client.directions(coords)['routes'][0]['geometry']
            decoded = convert.decode_polyline(geometry)
            distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
            duration_txt = "<h4> <b>Durée :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
            price_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+ str(13.8)+" € . </strong>" +"</h4></b>"
            m = folium.Map(location=[df["Y"][i],df["X"][i]],zoom_start=10, control_scale=True,tiles="cartodbpositron")
            folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt+price_txt,max_width=300)).add_to(m)
        
            folium.Marker(
                location=list(coords[0][::-1]),
                popup=df["NOMGARE"][i],
                icon=folium.Icon(color="green"),
            ).add_to(m)

            folium.Marker(
                location=list(coords[1][::-1]),
                popup=df["NOMGARE"][j],
                icon=folium.Icon(color="red"),
            ).add_to(m)

            return m
        else:
            return "Vos variables n'ont pas le bon format ou utilisez la fonction 'nomCoord'"


    def distance(i,j,df):
        coords = ((df["X"][i],df["Y"][i]),(df["X"][j],df["Y"][j]))
        client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
        res = client.directions(coords, preference="fastest")
        dist=float(round(res['routes'][0]['summary']['distance']/1000,1))
        return dist

#%%
        for i in range(nb_points-2):

            coords=((df["X"][dep+1+i],df["Y"][dep+1+i]),(df["X"][dep+2+i],df["Y"][dep+2+i]))
            folium.Marker(
                location=list(coords[0][::-1]),
                popup=df["NOMGARE"][dep+1+i],
            ).add_to(m)

            folium.Marker(
                location=list(coords[1][::-1]),
                popup=df["NOMGARE"][dep+2+i],
            ).add_to(m)
            coords=0

        return m
#%%
#initialisation coord
x,y= df["X"][5],df["Y"][5] ## choisir point de départ
x1,y1=df["X"][30],df["Y"][30] ## point d'arrivée
# %%
#exemple affichage distance

graphique.distance(5,30,df)
# %%
#exemple affichage graph

graphique.graph_rang(5.0,30.0,df)


#%%
nomCoord(df,'PAMIER SUD')
# %%
#exemple return coordonnées
nomCoord(df,'MONTPELLIER')
# %%
types_trajet =  ["fastest", "shortest", "recommended"]

x1,y1 = df["X"][5] ,df["Y"][5] ## choisir point de départ
x2,y2 = df["X"][30]   ,df["Y"][30]   ## point d'arrivée

coords = ((x1,y1),(x2,y2))


client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')


trajets = []

for t in types_trajet:
    r = client.directions(coords,preference=t)
    propriete = r['routes'][0]['summary']
    print(propriete)
    trajets.append([t,propriete['distance']/1000,propriete['duration']/60])



# %%
#exemple def
indCoord(df,3)
# %%
