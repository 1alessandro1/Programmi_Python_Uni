# per spese fino a 50 sconta 10 
# per spese da 51 a 100 sconto 20
# per spese superiori a 100 sconto 30

spesa = float(abs(input("Inserisci quanto hai speso: ")))

if 0 <= spesa <= 50:
    prezzoscontato = print("Il costo del prodotto scontato è: ", spesa - spesa * 0.1)
    print(prezzoscontato)
elif 51 <= spesa <= 100:
    prezzoscontato = print("Il costo del prodotto scontato è: ", spesa - spesa * 0.2)
    print(prezzoscontato)
elif spesa > 100:
    prezzoscontato = print("Il costo del prodotto scontato è: ", spesa - spesa * 0.3)
    print(prezzoscontato)
