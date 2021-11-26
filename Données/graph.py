#%%
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
    if x==0 or y ==0:
        return "ERREUR : Ce nom n'a pas été trouvé"
    else:
        return x,y


#%%
class graphique:
    def __init__(self) -> None:
        pass
    def graph(x,y,x1,y1):
        coords = ((x,y),(x1,y1))
        client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
        res = client.directions(coords)
        geometry = client.directions(coords)['routes'][0]['geometry']
        decoded = convert.decode_polyline(geometry)
        distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
        duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

        m = folium.Map(location=[y,x],zoom_start=10, control_scale=True,tiles="cartodbpositron")
        folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)

        folium.Marker(
            location=list(coords[0][::-1]),
            popup=df["NOMGARE"][0],
            icon=folium.Icon(color="green"),
        ).add_to(m)

        folium.Marker(
            location=list(coords[1][::-1]),
            popup=df["NOMGARE"][30],
            icon=folium.Icon(color="red"),
        ).add_to(m)

        return m

    def distance(x,y,x1,y1):
        coords = ((x,y),(x1,y1))
        client = openrouteservice.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
        res = client.directions(coords)
        dist=str(round(res['routes'][0]['summary']['distance']/1000,1))
        return dist


#%%
#initialisation coord
x,y= df["X"][5],df["Y"][5] ## choisir point de départ
x1,y1=df["X"][33],df["Y"][33] ## point d'arrivée
# %%
#exemple affichage distance

graphique.distance(x,y,x1,y1)
# %%
#exemple affichage graph

graphique.graph(x,y,x1,y1)
# %%
#exemple return coordonnées
nomCoord(df,"VENDARGUES")
# %%
