from turtle import Turtle, Screen

# def tutle object
t = Turtle()
t.shape("turtle")
t.color("red")


def turtle_square():  # defining function
    """Makes the turtle draw a square"""
    for _ in range(4):
        t.forward(100)
        t.right(90)


turtle_square()  # calling the function
screen = Screen()
screen.exitonclick()
