import turtle
import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)
turtle.colormode(255)


def move_forwards():
    """Move Tim Forward"""
    tim.forward(10)


def move_backwards():
    """Move Tim Backward"""
    tim.back(10)


def turn_left():
    """Turn Tim Left"""
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    """Turn Tim Right"""
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    """Reset's The Drawing Board"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def pen_up():
    """Makes Tim Hold PenUp and Move"""
    tim.penup()


def draw():
    """Makes Tim Put PenDown and Continue Drawing"""
    tim.pendown()


def Random_color():
    """Generates Random Color Tuples using RGB values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def change_color():
    """Makes Tim Change Pen Color"""
    tim.pencolor(Random_color())


def change_penSize():
    """Makes Tim Change Pen Color"""
    tim.pensize(random.choice([2, 4, 6, 8, 10, 12, 14]))


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.onkey(pen_up, "p")
screen.onkey(draw, "d")
screen.onkey(change_color, "z")
screen.onkey(change_penSize, "x")

screen.exitonclick()
