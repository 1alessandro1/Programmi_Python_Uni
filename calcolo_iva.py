# import sys

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


# while numeratore_valore_iva < 0 or numeratore_valore_iva > 99:
#    print ("Il valore dell'iva non è accettabile")
#    numeratore_valore_iva = int(input("Re-nserire il valore dell'IVA: "))
#  
# valore_netto = (prezzo_con_iva)/(1 + numeratore_valore_iva / 100)
#  
# print (valore_netto)






# Questo qui sotto (1) non va bene per il fatto che prima devi definire la variabile "prezzo_con_iva" in
# cui se scrivi solamente input("inserisci bla bla") lo prenderà sempre come una stringa e non ci 
# si possono fare delle operazioni algebriche. Saresti costretto ad utilizzare int(input()) o float(input())
# ma non ti permettono di effettuare dei controlli senza che il programma crashi lamentandosi del fatto
# che l'input non gli piaccia



# Es. (1) 
# while not prezzo_con_iva.isnumeric():
#    print("il valore del prezzo con IVA non è accettabile")
# 
# prezzo_con_iva = float(input("Inserire il prezzo lordo: "))
#
# [...] etc
 



# resto del codice che fa l'attuale lavoro di calcolo

# numeratore_valore_iva = int(input("Inserire il valore dell'IVA: "))
# 
# while numeratore_valore_iva < 0 or numeratore_valore_iva > 99:
#   print ("il valore dell'iva non è accettabile")
#   numeratore_valore_iva = int(input("Inserire il valore dell'IVA: "))
# 
# 
# valore_netto = (prezzo_con_iva)/(1 + numeratore_valore_iva / 100)
# 
# print (valore_netto)
