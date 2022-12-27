from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5)
        self.shape('circle')
        self.color('blue')
        self.hideturtle()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)
        self.showturtle()

    def food_colision(self, x , y):
        x_co = self.xcor()
        y_co = self.ycor()
        x1 = x_co + 15
        x2 = x_co - 15
        y1 = y_co + 15
        y2 = y_co - 15

        if x1 > x > x2 and y1 > y > y2:
            xa = random.randint(-250, 250)
            ya = random.randint(-250, 250)
            self.goto(xa, ya)
            return True
