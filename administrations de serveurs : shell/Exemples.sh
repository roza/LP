#trouver tout les fichiers .sh du dossier courant
find ./ -type f -name "*.sh"

#afficher les fichiers dans le repertoire courant qui ont ete modifies dans les 3 derniers jours
find ./ -mtime -3 -type f -print

#afficher les fichiers dans le repertoire courant qui ont ete modifies dans les 3 derniers jours etqui sont executable
find ./ -mtime -3 -type f -executable
