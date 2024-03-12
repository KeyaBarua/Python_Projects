import turtle

import colorgram as cg
from turtle import Turtle, Screen
import random

colors = cg.extract("hirst_painting.jpg", 2 ** 32)
turtle.colormode(255)
# color_palette = []

# Extracting RGB colors using colorgram
# for count in range(len(colors)):
#     red = colors[count].rgb.r
#     green = colors[count].rgb.g
#     blue = colors[count].rgb.b
#     new_color = (red, green, blue)
#     color_palette.append(new_color)

color_palette = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]

# Creating objects
tim = Turtle()
screen = Screen()

# Making the screen full
screen.screensize()
screen.setup(width=1.0, height=1.0)


tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.goto(-200, -200)
tim.pendown()


for row in range(10):
    y = tim.ycor()
    for _ in range(10):
        color = random.choice(color_palette)
        tim.penup()
        tim.fd(50)
        tim.pendown()
        tim.dot(20, color)
    tim.penup()
    tim.setposition(-200, y + 50)
    tim.pendown()


screen.exitonclick()
