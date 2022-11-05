import itertools

a = 'https://www.quectel.com/wp-content/uploads/2021/0'
b = '/Quectel_5GLTE-Advanced_Module_Product_Overview_V4.3.pdf'
c = (len(a+b))


while c == 105:
    for i in range(4,10):
#       print(a,end = "")
#       print(i,end = "")
#       print(b)
        nuovo_a = "".join([a, str(i), b])
        print(nuovo_a)
        c = len(nuovo_a)

if c == 106:
    a = a[:-1]
    for i in range(10,13):
#       print(a,end = "")
#       print(i,end = "")
#       print(b)
        nuovo_a = "".join([a, str(i), b])
        print(nuovo_a)
        c = len(nuovo_a)



# ora serve manipolare b

# b = '/Quectel_5GLTE-Advanced_Module_Product_Overview_V4.3.pdf'


b = '/Quectel_5GLTE-Advanced_Module_Product_Overview_V'

for i, j in itertools.product(range(4,6), range(0,10)):
#    print(b,end = "")
#    print(".", end = "")
#    print(i, end = "")
#    print(".", end = "")
#    print(j, end = "")
#    print(".pdf")
    nuovo_b = "".join([b,str(i),".",str(j),".pdf"])
    print(nuovo_b)
    


# b deve avere tutte le combinazioni tra che so 