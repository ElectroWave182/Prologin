from itertools import combinations
from copy import deepcopy

def connexe():
    chemins = [lien for lien in liens if start == min(lien)]
    while chemins != []:
        for chemin in chemins:
            if max(chemin) == end: return True
            chemins.extend([lien for lien in liens if chemin[1] == lien[0]])
            chemins.remove(chemin)
    return False

def main():
    global villes, aques, liens, start, end
    useless, aques = int(input()), int(input())
    tous = [list(input().split()) for _ in range(aques)]
    rome, tivoli = input(), input()
    start, end = min(rome, tivoli), max(rome, tivoli)

    for nbAq in range(aques, 0, -1):
        for comb in list(combinations(tous, nbAq)):
            liens = comb
            if not connexe():
                yield str(aques - nbAq)
                for lien in tous:
                    if not lien in comb: yield " ".join(lien)
                return
    print(str(aques) + "\n" + "\n".join(map(" ".join, tous)))

print("\n".join(list(main())))
