stock = list(map(int, input().strip().split()))
suc, sal, nbClients = stock[0], stock[1], int(input())
sClients = ind = 0
for loop in range(nbClients):
    souhait = int(input())
    if souhait == 0 and suc > 0:
        suc -= 1
        sClients += 1
    elif souhait == 1 and sal > 0:
        sal -= 1
        sClients += 1
    elif souhait == 2:
        ind += 1
stock = suc + sal
if stock > ind:
    sClients += ind
elif stock <= ind:
    sClients += stock
print(nbClients - sClients)