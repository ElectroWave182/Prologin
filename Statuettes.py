try: import psyco; psyco.full()
except: pass
nm = input().split()
n = int(nm[0])
m = int(nm[1])
amis = list(map(int,input().split()))
statuettes = list(map(int,input().split()))
if n > m:
    print(0)
else:
    statuettesRangees = sorted(statuettes)
    nbCadeaux = 0
    posCadeaux = ""
    cpt1 = 0
    for loop in range(m - n + 1):
        posValides = 1
        cptPosNbMin = 0
        for loop in range(m):
            if statuettesRangees[cpt1] == statuettes[cptPosNbMin]:
                debutPos = cptPosNbMin + 1 - amis[0]
            cptPosNbMin = cptPosNbMin + 1
        if 0 <= debutPos <= m - n:
            statuettesX = ""
            cpt2 = 0
            for loop in range(m):
                if debutPos <= cpt2 <= debutPos + n - 1:
                    statuettesX = statuettesX + " " + str(statuettes[cpt2])
                cpt2 = cpt2 + 1
            statuettesX = list(map(int,statuettesX.split()))
            cpt2 = 0
            for loop in range(n - 1):
                if statuettesX[amis[cpt2] - 1] < statuettesX[amis[cpt2 + 1] - 1]:
                    posValides = posValides + 1
                cpt2 = cpt2 + 1
            if posValides == n:
                nbCadeaux = nbCadeaux + 1
                posCadeaux = posCadeaux + " " + str(debutPos + 1)
        cpt1 = cpt1 + 1
    print(nbCadeaux)
    if nbCadeaux != 0:
        posCadeaux = sorted(list(map(int,posCadeaux.split())))
        posCadeauxCr = str(posCadeaux[0])
        cptPosCadeaux = 1
        for loop in range(nbCadeaux - 1):
            posCadeauxCr = posCadeauxCr + " " + str(posCadeaux[cptPosCadeaux])
            cptPosCadeaux = cptPosCadeaux + 1
        print(posCadeauxCr)