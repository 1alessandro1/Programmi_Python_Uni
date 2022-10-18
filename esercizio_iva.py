import sys
prezzo_con_iva = float(input("Inserire il costo lordo del prodotto: "))

while not numeratore_con_iva.isnumeric():
  print ("Devi inserire un valore numerico!")
  
  
numeratore_valore_iva = int(input("Inserire il valore dell'IVA: "))

while numeratore_valore_iva < 0 or numeratore_valore_iva > 99:
  print ("il valore dell'iva non è accettabile")
  numeratore_valore_iva = int(input("Inserire il valore dell'IVA: "))


valore_netto = (prezzo_con_iva)/(1 + numeratore_valore_iva / 100)

print (valore_netto)
