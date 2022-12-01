def cubo(x):
    return x ** 3

def media(lista):
    somma_elementi = sum(lista)
    numero_elementi = len(lista)
    media = somma_elementi / numero_elementi
    return media

l = []
for i in range(1000):
    l.append(cubo(i))

print(media(l))

# grave errore:
# def cubo(x):
#     print(x ** 3)
# il valore qui viene stampato ma non restituito

print(cubo(cubo(4)))

# fare una funzione che prende come parametro una stringa e vede se tale stringa è palindroma
# ateneta

# itopinonavevanonipoti