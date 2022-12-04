from turtle import Turtle, Screen


mabe_the_turtle = Turtle()
mabe_the_turtle.shape("turtle")
mabe_the_turtle.color("magenta")
for turns in range(0,4):
    mabe_the_turtle.forward(100)
    mabe_the_turtle.right(90)


screen = Screen()
screen.exitonclick()