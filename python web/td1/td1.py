def somme_depenses(liste):
    """
    Cette fonction prend en entrée un tableau de couples
    (nom, montant) et renvoie le total cumulé des dépenses
    >>>somme_depenses([('joe',23),('ophelie',17),('ophelie',12),('paul',5)]) 
    57
    """
    total = 0
    for personne, depense in liste:
        total += depense
    return total

def somme_personne(liste, nom):
    """
    Cette fonction prend en entrée un tableau de couples
    (nom, montant) et un nom et renvoie le total cumulé des dépenses de la personne qui s'apelle nom
    >>>somme_personne([('joe',23),('ophelie',17),('ophelie',12),('paul',5)], "ophelie") 
    29
    """
    total = 0
    for personne, depense in liste:
        if personne == nom :
            total += depense
    return total

def somme_par_personne (liste) : 
    """
    Cette fonction prend en entrée un tableau de couples
    (nom, montant) et renvoie le total cumulé des dépenses de chaque personne (sous forme d'un dictionnaire)
    >>>somme_par_personne([('joe',23),('ophelie',17),('ophelie',12),('paul',5)]) 
    {'joe' : 23, 'ophelie' : 29, 'paul' : 5}
    """
    res = {}
    for personne, depense in liste : 
        if personne not in res : 
            res[personne] = depense
        else : 
            res[personne] = res[personne] + depense
    return res

def avoir_par_personne (liste) : 
    """
    Cette fonction prend en entrée un tableau de couples
    (nom, montant) et renvoie pour chaque personne la somme qu'elle doit touché ou percevoir pour que les depenses soient équilibrées 
    >>>avoir_par_personne([('joe',23),('ophelie',17),('ophelie',12),('paul',5)]) 
    {'joe' : -4, 'ophelie' : -10, 'paul' : 14}
    """
    if liste == [] : 
        return {}
    else : 
        spp = somme_par_personne(liste)
        moyenne = 0
        for nom, depense in spp.items() : 
            moyenne = moyenne + depense
        moyenne = moyenne / len(spp)
        for nom, depense in spp.items() : 
            spp[nom] = moyenne - depense
    return spp

avoir_par_personne([('joe',23),('ophelie',17),('ophelie',12),('paul',5)])

