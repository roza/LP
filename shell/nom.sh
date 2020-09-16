#nom du shell (à lancer avec : source nom.sh) avec BASH
echo "nom du shell : " $0

#nombre d'arguments
echo "nombre d'arguments" $#

echo $? #vaut 0 si réussite de la derniere commande et autre chose si echec de la derniere commande 