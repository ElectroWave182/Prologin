from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def main():
    taille, msg = int(input()), list(map(int, input().split()))
    lettre = msg[0]
    if 64 < lettre < 81:
        for nb in msg[1:]:
            lettre += nb % 26
        lettre = (lettre - 65) % 26 + 65
        return chr(lettre)
    return " "
print(main())
