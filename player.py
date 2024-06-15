from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0,-300)

    def move_forward(self):
        self.forward(15)