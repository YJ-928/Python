from turtle import Turtle
import turtle

# Declaring Constants (as all caps in Pascal-case)
# coordinates for start of game & snake creation
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0
SNAKE_LEN = 0.7
SNAKE_WID = 0.7
SNAKE_COLOR = "orange"
SNAKE_SHAPE = "square"


class Snake:

    def __init__(self):
        # empty list, containing all snake_segments
        self.turtle_snake = []
        self.create_snake()
        self.snake_head = self.turtle_snake[0]

    def create_snake(self):
        """Creating our snake using single sq turtles as segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Creates a new snake segment"""
        snake_segment = Turtle(shape=SNAKE_SHAPE)
        snake_segment.color(SNAKE_COLOR)
        snake_segment.penup()
        snake_segment.shapesize(
            stretch_len=SNAKE_LEN, stretch_wid=SNAKE_WID)
        snake_segment.goto(position)
        self.turtle_snake.append(snake_segment)

    def extend_snake(self):
        """Extends the snake by 1 segment
        Each time it eats a peice of Food"""
        self.add_segment(self.turtle_snake[-1].position())

    def move(self):
        """Moves the snake in our desired direction"""
        # to make the other segments follow the Snake Head
        # we make the snake head move as per user commands
        for seg_num in range(len(self.turtle_snake)-1, 0, -1):
            new_x_coords = self.turtle_snake[seg_num - 1].xcor()
            new_y_coords = self.turtle_snake[seg_num - 1].ycor()
            self.turtle_snake[seg_num].goto(new_x_coords, new_y_coords)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves the snake in north/up (90-degree) direction"""
        if self.snake_head.heading() != MOVE_DOWN:
            self.snake_head.setheading(MOVE_UP)

    def down(self):
        """Moves the snake in south/down (270-degree) direction"""
        if self.snake_head.heading() != MOVE_UP:
            self.snake_head.setheading(MOVE_DOWN)

    def left(self):
        """Moves the snake in west/left (180-degree) direction"""
        if self.snake_head.heading() != MOVE_RIGHT:
            self.snake_head.setheading(MOVE_LEFT)

    def right(self):
        """Moves the snake in east/right (0-degree) direction"""
        if self.snake_head.heading() != MOVE_LEFT:
            self.snake_head.setheading(MOVE_RIGHT)

    def reset(self):
        """Clears and restarts the game whenever GameOver is triggered"""
        for segments in self.turtle_snake:
            segments.goto(1000, 1000)
        turtle.clear()
        self.turtle_snake = []
        self.create_snake()
        self.snake_head = self.turtle_snake[0]
