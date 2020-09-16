#! /bin/bash

#Ce script attend 2 paramètres : 
# - nom de repertoire : rep
# - nombre de jours : n (entier)
#Il affiche la liste des fichiers qui ont été modifiés dans les n  derniers jours

#find www -type f -mtime -2  #liste les fichiers du repertoire www modifies dans les 2 derniers jours

#ce qu'on veut 
if [ $# != 2 ]
then cat $0 | grep "^# "
exit 1
else echo "args ok"
fi
find $1 -type f -mtime -$2