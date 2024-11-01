dPoele, nbPlaques, plaques, tempMax, verif = list(map(int, input().split())), int(input()), [], 0, True
for loop in range(nbPlaques):
    plaques += list(map(int, input().split()))
for cpt in range(nbPlaques):
    if plaques[cpt*3] - plaques[cpt*3 + 2] + 1 < dPoele[0] and plaques[cpt*3 + 1] - plaques[cpt*3 + 2] + 1 < dPoele[0]:
        for numPlaque in range(nbPlaques):
            if numPlaque != cpt and plaques[cpt*3] - plaques[cpt*3 + 2] < plaques[numPlaque*3] < plaques[cpt*3] + plaques[cpt*3 + 2] and plaques[cpt*3 + 1] - plaques[cpt*3 + 2] < plaques[numPlaque*3 + 1] < plaques[cpt*3 + 1] + plaques[cpt*3 + 2]:
                if abs(plaques[cpt*3] - plaques[numPlaque*3]) < abs(plaques[cpt*3 + 1] - plaques[numPlaque*3 + 1]):
                    if plaques[cpt*3 + 2] + plaques[numPlaque*3 + 2] - abs(plaques[cpt*3] - plaques[numPlaque*3]) > sommeTemp:
                        sommeTemp = plaques[cpt*3 + 2] + plaques[numPlaque*3 + 2] - abs(plaques[cpt*3] - plaques[numPlaque*3])
                        verif = False
                else:
                    if plaques[cpt*3 + 2] + plaques[numPlaque*3 + 2] - abs(plaques[cpt*3 + 1] - plaques[numPlaque*3 + 1]) > sommeTemp:
                        sommeTemp = plaques[cpt*3 + 2] + plaques[numPlaque*3 + 2] - abs(plaques[cpt*3 + 1] - plaques[numPlaque*3 + 1])
                        verif = False
        if verif:
            sommeTemp = plaques[cpt*3 + 2]
        if sommeTemp > tempMax:
            tempMax = sommeTemp
print(tempMax)