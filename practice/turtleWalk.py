from turtle import Turtle, Screen
import turtle as t
import random

walk = Turtle()
t.colormode(255)
walk.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# python tuples - cant be changed unlike lists ex: (1, 3, 8)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

walk.speed('fastest')
walk.pensize(15)
for walks in range(200):
    walk.forward(30)
    walk.setheading(random.choice(directions))
    walk.color(random_color())
    # walk.color(random.choice(colors))

screen = Screen()
screen.exitonclick()