import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

t.forward(200)
t.forward(100)

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(90)

turtle.done()