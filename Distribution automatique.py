nbAppareils, matrice, chemin, prix = int(input()), "", "", ""
for cpt1 in range(nbAppareils):
    lMatrice = str(input())
    matrice += " " + lMatrice
    lMatrice = list(map(int, lMatrice.split()))
    sMatrice = sorted(lMatrice)
    for cpt2 in range(1, nbAppareils - 1):
        for cpt3 in range(nbAppareils):
            if sMatrice[cpt2] == lMatrice[cpt3]:
                break
        if cpt1 <= cpt3:
            chemin += " " + str(cpt3)
            break
        elif cpt1 != list(map(int, chemin.split()))[cpt3]:
            chemin += " " + str(cpt3)
            break
        else:
            for cpt4 in range(nbAppareils):
                liste = list(map(int, matrice.split()))
                if sorted(liste[cpt3*nbAppareils : (cpt3 + 1)*nbAppareils - 1])[cpt2] == liste[cpt3*nbAppareils + cpt4]:
                    break
            if cpt1 <= cpt4:
                chemin += " " + str(cpt4)
                break
            elif cpt3 != list(map(int, chemin.split()))[cpt4]:
                chemin += " " + str(cpt4)
                break
for cpt1 in range(nbAppareils):
    prix += " " + str(list(map(int, matrice.split()))[list(map(int, chemin.split()))[cpt1] + nbAppareils*cpt1])
total = 0
for cpt1 in range(nbAppareils):
    if nbAppareils != cpt1 + 2:
        total += sorted(list(map(int, prix.split())))[cpt1]
print(total)