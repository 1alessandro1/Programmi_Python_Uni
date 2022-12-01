from math import *

a = int(input("inserisci il primo numero: "))
b = int(input("inserisci il secondo numero: "))

if gcd(a,b) == 1:
    print("i numeri sono primi tra loro")
else: 
    print("i numeri non sono primi tra loro")