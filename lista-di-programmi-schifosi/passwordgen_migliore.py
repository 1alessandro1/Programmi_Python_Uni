import secrets
import string

pwd_length = 12
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(string.ascii_letters))

print(pwd)