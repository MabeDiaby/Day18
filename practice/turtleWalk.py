from turtle import Turtle, Screen
import random

walk = Turtle()
walk.shape("turtle")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

walk.speed('fastest')
walk.pensize(15)
for walks in range(200):
    walk.forward(30)
    walk.setheading(random.choice(directions))
    walk.color(random.choice(colors))

screen = Screen()
screen.exitonclick()