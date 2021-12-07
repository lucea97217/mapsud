# INTRODUCTION

Bienvenue sur le projet du groupe 6 !

L'objectif de ce package est de fournir une lecture compréhensible des tarifs autoroutiers (2021) concernant la région Occitanie,  entre Montpellier, Toulouse, et la frontière espagnole.

<img src="https://github.com/lucea97217/Projetgroupe6/blob/9a333e0e9263a3ddd4c0825bb65714172d1e228a/Sphinx_DL/source/Projet/DONNEES/Capture/Capture5.PNG" width="400" />

La liste détaillé des tarifs est disponible sur https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf (page 3).

L'utilisateur aura la possiblité de sélectionner deux points parmis l'ensemble des sorties d'autoroutes de la région concernée, une entrée A et une sortie B.  
1) Le programme lui proposera en retour une carte intéractive et cliquable, affichant l'itinéraire entre A et B surligné en bleu (itinéraire passsant uniquement par l'autoroute). Ainsi que d'autres indicateurs, comme la durée estimée, la distance, le prix totale, ou encore le prix moyen au kilomètre.  
2) Il apparaît parfois préférable, pour aller de A jusqu'en B, de quitter l'autoroute lors d'une sortie intermédiaire, puis de la réintégrer immédiatement après, afin de minimiser le coût du péage sur le trajet global entre A et B. Il seraît donc intéressant de chercher le tajet optimal minimisant le coût (sans pour autant augmenter la distance donc).  
Un diagramme en baton affichera le coût du trajet optimal en fonction de k le nombre de sorties maximum autorisées (c'est à dire en s'accordant le droit de sortir de l'autoroute, pour re-rentrer immédiatement après, k fois maximum).    
L'utilisateur aura également la possiblité de sélectionner sa contrainte k, et le programme adaptera l'itinéraire sur la carte en conséquence, affichant notamment les k sorties intermédiares.

Voici un exemple entre la sortie A = St-Jean-de-Védas, et B = Carcassane ouest, passant par l'A709, A9, A61 (nbSorties correspond à la contrainte k) :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/23a68b81a13c988690123226e56a5d861a5c6af1/Sphinx_DL/source/Projet/DONNEES/Capture/exemple_prog_graph.png" width="400" />

La contrainte k = 0 sorties autorisées correspond au cas du direct entre A et B. Au-delà de 5 sorties maximums autorisées, pour cet exemple, on ne peut plus optimiser le coût du trajet, et donc s'accorder d'avantage de sorties n'apporterait rien. C'est pourquoi le programme ne propose pas d'itinéraire comportant plus de 5 sorties.

# INSTALLATION

Tout d'abord lancer le terminal, et exécuter les commandes ci-dessous, afin d'installer les packages nécessaires au bon fonctionnement :

    $ pip install numpy pandas openrouteservice folium matplotlib ipywidgets
  
Télécharger le dossier github du projet sur votre ordinateur :

     $ git clone https://github.com/lucea97217/Projetgroupe6.git
     
**Il vous faudra ensuire créer une clé API personnelle** (moins de 1min). Si vous utilisez la clé d'une autre personne, cela la détruira.

--> Pour cela, suivre le lien https://openrouteservice.org/dev/#/signup, et les instructions suivantes :

1/ Tout d'abord vous devez créer un compte (on peut utiliser "sign up with github" pour aller plus vite) :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_6.PNG" width="500" />

2/ Ensuite connecter vous à celui-ci :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_7.PNG" width="400" />

3/ Dans l'onglet "TOKENS", puis dans la rubrique "Request a token", créer une nouvelle clé :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_8.PNG" width="800" />

4/ Votre clé apparaît sous la forme d'une chaîne de caractère, que vous pouvez copier-coller pour la suite.

<img src="https://github.com/lucea97217/Projetgroupe6/blob/fa225123ed9a8af8dd03ecb17132383c67a20507/Sphinx_DL/source/Projet/DONNEES/Capture/Capture_9.PNG" width="800" />

# UTILISATION

1) Ouvrir le dossier téléchargé du projet sur votre ordinateur.

2) Aller dans le sous-dossier "Données".

3) Ouvir le fichier python "progMap.py" dans un éditeur de code tel que VS-code. (L'éditeur est nécessaire pour la sortie graphique du programme, sinon, en ligne de commande sur la console, il ne s'affichera pas de graphique.)

4) Executer le code.

5) Coller votre clé API dans la zone dédiée sur l'interphace graphique qui s'affiche.

<img src="https://github.com/lucea97217/Projetgroupe6/blob/24dd9d1efe33aeca3e1a51407b0f73a8f50c9db2/Sphinx_DL/source/Projet/DONNEES/Capture/Capture10.PNG" width="400" />

Vous pouvez également la coller dans le code python, à l'emplacement indiqué ci-dessous :

<img src="https://github.com/lucea97217/Projetgroupe6/blob/24dd9d1efe33aeca3e1a51407b0f73a8f50c9db2/Sphinx_DL/source/Projet/DONNEES/Capture/Capture11.PNG" width="1400" />

6) Il ne vous reste plus qu'à sélectionner votre point de Départ et d'Arrivée, ainsi que la contrainte du nombre de sorties maximums autorisées (nbSorties). Sachant que la contrainte correspondante au trajet le moins cher (parmis tout les trajets possibles) est affichée sur une ligne de texte.

Exemple entre St-Jean-de-Védas et la frontière espagnole, avec l'itinéraire optimal comportant maximum 3 sorties. Pour ce parcours, le trajet optimal est atteint pour 5 sorties autorisées.

<img src="https://github.com/lucea97217/Projetgroupe6/blob/17a9c6585c64a6147508a32c18880b6cdbc5285b/Sphinx_DL/source/Projet/DONNEES/Capture/Capture12.PNG" width="500" />

