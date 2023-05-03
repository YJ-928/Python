from turtle import Turtle, Screen
import random
import turtle

Directions = [0, 90, 180, 270]

t = Turtle()
t.pensize(15)
t.speed(0)
# setting turtle color mode to 255, to Gen color using RGB 0 to 255
turtle.colormode(255)


def Random_color():
    """Generates Random Colors using RGB values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def RandomWalk():
    """Makes the turtle walk in a random direction"""
    Direction = random.choice(Directions)
    t.pencolor(Random_color())
    t.forward(30)
    t.setheading(Direction)


for _ in range(200):
    RandomWalk()

screen = Screen()
screen.exitonclick()
