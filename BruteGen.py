import msvcrt

gen = 0

def generar(dic,cnt,pref):
    global gen
    if msvcrt.kbhit():
        char = msvcrt.getwch()
        if (char == '\x1b'):
            raise ValueError("Se ha parado la generación.")
    if cnt == 0:
        f.write(pref+"\n")
        gen += 1
        if (gen == int(lines*0.1)):
            print("10%")
            print()
        elif (gen == int(lines*0.2)):
            print("20%")
            print()
        elif (gen == int(lines*0.3)):
            print("30%")
            print()
        if (gen == int(lines*0.4)):
            print("40%")
            print()
        elif (gen == int(lines*0.5)):
            print("50%")
            print()
        elif (gen == int(lines*0.6)):
            print("60%")
            print()
        if (gen == int(lines*0.7)):
            print("70%")
            print()
        elif (gen == int(lines*0.8)):
            print("80%")
            print()
        elif (gen == int(lines*0.9)):
            print("90%")
            print()
    else:
        for char in dic:
            generar(dic, cnt-1, pref+char)

def elevar(b,e):
    res = b
    for i in range(0,e-1):
        res *= b
    return res

f = open("pswds.txt", "w")



mini = int(input("Número mínimo de caracteres: "))
maxi = int(input("Número máximo de caracteres: "))
chars = input("Caracteres a usar: ")
dic = []

for c in chars:
    if not (c in dic):
        dic.append(c)
dic.sort()

lines = dskSpc = 0

for i in range(mini,maxi+1):
    lines += elevar(len(dic), i)
    dskSpc += ((lines * (i+2))-3) * 0.0000009488103185

dskSpc = str(dskSpc)

go = input("Se van a generar " + str(lines) + " combinaciones que ocuparán " + dskSpc[:dskSpc.find(".")+3] + "MB. ¿Quieres continuar? (S/N) ")

while (go != 's' and go != 'S' and go != 'n' and go != 'N'):
    go = input("Esa no es una opción válida, vuelve a introducir: ")

if (go == 's' or go == 'S'):
    print("En caso de querer parar la ejecución pulsa la tecla ESC.")
    try:
        for i in range(mini,maxi+1):
            generar(dic,i,"")
        print("Se han generado todas las combinaciones.")
    except ValueError as e:
        print(e)
        f.close()

f.close()
if (go == 'n' or go == 'N'):
    print("Fin del programa.")