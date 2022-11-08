import itertools

a = 'https://www.quectel.com/wp-content/uploads/2021/0'
b = '/Quectel_5GLTE-Advanced_Module_Product_Overview_V4.3.pdf'
c = (len(a))


while c == 49:
    for i in range(4,10):
        nuovo_a = "".join([a, str(i), b])
        print(nuovo_a)
        c = len(nuovo_a)
if c == 50:
    a = a[:-1]
    for i in range(10,13):
        nuovo_a = "".join([a, str(i), b])
        print(nuovo_a)
        c = len(nuovo_a)








b = '/Quectel_5GLTE-Advanced_Module_Product_Overview_V'

for i, j in itertools.product(range(4,6), range(0,10)):

    nuovo_b = "".join([b,str(i),".",str(j),".pdf"])
    


    