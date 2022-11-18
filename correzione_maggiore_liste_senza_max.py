print("Inserisci una sequenza di interi terminante con 'FINE': ")
n = input("Input: ")

if n == "FINE":
    print("La sequenza è vuota")
else:
    minimo = int(n)
    while n != "FINE":
        if minimo > int(n):
            minimo = int(n)
        n = input("Input: ")
    print("Il minimo è", minimo)