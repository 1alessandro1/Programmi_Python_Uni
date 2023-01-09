UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']

def controlloPassword(password_lista):
    for i in range(len((password_lista))):
        if password_lista[i] not in UPPERCASE:
            presenza_uppercase = False
        elif password_lista[i] not in LOWERCASE:
            presenza_lowercase = False
        elif password_lista[i] not in DIGITS:
            presenza_digits = False
        elif password_lista[i] not in SPECIAL:
            presenza_special = False
    return presenza_uppercase, presenza_digits, presenza_special

password = "aaaaaaaaaaaaaaaaa"
password_lista = list(password)

# print(password_lista)

presenza_uppercase = True
presenza_lowercase = True
presenza_digits = True
presenza_special = True



print(controlloPassword(password_lista))