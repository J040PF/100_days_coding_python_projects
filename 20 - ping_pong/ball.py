import time
from turtle import Turtle
import random

class BallGame(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.shape('circle')
        self.penup()
        self.x = 0.1
        self.y = 0.1

    def move_ball(self):

        if self.ycor() > 200 or self.ycor() < -200:
            self.y *= -1

        self.x_position = self.xcor() + self.x
        self.y_position = self.ycor() + self.y

        self.goto(self.x_position, self.y_position)

    def bounce_paddle(self, ny, y2):
        if self.xcor() >= 265 and self.distance(ny) < 20 \
                or self.xcor() <= -265 and self.distance(y2) <20:
            self.x *= -1








