# data una lista di numeri trovare se un numero ha una certa proprietà a scelta

limite = int(input("Inserire il numero di elementi da sommare: "))

for i in range(limite):
    a = (input("Input: "))
    if float(a) % 2 == 0:
        print(a,"questo numero è pari")
    else:
        print(a,"questo è dispari")


#controllo = (int(i) for i in lst[:-1])




