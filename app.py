# print("tests")
# import turtle
# from turtle import *
# t = Turtle()
# t.shape('turtle')

# t.forward(200)
# t.forward(100)

# def square(x):
#     t.forward(x)
#     t.left(90)
#     t.forward(x)
#     t.left(90)
#     t.forward(x)
#     t.left(90)
#     t.forward(x)
#     t.left(90)
# square(90)

# turtle.done()

import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

# def square(x, y):
#     for i in range(4):
#          t.forward(x)
#          t.left(y)

# def doubleSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 2
# doubleSquares(6)
# def doubleSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 2
# doubleSquares(5)
def triangle (x,y):
    for i in range(3):
     t.forward(60)
     t.left(120)
     t.forward(60)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(100,90)

turtle.done()