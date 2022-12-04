from turtle import Turtle, Screen


mabe = Turtle()
mabe.shape("turtle")
mabe.color("magenta")
for turns in range(0,4):
    mabe.forward(100)
    mabe.right(90)


screen = Screen()
screen.exitonclick()