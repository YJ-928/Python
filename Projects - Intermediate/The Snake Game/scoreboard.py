from turtle import Turtle


def fetch_high_score():
    with open("Highscore.txt", "r") as file:
        return file.read()


# Constants
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "bold")
GAMEOVER_FONT = ("Courier", 28, "bold")
SCORE_COLOR = "blue"
SCORE_COORDS = (0, 270)
START_SCORE = 0
HIGH_SCORE = int(fetch_high_score())


class ScoreBoard(Turtle):

    def __init__(self):
        # Inheriting from Turtle Super-Class
        super().__init__()
        self.score = START_SCORE
        self.high_score = HIGH_SCORE
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard by writing new score"""
        self.clear()
        self.goto(SCORE_COORDS)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=SCORE_FONT)

    def game_restart(self):
        """Saves the HighScore to Highscore.txt and resets the score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Highscore.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases score count by 1 at each call"""
        self.score += 1
        # clear the old written score, before writing new updated score
        self.update_scoreboard()
