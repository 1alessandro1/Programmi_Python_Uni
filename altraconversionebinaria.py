# conversione binaria del prof

numeronaturale = int(input("Inserire il numero naturale: "))


a = bin(numeronaturale)
print(a)

while numeronaturale != 0:
    resto = (numeronaturale % 2)
    print(resto)
    numeronaturale = numeronaturale // 2