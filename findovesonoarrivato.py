# Funzione per controllare che l'utente abbia inserito un prezzo ivato con numeri decimali

def PrendiPrezzoIvatoGiusto():
    prezzo_con_iva = input("Inserisci il prezzo ivato: ")
    while True:
        try:
            prezzo_con_iva = float(prezzo_con_iva)
            break
        except:
            print("Il valore contiene dei caratteri che non sono numeri decimali, riprova")
            prezzo_con_iva = input("Re-inserisci il prezzo ivato: ")
    prezzo_con_iva = float(prezzo_con_iva)
    return prezzo_con_iva

# Funzione per controllare che l'utente abbia inserito un valore dell'iva con numeri decimali

def PrendiNumeratoreValoreIvaGiusto():
    numeratore_valore_iva = input("Inserisci il prezzo ivato: ")
    while True:
        try:
            numeratore_valore_iva = float(numeratore_valore_iva)
            break
        except:
            print("Il valore del numeratore dell'iva inserito contiene dei caratteri che non sono numeri decimali, riprova")
            numeratore_valore_iva = input("Re-inserisci il prezzo ivato, contiene dei caratteri non ammessi: ")
    numeratore_valore_iva = float(numeratore_valore_iva)
    return numeratore_valore_iva


def DominioIVA():  
    while PrendiNumeratoreValoreIvaGiusto() < 0 and PrendiNumeratoreValoreIvaGiusto() > 99:
        print("il valore dell'iva inserito è fuori dal range ammesso, riprovare")
        
    return 
   
    
    # boh come mazza ci torno alla funzione che mi ricontrolla se è un numero che non ha caratteri dopo che gli ho detto che è troppo grosso?

    valore_iva_da_controllare = float(valore_iva_da_controllare)
    return valore_iva_da_controllare

    


valore_netto = (prezzo_con_iva)/(1 + numeratore_valore_iva / 100)
 
    


#print(PrendiPrezzoIvatoGiusto())
#print(PrendiNumeratoreValoreIvaGiusto())


c = PrendiPrezzoIvatoGiusto() * 2
print(c)
# print(DominioIVA())



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
# prezzo_con_iva = float(input("Inserire il prezzo ivato: "))
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



# Roba astrusa per evitare di perdere l'int

def PrendiValoreIVAGiusto():
    numeratore_valore_iva = input("Inserisci il valore del numeratore dell' IVA: ")
    while True:
        try:
            numeratore_valore_iva = float(numeratore_valore_iva)
            break
#               numeratore_valore_iva = print(input("Riprovare: "))
        except:
                PrendiValoreIVAGiusto()
#        return numeratore_valore_iva

def DominioIVA():
    numeratore_valore_iva = float(PrendiValoreIVAGiusto())   
    while numeratore_valore_iva > 0 or numeratore_valore_iva < 99:
        return float(numeratore_valore_iva)