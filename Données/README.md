# Introduction

Bienvenue sur le projet du groupe 6 !

L'objectif de ce package est de fournir une lecture compréhensible des tarifs autoroutiers (2021) concernant la région Occitanie,  entre Montpellier, Toulouse, et la frontière espagnole.

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/Capture5.PNG" width="400" />

La liste détaillé des tarifs est disponible sur https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf (page 3).

L'utilisateur aura la possiblité de sélectionner deux points parmis l'ensemble des sorties d'autoroutes de la région concernée, une entrée A et une sortie B.  
1) Le programme lui proposera en retour une carte intéractive et cliquable, affichant l'itinéraire entre A et B surligné en bleu (itinéraire passsant uniquement par l'autoroute). Ainsi que d'autres indicateurs, comme la durée estimée, la distance, le prix totale, ou encore le prix moyen au kilomètre.  
2) Il apparaît parfois préférable, pour aller de A jusqu'en B, de quitter l'autoroute lors d'une sortie intermédiaire, puis de la réintégrer immédiatement après, afin de minimiser le coût du péage sur le trajet global entre A et B. Il seraît donc intéressant de chercher le tajet optimal minimisant le coût (sans pour autant augmenter la distance donc).  
Un diagramme en baton affichera le coût du trajet optimal en fonction de k le nombre de sorties maximum autorisées (c'est à dire en s'accordant le droit de sortir de l'autoroute, pour re-rentrer immédiatement après, k fois maximum).    
L'utilisateur aura également la possiblité de sélectionner sa contrainte k, et le programme adaptera l'itinéraire sur la carte en conséquence, affichant notamment les k sorties intermédiares.

Voici un exemple entre la sortie A = St-Jean-de-Védas, et B = Carcassane ouest, passant par l'A709, A9, A61 (nbSorties correspond à la contrainte k) :

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/exemple_prog_graph.png" width="400" />

La contrainte k = 0 sorties autorisées correspond au cas du direct entre A et B. Au-delà de 5 sorties maximums autorisées, pour cet exemple, on ne peut plus optimiser le coût du trajet, et donc s'accorder d'avantage de sorties n'apporterait rien. C'est pourquoi le programme ne propose pas d'itinéraire comportant plus de 5 sorties.

# Installation

Tout d'abord lancer le terminal, et exécuter la commande ci-dessous, afin d'installer les packages nécessaires au bon fonctionnement :

    $ pip install mapsud numpy pandas openrouteservice folium matplotlib ipywidgets
     
**Il vous faudra ensuire créer une clé API personnelle** (moins de 1min). Vous ne pouvez pas utiliser la clé d'une autre personne.

--> Pour cela, suivre le lien https://openrouteservice.org/dev/#/signup, et les instructions suivantes :

1/ Tout d'abord vous devez créer un compte (on peut utiliser "sign up with github" pour aller plus vite) :

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_6.PNG" width="500" />

2/ Ensuite connecter vous à celui-ci :

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_7.PNG" width="400" />

3/ Dans l'onglet "TOKENS", puis dans la rubrique "Request a token", créer une nouvelle clé :

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_8.PNG" width="800" />

4/ Votre clé apparaît sous la forme d'une chaîne de caractère, que vous pouvez copier-coller pour la suite.

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_9.PNG" width="800" />

# Utilisation

1) Ouvrir un éditeur de code (tel que VS-code), puis copier-coller le code ci-dessous :

       # CODE A EXECUTER POUR LANCER MAPSUD
       #%%
        
       import ssl
       ssl._create_default_https_context = ssl._create_unverified_context
       from mapsud.graph import map
        
       #%%

       map("APIkey") 
        
       #%%

2) Remplacer APIkey par votre clé API personelle, puis executer le code.  
La fonction map() a besoin comme argument d'une chaîne de caractère, veillez donc à laisser les guillemets.

3) Une interface graphique s'affiche, il ne vous reste plus qu'à sélectionner votre point de Départ et d'Arrivée, ainsi que la contrainte du nombre de sorties maximums autorisées (nbSorties). Sachant que la contrainte correspondante au trajet le moins cher (parmis tout les trajets possibles) est affichée sur une ligne de texte.

Exemple entre St-Jean-de-Védas et la frontière espagnole, avec l'itinéraire optimal comportant maximum 3 sorties. Pour ce parcours, le trajet optimal est atteint pour 5 sorties autorisées.

<img src="https://raw.githubusercontent.com/lucea97217/mapsud/main/Sphinx_DL/source/Projet/DONNEES/Capture/Capture12.PNG" width="500" />

