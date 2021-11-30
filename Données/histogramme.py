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

          fig = px.bar(data, x=name_axe_x, y=name_axe_y)
          fig.show()

          return fig.show()

     R = trajet_optimal_min(nomCoord(DEPART),nomCoord(ARRIVEE))

     name_axe_x = "Nombre de sortie maximale autorisée"
     name_axe_y = "prix (€)"
     d = {name_axe_x: [], name_axe_y: []}
     for n in range(len(R)):
          d[name_axe_x].append(R[n][2])
          d[name_axe_y].append(R[n][0])
     print(d)

     data = pandas.DataFrame(d)
     print(d)
     plt.hist(data)
     #fig = px.bar(data, x=name_axe_x, y=name_axe_y)
     #fig.show()
     
     return plt.show()

     

#%%
li=['VENDARGUES']
li2=['PAMIER SUD']

#%% 
hist('VENDARGUES','PAMIER SUD')
# %%
interact(hist,DEPART = df_nom, ARRIVEE = df_nom)


# %%

L = [1,2,3]
M = [5,5,5]
data = [L,M]
plt.hist(L)

# %%
