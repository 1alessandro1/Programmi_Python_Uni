import random

conto_dei_lanci_uguali = 0

for i in range(1000):
    lancio_1 = random.randrange(1,7)
    lancio_2 = random.randrange(1,7)
    
    if lancio_1 == lancio_2:
        conto_dei_lanci_uguali += 1

print(conto_dei_lanci_uguali)

