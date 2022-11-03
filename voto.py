votoNormale = input("Inserire il voto: ")

if len(votoNormale) == 1:
    print("il voto decimale è",int(votoNormale)) 

else:
    segno = votoNormale[len(votoNormale) - 1]
    # accedo all'ultimo carattere della stringa calcolando la sua lunghezza e accedendo al carattere collocato alla lunghezza -1
    votodec = float(votoNormale[0:len(votoNormale)-1])
    
    if segno == '-':
        votodec = votodec - 0.25
    elif segno == '+':
        votodec = votodec + 0.25
    else:
        print("hai inserito un carattere errato nel voto")
    print (votodec)




# votoclassico 10- 7+ 7

# 7+ 7,25
# 
# 7- = 6.75
# 
# 10- 9.75


"""
come lo ha scritto il prof

v = input("voto:")
ris = float(v[0])
if len(v) == 2:
    if v[1] == "+":
        r(is = ris + 0.25
    else:
        ris = ris - 0.25
print("il voto è: ", ris)

"""