prezzo_con_iva = float(input("Inserire il costo lordo del prodotto: "))

numeratore_valore_iva = int(input("Inserire il valore dell'IVA: "))

if numeratore_valore_iva < 0 or numeratore_valore_iva > 99:
   print ("Il valore dell'IVA non è accettabile")
   quit()
   

valore_netto = (prezzo_con_iva)/(1 + numeratore_valore_iva / 100)

print (valore_netto)
