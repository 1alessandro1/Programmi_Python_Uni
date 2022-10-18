def PrendiPrezzoLordoGiusto():
    prezzo_con_iva = input("Inserisci il prezzo lordo: ")
    while True:
        try:
            prezzo_con_iva = float(prezzo_con_iva)
            print ("Bene, il valore del prezzo lordo che hai inserito è un numero decimale accettabile...")
            break
        except:
            print("Il valore inserito non è composto da soli numeri decimali, riprova...")
            prezzo_con_iva = input("Re-inserisci il prezzo lordo: ")
    return float(prezzo_con_iva)

def PrendiValoreIVAGiusto():
    numeratore_valore_iva = input("Inserisci il valore del numeratore dell'IVA: ")
    while True:
        try:
            numeratore_valore_iva = float(numeratore_valore_iva)
            if numeratore_valore_iva >= 0 and numeratore_valore_iva <= 100:
                print("Ok, il valore dell'IVA inserito è compreso nell'intervallo corretto...")

                return numeratore_valore_iva 
            else:
                numeratore_valore_iva = float(input("Reinserisci un valore compreso tra 0 e 100: "))
        except:
            numeratore_valore_iva = input("Attenzione, hai inserito un valore che contiene valori non decimali, riprova: ")


valore_netto = (PrendiPrezzoLordoGiusto())/(1 + PrendiValoreIVAGiusto() / 100)

print(valore_netto)
