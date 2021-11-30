#%%
import pandas
from algo_tarifs import trajet_optimal_min
import plotly.express as px
from graph import nomCoord,df_nom
from ipywidgets import interact
import matplotlib.pyplot as plt


#%%

def histo(DEPART,ARRIVEE):
     if DEPART == ARRIVEE:
          name_axe_x = "Nombre de sortie maximale autorisée"
          name_axe_y = "prix (€)"
          d = {name_axe_x: [], name_axe_y: []}
          data = pandas.DataFrame(d)
          plt.bar(d[name_axe_x],d[name_axe_y])
          print(" Pas d'itinéraire possible.")
          return plt.show()


     R = trajet_optimal_min(nomCoord(DEPART),nomCoord(ARRIVEE))

     name_axe_x = "Nombre de sortie maximale autorisée"
     name_axe_y = "prix (€)"
     d = {name_axe_x: [], name_axe_y: []}
     for n in range(len(R)):
          d[name_axe_x].append(R[n][2])
          d[name_axe_y].append(R[n][0])

     data = pandas.DataFrame(d)

     if d[name_axe_y]==[0] and d[name_axe_x]==[0]:
          plt.scatter(d[name_axe_x],d[name_axe_y])
          return plt.show()

     plt.bar(d[name_axe_x],d[name_axe_y])
     return plt.show()

     



#%% 
histo('VENDARGUES','PAMIER SUD')
# %%
interact(histo,DEPART = df_nom, ARRIVEE = df_nom)

# %%
