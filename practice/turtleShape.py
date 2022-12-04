from turtle import Turtle, Screen
import random

shape = Turtle()
shape.shape("turtle")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for sides in range(num_sides):
        shape.forward(100)
        shape.right(angle)

for shape_side_n in range(3,11):
    shape.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()