x = 10 # variabile globale
y = 9 # variabile globale
def fun():
    global y #
    y = 8 # y viene modificato!
print(x, y) # stampa 10 9
fun()
print(x, y) # stampa 10 8

# non usare le global