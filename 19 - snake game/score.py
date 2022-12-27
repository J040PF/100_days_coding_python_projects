from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.pendown()

    def update(self, va):
        self.clear()
        self.write(arg=va, move=False, align='center', font=('Arial', 10, 'bold'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        go = 'Game Over'
        self.write(arg=go, move=False, align='center', font=('Arial', 15, 'bold'))

