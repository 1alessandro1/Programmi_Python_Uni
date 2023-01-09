def salvaNuovoUtente(user, pwd):
    f = open ("utenti.txt", "a")
    f.write(user+":"+pwd+"\n")
    f.close()
username = input("Scegli il tuo username: ")
password = input("Scegli la tua password: ")

salvaNuovoUtente(username, password)


# authentication

def getUtentiRegistrati():
    inFile = open("utenti.txt", "r")
    utenti=()
    for line in inFile:
        line = line.strip("\n")
        lista = line.split(":")
        user = lista[0]
        pwd = lista[1]
        utenti[user] = pwd
    inFile.close()
    return utenti

def isRegistrato(user, pwd):
    utenti = getUtentiRegistrati()
    trovato = False
    for i in utenti:
        if i == user and utenti[i] == pwd:
            trovato = True
    return trovato