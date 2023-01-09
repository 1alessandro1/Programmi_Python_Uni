# Dato file con righe formate da nomi ed età creare un dizionario che abbiacome chiavi le età e come valori i nomi di chi ha quell'età
ilmiofile = open("nomiedeta.txt", "r")

from collections import defaultdict
  
dizionario = defaultdict(list)
# Details["Country"].append("India")
# Details["Country"].append("Pakistan")
# print(Details)

# dizionario = {}

for line in ilmiofile:
    key, lista = line.split()
    dizionario[key].append(lista)

print(dizionario)

# lista = ilmiofile.read().strip("\n").split()
# 
# print(lista)
# 
# diz = {}

# for i in range(len(lista)):
#     for eta in lista:
#         if i % 2 != 0:
#             diz[i] = eta
#     for nome in lista:
#         if i % 2 == 0:    
#             diz[nome] = diz[i]
#         
#             del [old_key]    
        

