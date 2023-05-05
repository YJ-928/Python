from turtle import Turtle

# Constants
SCORE_SPEED = "fastest"
SCORE_COLOR = "orange"
SCORE_ALIGN = "center"
SCORE_FONT = ("Courier", 18, "bold")
DISPLAY_COORDS = (-240, 240)
GAME_OVER = ("Courier", 28, "bold")
FINISH_LINE_COLOR = "white"
FINISH_LINE_COORDS = (0, 270)
FINISH_LINE = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Scoreboard class inherits from Turtle super class"""
        super().__init__()
        self.score = 1
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.speed(SCORE_SPEED)
        self.update_level()
        self.finish_line()

    def finish_line(self):
        """Displays the finish line at the top of the screen"""
        self.color(FINISH_LINE_COLOR)
        self.goto(FINISH_LINE_COORDS)
        self.write("🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁 Finish Line 🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁",
                   align=SCORE_ALIGN, font=FINISH_LINE)

    def update_level(self):
        """Updates the Player Level"""
        self.color(SCORE_COLOR)
        self.clear()
        self.goto(DISPLAY_COORDS)
        self.write(f"Level: {self.score}", align=SCORE_ALIGN, font=SCORE_FONT)

    def level_up(self):
        """Increments the player level by 1
        after each successfull cross"""
        self.color(SCORE_COLOR)
        self.score += 1
        self.update_level()
        self.finish_line()

    def gameover(self):
        """Displays GameOver and final level"""
        self.color(SCORE_COLOR)
        self.home()
        self.write("G A M E  O V E R", align=SCORE_ALIGN, font=GAME_OVER)
        self.goto(0, -100)
        self.write(f"Final Score: {self.score}",
                   align=SCORE_ALIGN, font=GAME_OVER)
