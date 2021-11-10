# %%
import osmnx
x1,y1= GPS[1]
x2,y2 = GPS[10]
osmnx.distance.euclidean_dist_vec(y1,x1,y2,x2)


# %%
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


x1,y1= GPS[1]
x2,y2 = GPS[10]

%config InlineBackend.figure_format = 'retina'
plt.rcParams['figure.figsize'] = (10, 10)
address = 'Montpellier, 34000, France'
geocoder = Nominatim(user_agent='Isochrone calculator')
location = geocoder.geocode(address)
location 

m = folium.Map((location.latitude, location.longitude), max_zoom=20, zoom_start=16)
folium.Marker((location.latitude, location.longitude), popup=address).add_to(m)
m
# %%
