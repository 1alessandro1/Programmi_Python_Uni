targa = "DE" + 295 + "WK" # TypeError: can only concatenate str (not "int") to str

# per printare una targa serve prima convertire il 295 in stringa

targa = "DE" + str(295) + "WK"

# Funzioni di conversione

a = int(3.14)
print (a)

a = int("12")
print(a)

a = float (22)
print (a)

a = float("3.14")
print (a)