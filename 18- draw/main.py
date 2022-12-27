from turtle import Turtle, Screen
from data import color_data
import random

def user(color, **speed):
    tut = Turtle()
    speed = 1
    tut.hideturtle()
    tut.penup()
    tut.goto(-250, -250)

    return tut


def back_screen(**setup):
    back = Screen()
    back.colormode(255)
    back.setup(565, 560)

    return back


def path(ball):
    for y in range(-250, 260, 50):
        for x in range(-250, 260, 50):
            cr = random.choice(color_data)
            ball.goto(x, y)
            ball.dot(40, cr)

tt = user(color_data[10])
sc = back_screen()
path(tt)
print(len(color_data))
