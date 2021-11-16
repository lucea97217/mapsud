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
client = openrouteservice.Client(key='5b3ce3597851110001cf62485fa977bf16a24e2387854486dad592d8')
#%%
#initialisation coord
x,y= df["X"][0],df["Y"][0] ## choisir point de départ
x1,y1=df["X"][30],df["Y"][30] ## point d'arrivée
coords = ((x,y),(x1,y1))

#%%

res = client.directions(coords)
#%%
geometry = client.directions(coords)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

# %%
######### distance resultante, calcul distance ##########
dist=str(round(res['routes'][0]['summary']['distance']/1000,1))
#%%
distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

m = folium.Map(location=[43.30366439969685,3.2229492234270127],zoom_start=10, control_scale=True,tiles="cartodbpositron")
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

m


