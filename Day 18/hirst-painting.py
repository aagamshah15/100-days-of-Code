import random
import colorgram
from turtle import Turtle, Screen, colormode
colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(250, 246, 243), (248, 245, 246), (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98)]

timmy = Turtle()
timmy.speed("fastest")
timmy.pu()

timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.fd(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen = Screen()
my_screen.exitonclick()




