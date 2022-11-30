import itertools
for i, j in itertools.product(range(0,11), range(0,11)):
    a = "".join([str(i),"*",str(j),"=", str(i*j)])
    print(a)    

# oppure
# n = 1
# while n <=10:
#     i = 1
#     while i <=10:
#         print(n*i), " ", end ="")
#         i = i + 1
#     n = n + 1
#     print()
