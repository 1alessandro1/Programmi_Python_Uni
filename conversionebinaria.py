# def ConvertiInBinario(n):
n = int(input("Inserisci n: "))
binString = []
ris = ""
while n > 0:
	binString.append(n % 2)
	n = int(n // 2)
binString.reverse()
for i in range(len(binString)):
    ris += str(binString[i])
 
print(ris)