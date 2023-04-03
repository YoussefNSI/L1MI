def carre_magique(n):
    carre_magique = [[0 for x in range(n)] for y in range(n)]
    i = n // 2
    j = n - 1
    num = 1
    while num <= n * n:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        if carre_magique[i][j]:
            j -= 2
            i += 1
            continue
        else:
            carre_magique[i][j] = num
            num += 1
        j += 1
        i -= 1
    return carre_magique


carre_magique = carre_magique(3)
for ligne in carre_magique:
    print(ligne)
