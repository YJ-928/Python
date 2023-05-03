from os import path
import turtle
import random
from turtle import Turtle, Screen

# setting up screen
# taking user input
screen = Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_coords = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []  # a list that will contain all created turtles

# setting up turtles based on color (VIBGYOR)
# goto to make turtle goto their starting coordinates
# penup to avoid turtle's to draw while racing
for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coords[i])
    all_turtles.append(new_turtle)

# to start race only after user has placed their bet
if user_bet:
    is_race_on = True

# to actually move turtles
# determine and stop the game after one color wins
while is_race_on:

    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
