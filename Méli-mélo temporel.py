nbPays = int(input())
liste = "0"
for loop in range(nbPays):
    numPaysIHeures = str(input())
    liste = liste + " " + numPaysIHeures
nbVoyages = int(input())
liste = liste.split()
Haruhi = 0
Joseph = 0
for loop in range(nbVoyages):
    HouJnumPaysF = input().split()
    HouJ = int(HouJnumPaysF[0])
    numPaysF = int(HouJnumPaysF[1])
    if HouJ == 1:
        Haruhi = int(liste[numPaysF*2])
    else:
        Joseph = int(liste[numPaysF*2])
    decalage = Haruhi - Joseph
    if decalage < 0:
        print(-decalage)
    else:
        print(decalage)