from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
STARTING_POS = (-240, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(STARTING_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def score_print(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()