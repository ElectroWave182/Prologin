from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def pgcd(a, b):
    resteA, resteB = max([a, b]), min([a, b])
    while resteB != 0:
        resteC = resteA % resteB
        resteA, resteB = resteB, resteC
    return resteA


def pythie(nbChem):
    somme = 0
    for i in range(1, nbChem + 1):
        for j in range(1, nbChem + 1):
            somme += i * j // pgcd(i, j)
    return somme


def chemins(n):
    laby = [[0] * n for _ in range(n - 1)]
    laby.insert(0, [1] * n)
    for lig in range(1, n):
        for col in range(lig, n):
            laby[lig][col] = laby[lig - 1][col] + laby[lig][col - 1]
    return laby[n - 1][n - 1]


nbChem = chemins(int(input()))
print(str(nbChem) + "\n")
print(str(pythie(nbChem)))
for t in range(20):
    print("\n" + str(pythie(t)))
