# dati in input

from math import sqrt

# Distanza lineare tra la posizione del robot e la proiezione ortogonale della distanza tra l'oggetto

dx = float(input("Inserisci dx in metri: "))

 # Distanza dell'oggetto dalla strada, dy (in metri)

dy = float(input("Inserisci dy in metri: "))

# velocità sul primo tratto (speed 1) in km/h

s1 = float(input("Inserisci s1: "))

# velocità sul secondo tratto (speed 2) in km/h

s2 = float(input("Inserisci s2: "))

# distanza lineare tra k

l1 = float(input("Inserisci l1: "))
# velocita_su_l2 = float(input("Inserisci la velocità su l2: "))

t1 = l1 / s1

l2 = sqrt((dx-l1)*(dx-l1)  + dy*dy)

t2 = l2 / s2

print("Tempo totale:" , t1+t2)
