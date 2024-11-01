prixInitial = int(input())
nbBillets = int(input())
prixNouveaux = input().split()
a = 0
b = 0
for loop in range(nbBillets):
    nbPN = int(prixNouveaux[b])
    b = b + 1
    if nbPN < prixInitial:
        a = a + 1
if a < 3:
    print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")
else:
    print("ARNAQUE !")