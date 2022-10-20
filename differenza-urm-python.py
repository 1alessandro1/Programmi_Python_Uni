print("Calcolo di RO - R1")


a = int(input("Inserisci R0: "))

b = int(input("Inserisci R1: "))

c = 0 # casella vuota defiinta prima di entrare nel while

while a != b:
    c = c + 1
    b = b + 1
    print (a,b,c)

print (c)