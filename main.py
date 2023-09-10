import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    # detect collision
    for car in car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


screen.exitonclick()
