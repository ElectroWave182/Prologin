nbInter, dfc, listeC, listePos = int(input()), [], "", ""
for loop in range(nbInter):
    dfc += list(map(int, str(input()).split()))
for cpt1 in range(0, nbInter*3, 3):
    for cpt2 in range(0, nbInter*3, 3):
        if cpt1 != cpt2 and (dfc[cpt1] >= dfc[cpt2 + 1] or dfc[cpt2] >= dfc[cpt1 + 1]):
            listeC += " " + str(dfc[cpt1 + 2] + dfc[cpt2 + 2])
if listeC == "":
    print(-1)
else:
    print(sorted(list(map(int, listeC.split())))[0])