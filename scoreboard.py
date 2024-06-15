from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-340,300)
        self.write(f'Score: {self.score}',align='center',font=('Ariel',15,'normal'))

    def score_up(self):
        self.score +=1
        self.clear()
        self.write(f'Score: {self.score}',align='center',font=('Ariel',15,'normal'))
