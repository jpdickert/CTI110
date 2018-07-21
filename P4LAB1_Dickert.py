# CTI-110
# P4T1
# Jason Dickert
# 25 June 2018
import turtle
turtle.shape("turtle")
square = 0
triangle = 0
while square < 4:
    turtle.forward(50)
    turtle.left(90)
    square = square + 1
while triangle < 3:
    turtle.forward(100)
    turtle.left(120)
    triangle = triangle + 1
turtle.exitonclick()
