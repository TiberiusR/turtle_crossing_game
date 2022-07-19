from turtle import Turtle
import random

COLORS = ["Red", "Blue", "Yellow", "Black", "Green", "Pink", "Orange"]
STARTING_MOVE_SPEED = 5
SPEED_INCREMENT = 5


class Car:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_SPEED

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += SPEED_INCREMENT
