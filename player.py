from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)













