from turtle import Turtle, Screen
import random

color = ["red", "green", "blue", "orange",
         "yellow", "black", "grey", "pink", "purple", "violet"]

t = Turtle()
t.shape("turtle")
Total = 360
sides = 3


def triangele_to_decagon(sides):
    """Function to Draw any shape, Based on Side and Angle"""
    if sides > 10:
        return
    global Total
    angle = (Total // sides)  # cal turn angle
    # randomizing Color
    Color = random.choice(color)
    t.color(Color)
    for _ in range(sides):  # based on Num of sides
        t.forward(100)
        t.right(angle)
        # calling back the same function with sides += 1
    return triangele_to_decagon(sides=sides+1)


triangele_to_decagon(sides)
screen = Screen()
screen.exitonclick()
