#x : affiche [1,2,3]

#y : affiche [2]

#z : affiche [0,2,4,...,18,20]

#t : affiche [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def impair(x):
    return x%2 == 1

print ([i for i in range(100) if impair(i)])