from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time

#screen settings
screen = Screen()
screen.screensize(600,600)
screen.tracer(0)

player = Player()
score = Scoreboard()

#listener for moving player forward
screen.listen()
screen.onkey(player.move_forward,'Up')

screen.update()

game_continue = True
cars = []
cap = 20

while game_continue:

    #if cap for cars still didnt reach
    if len(cars) < cap:
        new_car = Car()
        new_car.create_car()
        cars.append(new_car)


    for car in cars:

       #check if player is run over by car and end game if true
        if player.distance(car) < 35:
            game_continue = False
            score.game_over()

        #if car is passing the screen get it back from the other side
        if car.xcor() < -400:
            car.random_place()
        car.move()
    screen.update()
    time.sleep(0.1)

    #check if player is passing the upper wall and get the score up
    if player.ycor() > 300:
        score.score_up()

        #after getting to the next round up the cars speed
        for car in cars:
            car.car_speed += 5

        player.goto_start()

screen.exitonclick()