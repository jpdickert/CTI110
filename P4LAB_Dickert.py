# CTI-110
# P4LAB Nested Loops
# Jason Dickert
# 27 June 2018
import turtle
t = turtle.Turtle()
t.pensize(10)
t.pencolor("Green")
for h in range(1,7):
    t.forward(50)
    t.left(60)
t.right(120)
for i in range(1,7):
    t.forward(200)
    t.backward(200)
    for j in range(1,4):
        t.forward(50)
        t.right(60)
        t.forward(50)
        t.backward(50)
        t.left(120)
        t.forward(50)
        t.backward(50)
        t.right(60)
    t.backward(150)
    t.left(120)
    t.forward(50)
    t.right(60)
turtle.exitonclick()
