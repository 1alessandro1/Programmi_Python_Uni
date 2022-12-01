from turtle import Turtle
MinDist = 10
t = Turtle(); t.color("blue"); t.width(2)
def lato(l):
    if l < MinDist :
        t.forward(l) # caso base
    else:
        t.speed(1000000)
        lato(l/3) # passo
        t.left(60) # ricorsivo
        lato(l/3)
        t.right(120)
        lato(l/3)
        t.left(60)
        lato(l/3)
lato(300)