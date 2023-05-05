from os import path
import turtle
import os
from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# setting up the main game screen 600x600 & Black BG
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game Created By YJ-928")
# to hide all turtle activities on screen
screen.tracer(0)

# initializing our snake and food from resp classes
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# continuosly listen and wait for key_press or user_commands
# after detecting key, call and execute resp func
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# while loop condition
game_is_on = True

# loop to continously run the game
while game_is_on:
    # to see snake only after all segments have moved
    screen.update()
    sleep(0.1)
    snake.move()

    # detect collision with food
    # Score a point
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect collision with wall
    # GameOver == GameRestart
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.game_restart()
        snake.reset()

    # detect collision with tail
    # GameOver == GameRestart
    for segment in snake.turtle_snake[1::]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_restart()
            snake.reset()

# to exit screen only if we click on it
screen.exitonclick()
