from turtle import Turtle, Screen
import turtle as t
import random

spiro = Turtle()
t.colormode(255)
spiro.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# python tuples - cant be changed unlike lists ex: (1, 3, 8)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
spiro.speed("fastest")

def draw_spiro(size_of_gap):
    for spiros in range(int(360 / size_of_gap)):
        spiro.circle(100)
        spiro.setheading(spiro.heading() + size_of_gap)
        # spiro.left(10)
        spiro.color(random_color())
        # walk.color(random.choice(colors))
draw_spiro(5)
screen = Screen()
screen.exitonclick()