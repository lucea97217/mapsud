#%%
import pandas
from algo_tarifs import *
import plotly.express as px

#%%

R = trajet_optimal(3,19)

name_axe_x = "Nombre de sortie maximale autorisée"
name_axe_y = "prix (€)"
d = {name_axe_x: [], name_axe_y: []}
for n in range(len(R)):
     d[name_axe_x].append(R[n][2])
     d[name_axe_y].append(R[n][0])

data = pandas.DataFrame(d)

fig = px.bar(data, x=name_axe_x, y=name_axe_y)

fig.show()

#%%
