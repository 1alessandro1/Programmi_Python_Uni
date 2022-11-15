# data una lista di numeri trovare se un numero ha una certa proprietà a scelta

lst = []

limite = int(input("Inserire il numero di elementi da sommare:"))

for i in range(limite):
    ele = (input("Input: "))
    lst.append(ele) # adding the element
 
for i in lst:
    if float(i) % 2 == 0:
        print(i,"questo numero è pari")
    else:
        print(i,"questo è dispari")


#controllo = (int(i) for i in lst[:-1])




