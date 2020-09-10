
l = list()
liste = []
l.append(0)
l.append(3)
l.append(1)
l.append(3)
l.append(2)

liste.append(0)
liste.append(1)
liste.append(2)
liste.append(3)
print(l)
print(liste)
liste = l + liste 
print(liste)
liste.sort()
print(liste)
print(len(liste))
print(liste.count(3))
print(liste)
liste.remove(0)
print(liste)
liste[5] = 5
print(liste)