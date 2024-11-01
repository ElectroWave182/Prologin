nbAmisJours = input().split()
nbAmis = int(nbAmisJours[0])
Jours = int(nbAmisJours[1])
if nbAmis == 1:
    numJour = input()
    print(1)
else:
    numJour = sorted(list(map(int, input().strip().split())))
    minJour = numJour[0]
    maxJour = minJour + Jours
    nbAmisVus = 0
    if numJour[nbAmis - 1] < maxJour:
        print(nbAmis)
    else:
        for loop in range(numJour[nbAmis - 1] - maxJour + 1):
            cptAmis = 0
            cptAmisVus = 0
            for loop in range(nbAmis):
                if minJour <= numJour[cptAmis] <= maxJour:
                    cptAmisVus = cptAmisVus + 1
                cptAmis = cptAmis + 1
            if nbAmisVus < cptAmisVus:
                nbAmisVus = cptAmisVus
            minJour = minJour + 1
            maxJour = maxJour + 1
        print(nbAmisVus)