# import sys

def PrendiPrezzoLordoGiusto():
    prezzo_con_iva = input("Inserisci il prezzo lordo: ")
    while True:
        try:
            prezzo_con_iva = float(prezzo_con_iva)
            break
        except:
            print("Valore non corretto, riprova")
            prezzo_con_iva = input("Re-inserisci il prezzo lordo: ")
    return prezzo_con_iva

def PrendiValoreIVAGiusto():
    numeratore_valore_iva = input("Inserisci il valore del numeratore dell' IVA: ")
    while True:
        try:
            numeratore_valore_iva = float(numeratore_valore_iva)
            break
        except:
            print("Valore non corretto, riprova")
            numeratore_valore_iva = input("Re-inserisci il valore del numeratore dell' IVA: ")
    return numeratore_valore_iva


#print(PrendiPrezzoLordoGiusto())
#print(PrendiValoreIVAGiusto())



while numeratore_valore_iva < 0 or numeratore_valore_iva > 99:
   print ("Il valore dell'iva non è accettabile")
   numeratore_valore_iva = int(input("Re-nserire il valore dell'IVA: "))
 
valore_netto = (prezzo_con_iva)/(1 + numeratore_valore_iva / 100)
 
print (valore_netto)






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
