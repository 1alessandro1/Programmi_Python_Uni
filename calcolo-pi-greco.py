from math import *

# ho già il lato dell'esagono

lato = 1


print("Utilizzeremo il metodo di Archimede per calcolare Pi greco")
print("Il numero di lati di un poligono regolare inscrivibile in una circonferenza raddoppia ogni volta partendo dall'esagono")

n = int(input("Seleziona fino a quale: "))

for i in range (n):
    
    contatore_lati = 6*2**i
    perimetro = contatore_lati * lato # stampiamo il valore del perimetro e printiamo il suo valore con il valore del numero dei lati
    print("Abbiamo", contatore_lati, "lati", "il perimetro di un poligono regolare con tali lati è", perimetro)
    print("pigreco è circa", perimetro/2)

    # inizio a calcolare apotema e dimensione del lato

    apotema = sqrt(1-(lato/2)**2)
    lato_nuovo = sqrt(((1-apotema)**2) + (lato/2)**2)
    print("La lunghezza del lato quando si hanno", 6*2**i, "lati è", lato_nuovo)
    lato = lato_nuovo

    























"""
   nuovo_lato = sqrt(((1-(apotema)**2)**2 + (lato/2)**2))
    
    
    
    
    
    
    lato = nuovo_lato
    n_lati_poligono_regolare = 3*4**i
    print(x,numero_lati_poligono_regolare)

    


perimetro = nuovo_lato * x

print(perimetro)

"""