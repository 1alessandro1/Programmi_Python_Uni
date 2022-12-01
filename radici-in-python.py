n = int(input("inserisci n: "))
x = float(input("inserisci un guess iniziale: "))
p = int(input("inserisci la precisione: "))

for i in range(p):
    xn_migliore = 0.5 * (x + (n / x))
    x = xn_migliore

print(xn_migliore)