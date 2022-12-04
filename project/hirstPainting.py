# # Part 1
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('project/hirstImage.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
from turtle import Turtle, Screen
import turtle as turtle_module
import random

hirst = turtle_module.Turtle()
hirst.shape("turtle")
turtle_module.colormode(255)
hirst.penup()
hirst.hideturtle()
color_list = [(169, 8, 49), (151, 88, 31), (68, 14, 37), (180, 158, 33), (51, 122, 84), (45, 100, 146), (214, 238, 223), (18, 40, 74), (105, 193, 142), (228, 219, 58), (66, 165, 112), (166, 51, 110), (111, 160, 211), (75, 29, 15), (152, 17, 10), (205, 75, 147), (208, 127, 182), (201, 164, 73), (25, 56, 41), (238, 217, 232), (217, 226, 234), (85, 82, 21), (74, 117, 206), (31, 45, 131), (27, 88, 63), (139, 221, 171), (217, 80, 55), (16, 84, 98), (69, 153, 166), (166, 147, 132), (128, 111, 104), (154, 161, 179), (217, 204, 135), (186, 101, 86), (226, 175, 168), (151, 162, 154), (183, 185, 211), (218, 177, 185), (185, 196, 186)]

# Part 2
# 10 x 10: 20 in size space: 50
# def random_color():
#     color = str(random.choice(color_list))
#     return color
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
hirst.speed("fastest")
number_of_dots = 100

for hirst_paint in range(1, number_of_dots + 1):
    hirst.dot(20, random.choice(color_list))
    hirst.forward(50)

    if hirst_paint % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)

screen = Screen()
screen.exitonclick()