def palindrome (mot):
    i = 0
    j = len(mot) - 1
    while i < len(mot) / 2 :
        if mot[i] != mot[j]:
            return False
        else : 
            i = i + 1
            j = j - 1
    return True


#print(palindrome("bonjour"))
#print(palindrome("couuoc"))


def palindrome_boucle (mot) :
    for i in range(len(mot)) :
        if (mot[i] != mot[len(mot)-1-i]) : 
            return False
    return True

#print(palindrome_boucle("bonjour"))
#print(palindrome_boucle("couuoc"))


def affichePalindromes(txt,n):
    liste = txt.split()
    for mot in liste : 
        if len(mot) == n :
            if palindrome(mot) :
                print(mot)

#affichePalindromes("bonjour tout le monde couuoc c'est un rever abcba", 5) 
