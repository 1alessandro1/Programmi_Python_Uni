from decimal import Decimal, getcontext
from math import *

getcontext().prec = 500000000000

# print("   math.sqrt: {0}", (Decimal(math.sqrt(num))))

# ho già il lato dell'esagono

lato = Decimal(1)

print("Utilizzeremo il metodo di Archimede per calcolare Pi greco")
print("Il numero di lati di un poligono regolare inscrivibile in una circonferenza raddoppia ogni volta partendo dall'esagono")

n = int(input("Selezionare fino a quanto si vuole moltiplicare per 2^n-volte partendo da 6*2^n il numero dei lati del poligono che approssima il cerchio: "))

for i in range (n):
    
    contatore_lati = Decimal(6*2**i)
    perimetro = Decimal(contatore_lati) * Decimal(lato) # stampiamo il valore del perimetro e printiamo il suo valore con il valore del numero dei lati
    print("Abbiamo", Decimal(contatore_lati), "lati", "il perimetro di un poligono regolare con tali lati è", (Decimal(perimetro)))
    print("Pi-greco è circa", (Decimal(perimetro)/2))
    
    # inizio a calcolare apotema e dimensione del lato
    
    apotema = Decimal(sqrt(1-(Decimal(lato)/2)**2))
    lato_nuovo = Decimal(sqrt(((1-Decimal(apotema))**2) + (Decimal(lato)/2)**2))
    print("La lunghezza del lato quando si hanno", 6*2**i, "lati è", (lato_nuovo))
    lato = lato_nuovo
    #print(type(lato))
    #print(type(lato_nuovo))


    























"""
   nuovo_lato = sqrt(((1-(apotema)**2)**2 + (lato/2)**2))
    
    
    
    
    
    
    lato = nuovo_lato
    n_lati_poligono_regolare = 3*4**i
    print(x,numero_lati_poligono_regolare)

    


perimetro = nuovo_lato * x

print(perimetro)

"""