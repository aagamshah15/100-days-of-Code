from turtle import Turtle, Screen, colormode
import random

colormode(255)
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Drawing a square
def draw_square(turtle, side):
    for _ in range():
        turtle.right(90)
        turtle.fd(side)


# Drawing a dotted line
def dotted_line(turtle, size):
    for _ in range(0, 10):
        turtle.fd(size)
        turtle.pu()
        turtle.fd(size)
        turtle.pd()


# Drawing different polygons
def draw_polygon(turtle, sides):
    angle = 360/sides
    for _ in range(sides):
        turtle.fd(100)
        turtle.right(angle)


# for side in range(3, 11):
    # timmy.color(random.choice(colors))
    # draw_polygon(timmy, side)

# Drawing a random walk
# timmy.width(5)
timmy.speed("fastest")


def random_walk(turtle):
    for _ in range(200):
        turtle.color(random_colors())
        directions = [0, 90, 180, 270]
        turtle.fd(30)
        turtle.setheading(random.choice(directions))


# Draw a spirograph
def spirograph(turtle, angle):
    for _ in range(int(360/angle)):
        turtle.color(random_colors())
        turtle.circle(150)
        turtle.left(angle)


spirograph(timmy, 5)

my_screen = Screen()
my_screen.exitonclick()
