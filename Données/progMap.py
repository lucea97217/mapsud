#%%
from mapsud.graph import *
from ipywidgets import interact
#%%
# On obtient alors enfin un graphe interactif
# Ou on peut sélectionner notre lieux de depart
# Notre lieux d'arrivée 
# Et notre contrainte de nombre de sorties supplémentaires

################################################################################
interact(graphique.graph_rang,DEPART= tabOpti(df), ARRIVEE= tabOpti(df),nbSorties = k, APIkey='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')


# %%
