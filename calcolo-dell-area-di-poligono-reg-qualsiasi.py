from math import *

n_lati = abs(int(input("Inserisci il numero dei lati del poligono regolare: ")))

dim_lato = abs(float(input("Inserisci la dimensione del lato (in cm): ")))

ang_int = 180 * (n_lati - 2)

singolo_angolo = (ang_int / n_lati) / 2

# Qua succede il macello perché python utilizza i radianti quindi 90 = pi/2, 60 = pi/3) eccetera. 

apotema = ((dim_lato / 2)) * abs(sin(radians((singolo_angolo))) ) / (abs(cos (radians(singolo_angolo))))

perimetro = n_lati * dim_lato

area = (perimetro * apotema) / 2


print ("In base ai dati inseriti, l'area del poligono regolare è di", area, "cm^2")

