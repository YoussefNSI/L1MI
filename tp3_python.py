def generate_magic_square(n):
    magic_square = [[0 for x in range(n)] for y in range(n)]
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
        if magic_square[i][j]:
            j -= 2
            i += 1
            continue
        else:
            magic_square[i][j] = num
            num += 1
        j += 1
        i -= 1
    return magic_square

# Example usage
magic_square = generate_magic_square(5)
for row in magic_square:
    print(row)
