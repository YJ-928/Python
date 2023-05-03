from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("red")


def DashLine():
    """To draw a dashed line using penUp and penDown cmd"""
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


for _ in range(20):
    DashLine()

screen = Screen()
screen.exitonclick()
