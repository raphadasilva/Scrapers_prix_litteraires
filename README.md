# Scrapers les lauréats des principaux prix litteraires

Récemment, Le Temps a publié un article [sur les lauréats des principaux prix littéraires en France](https://www.letemps.ch/culture/2016/11/02/goncourt-renaudot-femina-medicis-profil-dun-laureat-prix-litteraire).

Comme aucune base de données rassemblant ces quelques centaines d'écrivains n'existaient jusqu'alors, il a fallu la créer à partir de Wikipedia. Le script suivant montre la marche à suivre avec un petit truc en plus : le calcul de l'âge de l'écrivain à partir de la première date rencontrée sur sa page Wikipedia perso.

Certes, il y a eu une quinzaine d'erreurs ou de cas particuliers dans la manip', mais ça reste bien faiblard sur plus de 370 individus !
