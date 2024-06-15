from turtle import Screen
from player import Player

screen = Screen()
screen.screensize(600,600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_forward,'Up')
screen.update()
game_continue = True

while game_continue:
    screen.update()

screen.exitonclick()