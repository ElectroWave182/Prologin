from sys import stdin
input = stdin.readline


def main():

    # Initialisation des entrées (tableau), et des déplacements possibles
    global crep
    nblig, nbcol = map(int, input().split())
    crep = [list(input().rstrip("\n")) for _ in range(nblig)]
    autour = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # Fonction récursive qui détermine les points libres en se déplaçant (pas en diagonale)
    def scan(lig, col):
        for h, v in autour:
            x, y = col + v, lig + h
            if -1 < x < nbcol and -1 < y < nblig and crep[y][x] == ".":
                crep[y][x] = "l"
                scan(y, x)

    # Partir du premier point, (en haut à gauche) qui est toujours libre
    crep[0][0] = "l"
    scan(0, 0)

    # Compter les points restant (ceux inaccessibles)
    inac = 0
    for lig in crep:
        inac += lig.count(".")
    print(inac)


main()
