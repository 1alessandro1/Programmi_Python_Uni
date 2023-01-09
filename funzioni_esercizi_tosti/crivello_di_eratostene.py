from math import sqrt
n = int(input("inserisci n: "))

interi = set()
multipli = set()


# crea l'insieme degli n da 2 a n

for i in range(2, n+1):
    interi.add(i)

# 

for j in range(2, round(sqrt(n)+1)):
    if j in interi:
        for i in interi:
            if i*j <=n:
                multipli.add(i*j)
            interi=interi.difference(multipli)

print("la lista dei primi", n, "numeri primi è", sorted(interi))