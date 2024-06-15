from turtle import Turtle
import random
COLORS = ['yellow','blue', 'red']
class Car(Turtle):
    def __init__(self):
        super().__init__()

    def create_car(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.shape('square')
        self.speed('fastest')
        self.setheading(180)
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.goto(random.randint(350, 450), random.randint(-250, 280))


    def move(self):
        self.forward(5)

    def random_place(self):
        self.goto(random.randint(350, 450), random.randint(-250, 280))


