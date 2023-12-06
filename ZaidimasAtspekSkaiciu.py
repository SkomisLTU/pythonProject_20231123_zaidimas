# This is a sample Python script.

'''
Parašyti programą, kuri:

Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
Metų
Mėnesių
Dienų
Valandų
Minučių
Sekundžių

'''

import random
laimeta = False
limit_v = 0  # virsutinis limitas
limit_a = 0  # apatinis limitas
gyvybes = "\u2665 \u2665 \u2665 \u2665 \u2665" # sirdeles
##### ivedimas


while 1:
    data1 = input("Įveskite spejamu skaiciu diapazona (x y) : ")
    try:
        data2 = data1.split(" ")
        limit_a = int(data2[0])
        limit_v = int(data2[1])
        if limit_a < limit_v:
            break
        else:
            print("blogai  ivestas diapazonas")
    except:
        print("blogai ivestas diapazonas")

 # spejamas skaicius
skaicius = random.randint(limit_a, limit_v)
print("Liko bandymu: ", gyvybes)
#### spejimai
for x in range(gyvybes.count("\u2665"), 0, -1):
    try:
        spejimas = int(input("Spekite skaiciu: "))
    except:
        print("ivedete ne skaiciu ir praradote gyvybe :( ")
        gyvybes = gyvybes[::-1].replace("\u2665", "_", 1)
        print("Liko bandymu: ", gyvybes)

    if spejimas < skaicius:
        if spejimas < limit_a:
            print("Spejai skaiciu uz ribu :O")
            gyvybes = gyvybes[::-1].replace("\u2665", "_", 1)
            print("Liko bandymu: ", gyvybes)
            print("Like variantai nuo ", limit_a, " iki ", limit_v)
        else:
            print("Nepataikiai, didesnis :P")
            limit_a = spejimas + 1
            gyvybes = gyvybes[::-1].replace("\u2665", "_", 1)
            print("Liko bandymu: ", gyvybes)
            print("Like variantai nuo ", limit_a, " iki ", limit_v)
    elif spejimas > skaicius:
        if spejimas > limit_v:
            print("Spejai skaiciu uz ribu :O")
            gyvybes = gyvybes[::-1].replace("\u2665", "_", 1)
            print("Liko bandymu: ", gyvybes)
            print("Like variantai nuo ", limit_a, " iki ", limit_v)
        else:
            print("Nepataikiai, mazesnis :P")
            limit_v = spejimas - 1
            gyvybes = gyvybes[::-1].replace("\u2665", "_", 1)
            print("Liko bandymu: ", gyvybes)
            print("Like variantai nuo ", limit_a, " iki ", limit_v)
    elif spejimas == skaicius:
        laimeta = True
        print("L A I M E J O T E")
        break
    else:
        print("KALIDA")

if laimeta == False:

    print("Pralaimejot", gyvybes)



