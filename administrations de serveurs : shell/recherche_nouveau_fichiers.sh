#! /bin/bash

# Ce script attend deux arguments : 
#  - un nom de repertoire rep
#  - un nombre de jours nbj
# et qui affiche tout les fichiers ayant été modifiés dans les nbj derniers jours et qui sont exzcutables

if [ $# == 2 ]
    then
        if [ -d $1 ]
            then
                find $1 -mtime -$2 -type f -executable > nouveaux.txt

                nb=`cat nouveaux.txt | wc -l`

                #pour afficher le nombre de fichiers dans un autre fichier
                echo il y a $nb nouveaux fichiers executables
                echo dans $1 depuis $2 jours
                echo leur liste est dans le fichier 'nouveaux.txt'
            else
                echo $1 n\'est pas un repertoire connu
                exit 1
        fi
    else 
        cat $0 | grep "^# "
        exit 1
fi