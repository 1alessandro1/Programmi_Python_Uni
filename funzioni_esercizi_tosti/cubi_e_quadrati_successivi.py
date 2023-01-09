# stampare i quadrati minori di 1000

import math 

lista_quadrati = []
lista_cubi = []


for i in range(round(math.sqrt(1000))):
    lista_quadrati.append(i**2)
for j in range(round(1000**(1/3))):
    lista_cubi.append(j**3)

# controllo se ci sono due elementi il cui predecessore è un quadrato e il successore è un cubo
# print(1000*(1/3))
# print(lista_cubi)
# print(lista_quadrati)


# for k in range(len(lista_cubi)):
#     for l in range(len(lista_cubi)):
#         if lista_cubi[k]-lista_quadrati[j] == 2:
#             print("ho trovato", k, l)

###########################################

X = set()
Y = set()

i = 1

while i**2<1000:
    X.add(i**2)
    i +=1

i = 1

while i**3<1000:
    Y.add(i**3)
    i += 1

for i in range(1000):
    if ((i-1) in X and (i+1) in Y):
        print(i)
