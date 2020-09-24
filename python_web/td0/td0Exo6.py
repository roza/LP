def decompte(L) : 
    dico = {}
    for mot in L : 
        if mot in dico : 
            dico[mot] = dico[mot]+1
        else : 
             dico[mot] = 1
    return dico

print(decompte([ "blanc","bleu","blanc","noir","bleu","bleu","rouge",
"rouge" ]))


def coupe(mot, n) : 
    res = ""
    for i in range(n) : 
        res += mot[i]
    return res + "."

def abrege(L,N) :
    dico = {}
    for mot in L :
        dico[mot] = coupe(mot, N)
    return dico

print(abrege(["maison","immeuble","parking","hopital", "rue"] , 3))