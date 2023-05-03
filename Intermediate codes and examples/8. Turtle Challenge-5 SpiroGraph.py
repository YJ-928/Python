import random
import turtle
from turtle import Turtle, Screen

t = Turtle()
t.speed(0)
# setting turtle color mode to 255, to Gen color using RGB 0 to 255
turtle.colormode(255)


def Random_color():
    """Generates Random Color Tuples using RGB values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def spiro_graph(size_of_gap):
    """Draws a Spirograph (Many Circles slightly titlted from Origin)"""
    for _ in range(360//size_of_gap):
        t.color(Random_color())
        t.circle(100)
        # tilting the circle, by shifting turtle from its current heading
        # to a new heading ,  by incrementing it by 5 units
        current_heading = t.heading()
        t.setheading(current_heading+size_of_gap)


spiro_graph(5)

turtle.hideturtle()
screen = Screen()
screen.exitonclick()
