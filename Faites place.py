from math import *
taille, nbMarchands, listePos = int(input()), int(input()), list(map(int, str(input()).split()))
for cpt in range(nbMarchands):
    pos = listePos[cpt]
    if cpt == 0:
        zoneMax = pos - 0.5
    elif (pos - prepos)/2 > zoneMax:
        zoneMax = (pos - prepos)/2
    prepos = pos
zone = taille - pos - 0.5
if zone > zoneMax:
    zoneMax = zone
print(floor(zoneMax))