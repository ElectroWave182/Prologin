from sys import stdin,stdout
input,print = stdin.readline,stdout.write
def carburant(n,p):
    masses = [80 if p[num] > 90 else 60 for num in range(n)]
    return sum(masses)
print(str(carburant(int(input()),list(map(int,input().rstrip("\n").split())))))