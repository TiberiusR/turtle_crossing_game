from turtle import Turtle

STARTING_POS = (0, -270)
MOVE_DISTANCE = 20


class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.seth(90)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POS)
