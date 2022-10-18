def PrendiPrezzoLordoGiusto():
    prezzo_con_iva = input("Inserisci il prezzo lordo: ")
    while True:
        try:
            prezzo_con_iva = float(prezzo_con_iva)
            break
        except:
            print("Valore non corretto, riprova")
            prezzo_con_iva = input("Re-inserisci il prezzo lordo: ")
    return float(prezzo_con_iva)

def PrendiValoreIVAGiusto():
    numeratore_valore_iva = input("Inserisci il valore del numeratore dell' IVA: ")
    while True:
        try:
            numeratore_valore_iva = float(numeratore_valore_iva)
            if numeratore_valore_iva > 0 and numeratore_valore_iva < 99:
                print("ok, il tuo valore è compreso nell'intervallo corretto")
                return numeratore_valore_iva 
            else:
                numeratore_valore_iva = float(input("Re-inserisci un valore compreso tra 0 e 99: "))
        except:
            numeratore_valore_iva = input("Attenzione, hai inserito un valore non numerico: ")


valore_netto = (PrendiPrezzoLordoGiusto())/(1 + PrendiValoreIVAGiusto() / 100)

print(valore_netto)
