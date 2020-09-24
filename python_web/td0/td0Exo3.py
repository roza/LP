def appartient (liste, eleme) : 
    for elem in liste :
        if elem == eleme :
            return True
    return False

liste = [1,2,3,4,5,6,7,8,9]

print(appartient(liste, 5))
print(appartient(liste, 12))


def indice_premier_occ (liste, eleme) : 
    for i in range(len(liste)) :
        if liste[i] == eleme :
            return i
    return None

print(indice_premier_occ(liste, 5))
print(indice_premier_occ(liste, 12))