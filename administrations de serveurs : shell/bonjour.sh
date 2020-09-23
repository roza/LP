#! /bin/bash

echo Bonjour depuis $0

#Pour lancer le script : 
# - source script.sh équivalent à . script.sh
# Avec ces commandes on reste dans le shell courant
# - bash script.sh équivalent à ./script.sh
# Avec ces commandes un processus fils est crée

echo premier argument : $1
echo deuxieme argument : $2
echo troisieme argument : $3

echo le nombre d\'arguments est : $#

echo la liste d\'arguments est : $*

for argument 
#ou for argument in $*
    do
        echo $argument
    done