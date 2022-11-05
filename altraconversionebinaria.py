numeronaturale = int(input("Inserire il numero naturale: "))

while numeronaturale != 0:
    resto = (numeronaturale % 2)
    print(resto[::-1])
    numeronaturale = numeronaturale // 2
