import turtle
from turtle import Turtle
import random

# Constants
COLORS = ["orange", "yellow", "green", "blue",
          "purple", "violet", "indigo", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SHAPE = "square"
CAR_LEN = 2
CAR_WID = 1


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_x = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates random cars"""
        new_car = Turtle()
        new_car.shape(CAR_SHAPE)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=CAR_WID, stretch_len=CAR_LEN)
        new_car.penup()
        new_car.goto(300, random.randint(-240, 240))
        self.all_cars.append(new_car)

    def move_car(self):
        """Continously Moves cars old & new generated"""
        for car in self.all_cars:
            new_x = car.xcor() - self.move_x
            car.goto(new_x, car.ycor())

    def car_speed_up(self):
        """Increments the Movement of cars as player level up's"""
        turtle.clear()
        self.move_x += MOVE_INCREMENT
