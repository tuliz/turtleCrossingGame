from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time
screen = Screen()
screen.screensize(600,600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.move_forward,'Up')
screen.update()
game_continue = True
cars = []
cap = 20

while game_continue:
    if len(cars) < cap:
        new_car = Car()
        new_car.create_car()
        cars.append(new_car)
    for car in cars:
        if player.distance(car) < 38:
            game_continue = False
            score.game_over()
        if car.xcor() < -400:
            car.random_place()
        car.move()
    screen.update()
    time.sleep(0.1)
    if player.ycor() > 300:
        score.score_up()
        player.goto_start()

screen.exitonclick()