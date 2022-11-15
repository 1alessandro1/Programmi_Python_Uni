numero_da_verificare = input("Inserisci un numero reale: ")
while True:
    try:
        numero_da_verificare = float(numero_da_verificare)
        print ("Bene, il valore che hai inserito è un numero reale :)")
        print(numero_da_verificare)
        break
    except:
        print("Il valore non è un numero reale...")
        numero_da_verificare = input("Re-inserisci un numero reale: ")
