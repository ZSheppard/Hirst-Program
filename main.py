#Damien Hirst Painting Project
#Zachary Sheppard
#September 4, 2023
#Learned how install and use online python library 'colorgram' from pypi


import colorgram
import random
import turtle
from turtle import *

#Code to extract colors from jpg
"""""
colors = colorgram.extract('DamienHirst.jpg', 30)
color_list = []
print(f"{colors}")

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

print(f"{color_list}")

"""""

tim = Turtle()
#Set pencolor to be represented by RGB tuples
turtle.colormode(255)
#Extracted RGB colors from colorgram and jpg
color_list = [(253, 251, 247), (253, 249, 252), (232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]

tim.penup()
tim.setpos(-300, -300)
tim.speed(50)

for y in range(1, 11):
    dot_distance = 60
    for x in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(30)
        tim.forward(dot_distance)

    tim.setpos(-300, -300 + (dot_distance * y))


screen = Screen()
screen.exitonclick()


