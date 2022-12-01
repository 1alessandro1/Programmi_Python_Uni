# fare una funzione che prende come parametro una stringa e vede se tale stringa è palindroma

# pseudocodice
# for i in range(len(parola)) serve verificare se l'i esimo carattere è uguale a l'i-esimo carattere - len(parola)
#
#
#
#



# def palindroma():
#     for i in range(len(parola)):
#         for j in range(len(parola) - 1):
#             while i < j:
#                 if parola[i] == parola[j]:
#                     pass
#                 else:
#                     t = False
#     return t
# 
# print(palindroma())

def palindroma(parola):

    if parola == "":
        return True

    i = 0
    j = len(parola) - 1
    trovato = False

    while i < j:
        if parola[i] != parola[j]:
            trovato = True
        i += 1
        j += -1
    return not trovato

# programma

s = input("Inserire una parola: ")
if palindroma(s):
    print(s, "è palindroma")
else:
    print(s, "non è palindroma")


def palindroma_veloce(parola):
    parola1 = parola[::-1]
    return parola == parola1

print(palindroma_veloce(s))
