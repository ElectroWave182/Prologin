from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def main():
    nbFam, taFam = int(input()), int(input())
    table = [list(input()) for _ in range(nbFam)]
    nbCar, cartes = int(input()), list(input())
    tableZ = []
    for famil in table:
        familZ = []
        for membre in famil:
            if not membre in cartes: familZ.append(membre)
        tableZ.append(familZ)
    return str(min([len(familZ) for familZ in tableZ]))
print(main())
