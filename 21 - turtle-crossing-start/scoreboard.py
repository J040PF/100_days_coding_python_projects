from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_write()

    def att_score(self):
        global SCORE
        self.clear()
        SCORE += 1

    def line(self):
        self.goto(-300, 200)
        self.pendown()
        self.goto(300, 200)
        self.penup()
        self.goto(-300, -250)
        self.pendown()
        self.goto(300, -250)
        self.penup()

    def score_write(self):
        self.hideturtle()
        self.penup()
        self.goto(-280, 200)
        self.write('Score : {}'.format(SCORE), font=FONT)
        self.line()

    def game_over(self):
        self.goto(-50,0)
        self.write('Game Over', font=FONT)