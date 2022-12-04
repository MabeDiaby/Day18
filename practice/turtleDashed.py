from turtle import Turtle, Screen

dashed = Turtle()
dashed.shape("turtle")

for dash in range(0,15):
    dashed.forward(10)
    dashed.penup()
    dashed.forward(10)
    dashed.pendown()



screen = Screen()
screen.exitonclick()