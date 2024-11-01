chiffreMax = int(input())
cpt1 = cpt2 = cpt3 = 0
while cpt1 <= chiffreMax or cpt2 < chiffreMax or cpt3 < chiffreMax:
    if cpt1 > chiffreMax:
        cpt1 = 0
        cpt2 += 1
        if cpt2 > chiffreMax:
            cpt2 = 0
            cpt3 += 1
    code = str(cpt3) + str(cpt2) + str(cpt1)
    if code != "000" and int(code) % 2 != 0 and int(code) % 5 != 0 and int(code) % 11 != 0 and (cpt1 + cpt2 + cpt3) % 2 != 0 and (cpt1*cpt2*cpt3) % 2 == 0:
        print(code)
    cpt1 += 1