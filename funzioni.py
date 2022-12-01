# Servono per risolvere dei sottoproblemi, il programma principale
# consiste nelle chiamate di queste funzioni

# print, len, sqrt sono tutte funzioni
# print si differenzia da len e sqrt perché len e sqrt ritornano dei valori, 
# mentre Print "fa" qualcosa, non ritorna nulla
# print si chiama "procedura" = fa qualcosa ma non restituiscono alcun valore
# mentre le altre sono funzioni che ritornano qualcosa 
# 

# le funzioni hanno associato un nome ed un codice
# per definire una funzione si usa la parola chiave "def" - esempio

from math import *

def righe():
    print("-" * 20)
    print("-" * 20)

righe() # salta alla def ed esegue quel codice
print("ciao")
righe() # salta alla def ed esegue quel codice

#

# 
x = sqrt(2)

def righe(car):
    print(car * 20)
    print(car * 20)

# car è il parametro formale

righe("#")
print("ciao")
righe("+")

# 
# 
# 
# risultato:
# 
# 
# --------------------
# --------------------
# ciao
# --------------------
# --------------------
# ####################
# ####################
# ciao
# ++++++++++++++++++++
# ++++++++++++++++++++
# 
# 
# 

def righe(car = "-", num_car = 20):
    print(car * num_car)
    print(car * num_car)


righe()
righe("#")
righe("*", 30)
righe(num_car = 10)
righe(num_car = 10, car = "-")

# dentro il richiamo della funzione specifico le variabili locali della funzione da eseguire