# INTRODUCTION

Bienvenue sur le projet du groupe 6 !

L'objectif de ce package est de fourir une lecture compréhensible des tarifs autoroutiers (2021) concernant la région entre Montpellier, Toulouse, et la frontière espagnole.

<img src="https://github.com/lucea97217/Projetgroupe6/blob/9a333e0e9263a3ddd4c0825bb65714172d1e228a/Sphinx_DL/source/Projet/DONNEES/Capture/Capture5.PNG" width="400" />

La liste détaillé des tarifs est disponible sur https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf (page 3).

L'utilisateur aura la possiblité de sélectionner deux points parmis l'ensemble des sorties d'autoroutes de la région concernée, une entrée A et une sortie B.  
1) Le programme lui proposera en retour une carte intéractive et cliquable, affichant l'itinéraire entre A et B surligné en bleu (itinéraire passsant uniquement par l'autoroute). Ainsi que d'autres indicateurs, comme la durée estimée, la distance, le prix totale, ou encore le prix moyen au kilomètre.  
2) Il apparaît parfois préférable, pour aller de A jusq'en B, de quitter l'autoroute lors d'une sortie intermédiaire, puis de la réintégrer immédiatement après, afin de minimiser le coût du péage sur le trajet global entre A et B. Il seraît donc intéressant de chercher le tajet optimal minimisant le coût (sans pour autant augmenter la distance donc).  
Un diagramme en baton affichera le coût du trajet optimal avec k sorties maximum autorisées (c'est à dire en s'accordant le droit de sortir de l'autoroute, pour re-rentrer immédiatement après, k fois maximum).    
L'utilisateur aura également la possiblité de sélectionner sa contrainte k, et le programme adaptera l'itinéraire sur la carte en conséquence, affichant notamment les sorties intermédiares.

Voici un exemple entre la sortie A = St-Jean-de-Védas, et B = Carcassane ouest, passant par l'A709, A9, A61 :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/23a68b81a13c988690123226e56a5d861a5c6af1/Sphinx_DL/source/Projet/DONNEES/Capture/exemple_prog_graph.png" width="400" />

La contrainte k = 0 sorties autorisées correspond au cas du direct entre A et B. Au-delà de 5 sorties maximums autorisées, pour cet exemple, on ne peut plus optimiser le coût du trajet, et donc s'accorder d'avantage de sorties n'apporterait rien. C'est pourquoi le programme ne propose pas d'itinéraire comportant plus de 5 sorties.

# INSTALLATION

Tout d'abord lancer le terminal, et exécuter les commandes ci-dessous, afin d'installer les packages nécessaires au bon fonctionnement :

    pip install #########
  
Ensuite installer la bonne version de python :

    commande ?
  
Télécharger le dossier github du projet sur votre ordinateur :

    J'y arrive pas, l'informatique c'est d'la m***e, je rage !#**%
    
**Il vous faudra ensuire créer une clé API personnelle** (moins de 1min).

--> Pour cela, suivre le lien https://openrouteservice.org/dev/#/signup, et les instructions suivantes :

Tout d'abord vous devez créer un compte (on peut utiliser "sign up with github" pour aller plus vite) :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_6.PNG" width="400" />

Ensuite connecter vous à celui-ci :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_7.PNG" width="500" />

Dans l'onglet "TOKENS", puis dans la rubrique "Request a token", créer une nouvelle clé :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_8.PNG" width="500" />

Votre clé apparaît sous la forme d'une chaîne de caractère, que vous pouvez copier-coller pour la suite.

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_9.PNG" width="500" />

# UTILISATION

