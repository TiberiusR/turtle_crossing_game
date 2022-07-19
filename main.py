from turtle import Screen
from crosser import Crosser
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

crosser = Crosser()
scoreboard = Scoreboard()
car = Car()

screen.listen()
screen.onkey(crosser.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for c in car.all_cars:
        if crosser.distance(c) < 15:
            game_is_on = False
            scoreboard.game_over()

    if crosser.ycor() > 275:
        scoreboard.score_print()
        crosser.reset_pos()
        car.increase_speed()


screen.exitonclick()
