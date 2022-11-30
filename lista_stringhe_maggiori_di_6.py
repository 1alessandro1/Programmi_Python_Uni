# 
lista = ["informatica", "casa", "gioco", "spazio"]

i = 0
while i < len(lista):
    print(lista[i], "i=", i)
    if len (lista[i]) > 6:
        lista.pop(i)
    else:
        i += 1
    print(lista)
print(lista)