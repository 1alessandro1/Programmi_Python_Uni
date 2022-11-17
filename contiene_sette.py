numero = input("inserire qualsiasi cagata: ")
cifra = input("inserisci quale cifra ne vuoi verificare la presenza: ")

contatore = 0

for i in range(len(numero)):
    if numero[i] == cifra:
        contatore += 1
#    print("ne ho trovato 1")

if contatore == 0:
    print("Putroppo non c'è nessun", cifra, "nel", numero)

print("ho trovato", contatore, "volte", cifra)


#### col count

b = numero.count(cifra)
print(b)


