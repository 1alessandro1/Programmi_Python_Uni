from turtle import *
import random
color('red', 'yellow')
speed(0)
i = 0
for i in range(100):
    caso = random.randrange(0,4)
    if caso == 0:
        forward(random.randrange(0,2))
    elif caso == 1: 
        left(random.randrange(0,2))
    elif caso == 2:
        right(random.randrange(0,2))
    elif caso == 3: 
        backward(random.randrange(0,2))
print(turtle.position())
done()