import math

a = float(input("inserisci a: "))
b = float(input("inserisci b: ")) 
c = float(input("inserisci c: "))

delta = (b*b - 4*a*c)

if delta < 0:
    print("L'equazione non ha soluzioni perché il delta è minore di zero")

elif a == 0:
        x_primogrado = (-c)/(b)
        print("La soluzione dell'equazione di secondo grado degenere al primo che hai inserito è", x_primogrado)
else:
    x1 = (-b + (math.sqrt(delta)))/ (2*a)
    x2 = (-b - (math.sqrt(delta)))/ (2*a)
    print("Le soluzioni dell'equazione di secondo grado che hai inserito sono", x1, x2)

    