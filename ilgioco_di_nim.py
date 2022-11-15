import secrets

secure_number = secrets.SystemRandom()

a = secure_number.randrange(10, 100)

print(a)

# while 
#     somma = 