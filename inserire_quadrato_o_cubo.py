n = ""
Q = set()
C = set()

while n != 0:
    n = int(input("Inserire positivo oppure 0: "))
    Q.add(n*n)
    C.add(n*n*n)

print(Q)
print(C)