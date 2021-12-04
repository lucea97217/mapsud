# Histogramme

    import pandas
    from algo_tarifs import trajet_optimal_min
    import plotly.express as px

    from ipywidgets import interact
    import matplotlib.pyplot as plt
    import pandas as pd
    from donnees import *
    
Fonction prenant en compte un point de départ A, et un point d'arrivée B, et retournant un diagramme en baton des tarifs en fonction de la contrainte k sorties intermédiares maximum autorisées.
k allant de 0 jusqu'à l'optimum, c'est à dire jusqu'à la contrainte qui, à partir d'elle, ne permet plus d'amélioration sur le tarif.
Les prix sont bien sûr décroissant lorsque k augmente, c'est à dire lorsqu'on a la possiblité d'emprunter un plus grand nombre de sorties, et donc d'optimiser son itinéraire.

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

Exemple entre Vendargues et Sesquières :

    histo('VENDARGUES', 'SESQUIERES')

# ------------Capture3-------------




