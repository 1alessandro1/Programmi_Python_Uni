n=int(input("inserire il numero da convertire in base arbitraria: "))
base=int(input("inserisci la base: "))
alfabeto="0123456789ABCDEF"


c = n 

valore=""

if n > 1:
    while c >= 1:
        resto=c%basec
        c=c//base
        valore = alfabeto[resto] + valore
        # print(resto)

else:
    print(n)