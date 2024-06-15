from turtle import Screen
from player import Player
from scoreboard import Scoreboard
screen = Screen()
screen.screensize(600,600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.move_forward,'Up')
screen.update()
game_continue = True

while game_continue:
    screen.update()
    if player.ycor() > 300:
        score.score_up()
        player.goto_start()

screen.exitonclick()