from copy import deepcopy
from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def main():
    maxi, n, m = int(input()) + 1, int(input()), int(input())
    lab = [list(map(int, input().split())) for _ in range(n)]
    table, trace = [lab[0]], deepcopy(lab)
    table.extend([[maxi]*m for _ in range(n - 1)])
    # ça c'est les entrées et d'autres tableaux qui vont nous servir plus tard
    for ligne in range(1, n):
        for colon in range(m):
        # là on rentre dans le labyrinthe
            val = lab[ligne][colon]
            if 0 < colon: chemin = [val + table[ligne - 1][colon - 1]]
            else: chemin = [maxi]
            chemin.append(val + table[ligne - 1][colon])
            if colon < m - 1: chemin.append(val + table[ligne - 1][colon + 1])
            else: chemin.append(maxi)
            best = min(chemin)
            table[ligne][colon] = best
            # en gros, ça met le prix en âmes du meilleur des 3 chemins possibles dans le point d'arrivée
            trace[ligne][colon] = chemin.index(best) - 1
            # et ce truc là retient les meilleurs chemins pour après
    del trace[0]
    finish = min(table[-1])
    # une fois qu'on connaît le prix du meilleur chemin,
    if finish < maxi:
        sortie, cheminOP = "", table[-1].index(finish)
        trace.reverse()
        for ligne in trace:
            sortie = str(cheminOP) + " " + sortie
            cheminOP += ligne[cheminOP]
        # on va chercher le chemin lui-même
        return str(cheminOP) + " " + sortie.rstrip(" ")
    return "IMPOSSIBLE"
print(main())
