import secrets

# si genera un numero randomico di biglie
secure_number = secrets.SystemRandom()

# si genera un numero randomico tra 0 e 1 per sapere chi gioca
verificachigioca = secure_number.randrange(0,2)

# se verificachigioca è uguale a 1 tocca al PC, se è 0 tocca all'umano

# si genera un numero randomico di biglie
numero_biglie = secure_number.randrange(10, 100)

print(numero_biglie, verificachigioca)

# numero_biglie = numero_biglie

while numero_biglie  != 1:
    print("Il numero corrente di biglie è", numero_biglie)
    if verificachigioca == 0:
        biglie_umano = int(input("Inserisci il numero di biglie che vuoi sottrarre: "))
        while biglie_umano not in range(1,int(numero_biglie/2 + 1)):
            print("Ritenta con un numero di biglie corretto: ")
            biglie_umano = int(input("Inserisci il numero di biglie che vuoi sottrarre: "))
        numero_biglie = numero_biglie - biglie_umano
    else:
        numerocasualedibiglie_calcolatore = secure_number.randrange(1,int(numero_biglie/2 + 1))
        numero_biglie = numero_biglie - numerocasualedibiglie_calcolatore
        print("Ho tolto", numerocasualedibiglie_calcolatore, "biglie")
    verificachigioca = 1 - verificachigioca
if verificachigioca == 0:
    print("Hai perso")
else:
    print("Hai vinto")