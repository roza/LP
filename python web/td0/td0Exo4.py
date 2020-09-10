x = [a for a in [1, 2, 3]]
print(x)
x = [a for a in x if a == 2]
print(x)
x = [a for a in range(0, 21) if a % 2 == 0]
print(x)
x = [a * 2 for a in range(0, 11)]
print(x)

def impair (n) :
    return n % 2 != 0

print(impair(5))
print(impair(2))

def impairs_plus_petit_n (n) :
    liste = [x for x in range(n) if x % 2 != 0]
    print(liste)

impairs_plus_petit_n (8)