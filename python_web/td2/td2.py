import collections

Carte = collections.namedtuple ('Carte', ['rang', 'couleur'])

class JeuCartes :
    rangs = [str(n) for n in range(2, 11)] + list('VDRA')
    couleurs = ' pique coeur carreau trèfle'.split ()

    def __init__(self):
        self._cartes = [Carte(rang , couleur) for couleur in self.couleurs for rang in self.rangs]

    def __len__(self):
        return len(self._cartes)

    def __getitem__ (self, position) : 
        return self._cartes[position]

    
vp = Carte("V", "coeur")
print(vp)

jeu = JeuCartes()
print("taille du jeu : " + str(len(jeu)))

print(jeu[0])
print(jeu[-1])

#tirage au sort d'une carte
print("Carte aléatoire")
from random import choice
print(choice(jeu))

#tirage au sort de 3 cartes
from random import sample
rdm_cartes = sample(jeu._cartes, 3)
print(rdm_cartes)

#affichage des as 
print([carte for carte in jeu if carte.rang =='A'])

#le jeu est itérable 
for carte in jeu :
    print(carte)

#a l'envers
for carte in reversed(jeu) : 
    print(carte)

coul_val = dict(trèfle=0, carreau =1, coeur =2, pique =3)

def hauteur(carte) :
    val = JeuCartes.rangs.index(carte.rang)
    return val*len(coul_val)+coul_val[carte.couleur]

print("Ordre du Bridge")
for carte in sorted(jeu, key=hauteur):
    print(carte)

    