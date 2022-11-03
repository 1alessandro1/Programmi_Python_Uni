from math import *

x1 = float(input("x1: ") )
y1 = float(input("y1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))

r1 = abs(float(input("r2: ")))
r2 = abs(float(input("r2: ")))

d = sqrt(abs((x2-x1)**2 - (y2-y1)**2))

if r1+r2 >= d:
    print("si toccano")
else:
    print("non si toccano")
