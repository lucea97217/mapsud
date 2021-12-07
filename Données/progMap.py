# CODE A EXECUTER POUR LANCER LE PROGRAMME

#%%
from mapsud.graph import *
from ipywidgets import interact

#%%

################################################################################

interact(graphique.graph_rang,DEPART= tabOpti(df), ARRIVEE= tabOpti(df),nbSorties = k, APIkey='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')


# %%
