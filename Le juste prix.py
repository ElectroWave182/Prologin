from math import *
nbConcurrents = int(input())
total = cpt = 0
for loop in range(nbConcurrents):
    prix = int(input())
    total += prix
    cpt += 1
print(floor(total/cpt))