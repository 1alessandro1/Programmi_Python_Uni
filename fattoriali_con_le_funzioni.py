def fiBBBBBonacci(n):
    a = 1 
    b = 1
    c = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

print(fiBBBBBonacci(8))

"""
def fatt(n):
    ris = 1
    for i in range (1,n+1):
        ris = ris * 1
    return ris

n = int(input("mettinpo: "))

print(fatt(n))
"""