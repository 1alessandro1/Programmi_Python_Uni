# Rimario

a = open("dizionario.txt", "r")

rimario = a.read()[::-1].split()

rimario.sort()

# print(rimario)


def Rime(parola, ind):
    insieme = list()
    for j in range(ind, len(rimario)):
        print(rimario[j], j, len(rimario))
        if rimario[j] != parola: # controllo per le parole di lunghezza 1
            if parola[0] == rimario[j][0] and parola[1] == rimario[j][1]:
                insieme.append(rimario[j][::-1])
            else:
                print("pippo")
                return insieme
    return insieme

diz = {}
for i in range(len(rimario)):
    if len(rimario[i]) > 2: # controllo per le parole di lunghezza 1
        print("!!",rimario[i])
        diz[rimario[i][::-1]] = Rime(rimario[i], i)
        
for el in diz:
    print(el, diz[el])