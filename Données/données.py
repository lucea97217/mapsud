#%%
#### IMPORT BIBLIOTHEQUES ###
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import alphashape
from descartes import PolygonPatch
import folium
import geopandas as gpd
from geopy.geocoders import Nominatim
from ipywidgets import interact, fixed, widgets
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import osmnx as ox
import pandas as pd
from shapely import geometry
from pyroutelib3 import Router
from pyproj import Proj, transform

pd.options.display.max_rows = 8
 
#%%

pd.options.display.max_rows = 8
 
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
L19 = [ 18.8 , 18.8 , 18.8 , 18.8 , 18.8 , 18.8 , 16.2 , 13.8 , 13.5 , 11.8 , 9.6 , 9.2 , 7.1 , 5.9 , 3.1 , 2.6 , -1 , -1 , 0.8 ]

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

def tarif (i,j) :   # i,j = numéros "arrangés" des sorties d'autouroutes

    if ( 0 <= i <= 42) and ( 0 <= j <= 42 ) :

        if i == j :
            print("Erreur : sortie = entrée")
        else :
            n = max(i,j)
            m = min(i,j)
            a = TARIF[n-1][m]
            
            if a == -1 :
                print("Il n'existe pas d'itinéraire entre ces deux sorties")
            else :
                return( a )

    else :
        print("Erreur : numéro incorrecte")

    
#
# %%

df_brut = pd.read_csv('Gares-peage_2019.csv' , sep = ';' )

# On récupére les indices des lignes qui ne nous intéresse pas.
# C'est à dire toutes celles qui ne sont pas A9, A61, A62, A66, A75, A620, A709.
X = df_brut['ROUTE']

A = []
for i in range (len(X)) :

    if X[i] not in ["A0009", "A0061", "A0062", "A0066", "A0075", "A0620", "A0709"] :
       df_brut.drop(i,0,inplace=True)

# mise à jour des index 

df_brut.reset_index(inplace=True,drop=True)



#%%

################################################################################

# Maintenant on va transfomer les colonnes X,Y (coordonées Lambert)
# en coordonnées GPS :

X = df_brut['X']
Y = df_brut['Y']



inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')

GPS = []   # couples (x,y)
for i in range (len(df_brut)) :
    GPS.append( transform(inProj, outProj, X[i], Y[i] ) )

#%%
tab = { 'ROUTE':df_brut["ROUTE"], 'NOMGARE':df_brut["NOMGARE"], 'COORDONNEES':GPS }
df_new = pd.DataFrame(tab)
df_new.reindex()
tab = { 'ROUTE':df_brut["ROUTE"], 'NOMGARE':df_brut["NOMGARE"], 'COORDONNEES':GPS }

df_new = pd.DataFrame(tab)


#%%

######## SUPRESSION ARRETS USELESS #########
df_coord = df_new.copy()
df_coord.iloc[0]=df_new.iloc[8]
df_coord.iloc[1]=df_new.iloc[9]
df_coord.iloc[2]=df_new.iloc[10]
df_coord.iloc[3]=df_new.iloc[52]
df_coord.iloc[4]=df_new.iloc[51]
df_coord.iloc[5]=df_new.iloc[11]
df_coord.iloc[6]=df_new.iloc[12]
df_coord.iloc[7]=df_new.iloc[13]
df_coord.iloc[8]=df_new.iloc[14]
df_coord.iloc[9]=df_new.iloc[15]
df_coord.iloc[10]=df_new.iloc[16]
df_coord.iloc[11]=df_new.iloc[17]
df_coord.iloc[12]=df_new.iloc[19]
df_coord.iloc[13]=df_new.iloc[18]
df_coord.iloc[14]=df_new.iloc[20]
df_coord.iloc[15]=df_new.iloc[28]
df_coord.iloc[16]=df_new.iloc[27]
df_coord.iloc[17]=df_new.iloc[26]
df_coord.iloc[18]=df_new.iloc[25]
df_coord.iloc[19]=df_new.iloc[24]
df_coord.iloc[20]=df_new.iloc[23]
df_coord.iloc[21]=df_new.iloc[47]
df_coord.iloc[22]=df_new.iloc[48]
df_coord.iloc[23]=df_new.iloc[49]
df_coord.iloc[24]=df_new.iloc[22]
df_coord.iloc[25]=df_new.iloc[21]

for i in range(len(df_coord)-24):
    df_coord.drop(24+i,0,inplace=True)


# %%

########## CALCUL DISTANCE #############
import requests
import json

# Def calcul de distance
def distance(x,y,x1,y1):
#calcul des distances entre les payages en restant sur la route
#on utilise les coordonnées récoltées précédemment

    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")

    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]
    return (round(route_1['distance']/1000,1))
#%%
#ajout de la variable distance au tableau des coordonnées
coord=[]
for i in range(len(df_coord)):
    coord.append(df_coord["COORDONNEES"][i])

#%%
####compteur####
count=[]
for i in range(len(df_coord)):
    count.append(i)
#%%
tab = { 'ROUTE':df_coord["ROUTE"], 'NOMGARE':df_coord["NOMGARE"], 'COORDONNEES':coord}
df_coord = pd.DataFrame(tab)


# %%
###### INSERTIONS DONNEES MANQUANTES ######

def Insert_row(row_number, df, row_value): 
    
    start_upper = 0
   
    
    end_upper = row_number 
   
    
    start_lower = row_number 
   
    
    end_lower = df.shape[0] 
   
    
    upper_half = [*range(start_upper, end_upper, 1)] 
   
    
    lower_half = [*range(start_lower, end_lower, 1)] 
   
    
    lower_half = [x.__add__(1) for x in lower_half] 
   
    
    index_ = upper_half + lower_half 
   
    
    df.index = index_ 
   
    
    df.loc[row_number] = row_value 
    
    
    df = df.sort_index() 
   
    
    return df 

   

#%%
########## CONVERT TO CSV #######
df_coord.to_csv('coordonnees.csv')



# %%
