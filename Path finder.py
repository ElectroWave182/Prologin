N,matrice = int(input()),[]
for loop in range(N):
    matrice += list(map(int,str(input()).split()))
for cpt1 in range(1,N):
    for cpt2 in range(cpt1 + 1):
        if cpt2 == 0:
            matrice[cpt1] += matrice[cpt1 - 1]
        elif cpt2 == cpt1:
            matrice[N*cpt1] += matrice[N*(cpt1 - 1)]
        else:
            nbGauche = matrice[(N - 1)*cpt2 + cpt1 - 1]
            nbHaut = matrice[(N - 1)*cpt2 + cpt1 - N]
            if nbGauche > nbHaut:
                matrice[(N - 1)*cpt2 + cpt1] += nbGauche
            else:
                matrice[(N - 1)*cpt2 + cpt1] += nbHaut
for cpt1 in range(N,2*N - 1):
    for cpt2 in range(N*2 - cpt1 - 1):
        nbGauche = matrice[N*(cpt1 + cpt2 - N + 2) - cpt2 - 2]
        nbHaut = matrice[N*(cpt1 + cpt2 - N + 1) - cpt2 - 1]
        if nbGauche > nbHaut:
            matrice[N*(cpt1 + cpt2 - N + 2) - cpt2 - 1] += nbGauche
        else:
            matrice[N*(cpt1 + cpt2 - N + 2) - cpt2 - 1] += nbHaut
print(matrice[N*N - 1])