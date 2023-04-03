from pycsp3 import *

n = 5  # taille du carré magique

X = VarArray(size=n, dom=range(1, n*n+1))

s = (n * (n * n + 1)) // 2  # somme de chaque ligne, colonne et diagonale principale

satisfy(
    AllDifferent(X),
    [s == Sum(X[i * n: (i + 1) * n]) for i in range(n)],  # chaque ligne a la somme s
    [s == Sum(X[i::n]) for i in range(n)],  # chaque colonne a la somme s
    [s == Sum(X[i * (n + 1)] for i in range(n))],  # diagonale principale a la somme s
    [s == Sum(X[i * (n - 1)] for i in range(1, n+1))],  # diagonale secondaire a la somme s
)

# affichage du carré magique
for i in range(n):
    for j in range(n):
        print(X[i * n + j].get_value(), end='\t')
    print()
