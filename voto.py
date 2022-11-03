from math import *

votoNormale = input("Inserire il voto: ")

if len(votoNormale) == 1:
    print("il voto decimale è",int(votoNormale)) 

else:
    segno = votoNormale[len(votoNormale) - 1]
    
    votodec = float(votoNormale[0:len(votoNormale)-1])
    
    if segno == '-':
        votodec = votodec - 0.25
    
    elif segno == '+':
        votodec = votodec + 0.25
    
    print (votodec)




# votoclassico 10- 7+ 7

# 7+ 7,25
# 
# 7- = 6.75
# 
# 10- 9.75