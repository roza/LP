#! /bin/bash

# Ce script prend en entrée un nombre quelconque d'arguments (au moins 1)
# et affiche un par un ses arguements en lettre majuscule 

if [ $# == 0 ]
    then
        cat $0 | grep "^# " 
        exit 1
        #affiche les lignes de ce fichier qui commence par "# " 
    else
        for argument 
            do 
                echo $argument | tr a-z A-Z
            done
fi