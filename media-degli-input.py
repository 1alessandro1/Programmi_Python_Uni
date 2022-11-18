lista = []


# creazione della lista

while True:
    ele = (input("Input: "))
    lista.append(ele) # adding the element
    if ele == "":
        (input("Input: "))
        lista = lista[:-1]
    if ele == "FINE":
        lista = lista[:-1]
        break
    
# somma degli elementi della lista

somma = sum(int(ele) for ele in lista)

if len(lista) != 0:
    media = somma / len(lista)
    print(media)
else:
    print("la lista è vuota")

