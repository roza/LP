from math import hypot

class Vecteur :

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __len__ (self):
        return 2

    def __repr__(self):
        return 'Vecteur(%r, %r)'%(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vecteur(x,y)

    def __mul__(self, other):
        return self.x * other.x  +  self.y * other.y

    def __rmul__(self, scalaire):
        return Vecteur(self.x * scalaire, self.y * scalaire)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

v1 = Vecteur(4,5)
print(v1)
print(len(v1))

v2 = Vecteur(-3,7)
v3 = v1 + v2
print(v3)
v4 = v1 * v2
print(v4)
v5 = 3*v1
print(v5)

print(abs(v1))
v6 = Vecteur(0,0)
if v6 :
    print("v6 non null")
else : 
    print("v6 null")