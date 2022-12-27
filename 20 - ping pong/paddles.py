from turtle import Turtle

paddl = [(280, 0), (-280, 0)]


class Paddles():

    def __init__(self):
        self.padle()
        self.padd1 = self.pade[1]

    def padle(self):

        self.pade = []

        for x in paddl:
            self.padlee = Turtle()
            self.padlee.penup()
            self.padlee.goto(x)
            self.padlee.color('white')
            self.padlee.shape('square')
            self.padlee.shapesize(3, 0.5)
            self.pade.append(self.padlee)

        self.pade_rigth = self.pade[0]
        self.pade_left = self.pade[1]

    def padle_up(self):
        self.pr = self.pade[0]
        x = self.pr.xcor()
        y = self.pr.ycor()
        self.pr.goto(x, y+30)

    def padle_down(self):
        self.pr = self.pade[0]
        x = self.pr.xcor()
        y = self.pr.ycor()
        self.pr.goto(x, y - 30)

    def padle_up_s(self):
        self.pr = self.pade[1]
        x = self.pr.xcor()
        y = self.pr.ycor()
        self.pr.goto(x, y+30)

    def padle_down_s(self):
        self.pr = self.pade[1]
        x = self.pr.xcor()
        y = self.pr.ycor()
        self.pr.goto(x, y - 30)
