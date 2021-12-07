# CODE A EXECUTER POUR LANCER LE PROGRAMME

#%%
from mapsud.graph import *
from ipywidgets import interact

#%%

################################################################################

interact(graphique.graph_rang,DEPART= tabOpti(df), ARRIVEE= tabOpti(df),nbSorties = k, APIkey='')





