import turtle
import random
from turtle import Turtle, Screen
from time import sleep
from art import logo

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178,
                                                                                                                                                                                                                                               149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t = Turtle()
turtle.colormode(255)
t.speed(0)
t.hideturtle()


def move_turtle_to_corner():
    """Moves the turtle to a corner of the screen 
    to start painting from there"""
    t.hideturtle()
    t.penup()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)


def move_turtle_to_line_start():
    """Moves the turtle back to starting line position"""
    t.hideturtle()
    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


def turtle_paints(Number_of_Lines):
    """Painting a Dot Picture using Turtle"""
    move_turtle_to_corner()
    while Number_of_Lines != 0:
        for _ in range(10):
            turtle.hideturtle()
            t.dot(20, random.choice(color_list))
            t.penup()
            t.forward(50)
        move_turtle_to_line_start()
        Number_of_Lines -= 1


print(logo)
turtle_paints(Number_of_Lines=turtle.numinput(title="Number of lines",
              prompt="Enter the number of lines? that you want in your painting: "))
if turtle.textinput(title="Play Again?", prompt="Do you want to draw again?, Type 'y' for Yes 'n' for No: ").lower() == "y":
    turtle_paints(Number_of_Lines=int(
        input("How many lines of Dots you need in your painting? : ")))
else:
    sleep(2)
    exit()

screen = Screen()
screen.exitonclick()
