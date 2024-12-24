import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

colors = colorgram.extract('200430102527-01-damien-hirst-severed-spots.jpg', 30)

colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_in_image = (r,g,b)
    colors_list.append(color_in_image)


screen.setworldcoordinates(0, 0, 800, 600)
tim.up()

for i in range(10):
    for j in range(10):
        tim.dot(20,random.choice(colors_list))
        tim.fd(50)
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.right(180)



screen.exitonclick()
