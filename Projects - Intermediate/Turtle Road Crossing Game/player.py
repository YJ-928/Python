from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_COLOR = "red"
PLAYER_SHAPE = "turtle"
PLAYER_SPEED = "fastest"


class Player(Turtle):

    def __init__(self):
        """Player class inherits from Turtle super class"""
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.speed(PLAYER_SPEED)
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.move_y = MOVE_DISTANCE

    def move(self):
        """Moves the turtle up by MOVE_DISTANCE"""
        new_y = self.ycor() + self.move_y
        self.goto(self.xcor(), new_y)

    def reset(self):
        """Moves the player back to starting position"""
        self.goto(STARTING_POSITION)
