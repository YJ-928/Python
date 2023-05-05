from turtle import Turtle
import random

# Constants
MIN_X = -270
MAX_X = 270
MIN_Y = -270
MAX_Y = 270
FOOD_SHAPE = "circle"
FOOD_LEN = 0.5
FOOD_WID = 0.5
FOOD_COLOR = "red"
FOOD_SPEED = "fastest"


class Food(Turtle):
    # Inheriting from Turtle Super-Class
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        # to create a food of size 10x10
        # divide the turtle dimension by half
        self.shapesize(stretch_len=FOOD_LEN, stretch_wid=FOOD_WID)
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.refresh()

    def refresh(self):
        """make our food appear randomly anywhere
        Refresh food location once snake collids with it"""
        x_coords = random.randint(MIN_X, MAX_X)
        y_coords = random.randint(MIN_Y, MAX_Y)
        self.goto(x_coords, y_coords)
