# ciaoo VERO deve dare (SI SI RIPETE)
# ciao deve dare FALSO (NO NON SI RIPETE).
# 
# 
# ciaooooooooooo len ciao è 5
# ciaooooooooo
# 
# cia

# Data una stringa, printare vero se l'ultimo carattere si ripete = "SI SI RIPETE" vero altrimenti non si ripete "NO NON SI RIPETE"

a = input("Inserisci una stringa: ") 
while a == "":
    a = input("Inserisci una stringa: ") 
    for i in range(len(a)-1):
        if a[i] == a[-1]: 
            print("SI RIPETE")
            break
        elif i == (len(a)-2) :
            print("NON SI RIPETE")