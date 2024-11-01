taille, pos1, pos2, = int(input()), int(input()), int(input())
milieu = taille/2
if milieu - pos1 < pos2 - milieu:
    print(1)
elif milieu - pos1 > pos2 - milieu:
    print(2)
else:
    print(0)