# importing turtle module
from turtle import Turtle, Screen

# assigning object to turtle class
my_turtle = Turtle()
screen = Screen()
my_turtle.speed(0)
# print(my_turtle, screen)

# changing turtle shape to actual turtle
# changing turtle color
my_turtle.shape("turtle")
my_turtle.color("DarkOrange")

# to allow us to exit screen only when clicked on it
screen.exitonclick()
