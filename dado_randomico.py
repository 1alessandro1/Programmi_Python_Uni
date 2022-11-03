import random


f1=f2=f3=f4=f5=f6=0

for i in range(1000):

    faccia = random.randrange(1,7)
    if faccia == 1:
        f1 += 1
    if faccia == 2:
        f2 += 1
    if faccia == 3:
        f3 += 1
    if faccia == 4:
        f4 += 1
    if faccia == 5:
        f5 += 1
    if faccia == 6:
        f6 += 1

print("La faccia col valore 1 è uscita", f1, "volte")
print("La faccia col valore 2 è uscita", f2, "volte")
print("La faccia col valore 3 è uscita", f3, "volte")
print("La faccia col valore 4 è uscita", f4, "volte")
print("La faccia col valore 5 è uscita", f5, "volte")
print("La faccia col valore 6 è uscita", f6, "volte")


