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



%config InlineBackend.figure_format = 'retina'
plt.rcParams['figure.figsize'] = (10, 10)
address = 'Footscray Railway Station Victoria, 3011, Australia'
geocoder = Nominatim(user_agent='Isochrone calculator')
location = geocoder.geocode(address)
location

m = folium.Map((location.latitude, location.longitude), max_zoom=20, zoom_start=16)
folium.Marker((location.latitude, location.longitude), popup=address).add_to(m)
m