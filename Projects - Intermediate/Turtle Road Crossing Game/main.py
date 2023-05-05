from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up the screen and initial game setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game created by YJ-928")
screen.bgcolor("black")
screen.tracer(0)

# creating player obj from Player class
player = Player()
# creating scoreboard obj from ScoreBoard class
scoreboard = Scoreboard()
# creating car_manager obj from CarManager class
car_manager = CarManager()

# to listen and move player_turtle when
# user presses the up key in keyboard
screen.listen()
screen.onkey(player.move, "Up")

# variable as delay for creating new cars
count = 0


def move_and_create_cars():
    """To randomly gen new cars using CarManager class
    and move them from right to left continously"""
    global count
    # to continously move cars
    car_manager.move_car()
    # for creating random new cars after loop runs 6 times
    if count == 6:
        # to create new car
        car_manager.create_car()
        count = 0
    count += 1


# loop condition
game_is_on = True

# loop to run the game
while game_is_on:
    screen.update()
    sleep(0.1)
    move_and_create_cars()

    # detect turtle collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 27:
            scoreboard.gameover()
            game_is_on = False

    # detect player win, if turtle reaches top side of screen
    if player.ycor() > 260:
        sleep(2)
        player.reset()
        scoreboard.level_up()
        car_manager.car_speed_up()

# to avoid screen crashing
screen.exitonclick()
