lista = [1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#lista = [1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1]
print(len(lista))

count_zeri = 0  
count_uni = 0
listazeri=[]
listauni=[]
lista.append("pippo") # per evitare errori alla fine

for i in range(len(lista)):
    if lista[i] == lista[i-1] == 0:
        count_zeri += 1
    elif lista[i] != lista[i-1]:
        listazeri.append(count_zeri+1) # aggiorno la lista
        count_zeri = 0
print(max(listazeri))
#print("la lista degli zeri è", (listazeri))

for j in range(len(lista)):
    if lista[j] == lista[j-1] == 1:
        count_uni += 1
    elif lista[j] != lista[j-1]:
        listauni.append(count_uni+1) # aggiorno la lista
        count_uni = 0
print(max(listauni))
# print("la lista degli uni è", (listauni))






# pseudocodice
# controlla dall'inizio ogni elemento della lista
# appena ne vedi due uguali incrementa il contatore di n volte quante sono quelli uguali
# printare 
