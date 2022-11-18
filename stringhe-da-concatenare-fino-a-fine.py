frase = []

while True:
    ele = (input("Input: "))
    frase.append(ele) # adding the element
    if ele == "FINE":
        frase = frase[:-1]
        break
    
print(frase)

# Senza liste

frase = ""

stringa = input("mettinpo: ")
while stringa != "FINE":
    frase = frase + stringa + " "
    stringa = input("mettinpo: ")
print("La frase è:\n" + frase.strip())