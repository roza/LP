def tri (a, b, c) : 
    liste = [a,b,c]
    liste.sort()
    return (liste[0], liste[1], liste[2])


print(tri(1,3,2))