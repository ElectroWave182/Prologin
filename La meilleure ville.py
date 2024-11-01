from math import *
nmg = input().split()
n = int(nmg[0])
m = int(nmg[1])
g = int(nmg[2])
listen = ""
listem = ""
listeg = ""
for loop in range(n):
    tpsAtt = input()
    listen = listen + " " + str(tpsAtt)
for loop in range(m):
    abt1 = input()
    listem = listem + " " + str(abt1)
for loop in range(g):
    abt2 = input()
    listeg = listeg + " " + str(abt2)
listen = listen.split()
listemg = (listem + listeg).split()
cpt1 = 0
for loop in range(n):
    tpsXmin = ""
    total = 0
    div = 0
    cpt2 = 0
    for loop in range(m + g):
        if int(listemg[cpt2*3]) - 1 == cpt1:
            cpt3 = 0
            tpsX1 = 0
            for loop in range(m + g):
                if int(listemg[cpt2*3]) == int(listemg[cpt3*3]):
                    tpsX2 = int(listen[int(listemg[cpt3*3]) - 1]) + int(listemg[cpt3*3 + 2])
                    cpt5 = cpt3
                    verif = True
                    while tpsX2 < tpsX1 and verif and int(listemg[cpt5*3 + 1]) != int(listemg[cpt2*3 + 1]):
                        verif = False
                        cpt4 = 0
                        tpsX3 = 0
                        for loop in range(m + g):
                            if int(listemg[cpt5*3 + 1]) == int(listemg[cpt4*3]):
                                verif = True
                                if int(listemg[cpt5*3]) > m:
                                    tpsX4 = int(listen[int(listemg[cpt4*3]) - 1]) + int(listemg[cpt4*3 + 2])
                                    if tpsX3 > tpsX4 or tpsX3 == 0:
                                        tpsX3 = tpsX4
                                else:
                                    tpsX4 = int(listemg[cpt4*3 + 2])
                                    if tpsX3 > tpsX4 or tpsX3 == 0:
                                        tpsX3 = tpsX4
                                cpt5 = cpt4
                            cpt4 = cpt4 + 1
                        tpsX2 = tpsX2 + tpsX3
                    if (tpsX1 > tpsX2 or tpsX1 == 0) and int(listemg[cpt5*3 + 1]) == int(listemg[cpt2*3 + 1]):
                        tpsX1 = tpsX2
                cpt3 = cpt3 + 1
            total = total + tpsX1
            div = div + 1
        cpt2 = cpt2 + 1
    if div == 0:
        score = -1
    else:
        score = floor(total/div)
    cpt1 = cpt1 + 1
    print(score)