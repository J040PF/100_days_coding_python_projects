import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
acellerator = 0.1

game_is_on = True


def up():
    player.move_up()


def down():
    player.move_down()


score = Scoreboard()
cars = []

for t in range(0, 10):
    Car = CarManager()
    cars.append(Car)

while game_is_on:

    for carro in cars:
        carro.car_move()

    screen.listen()
    screen.onkey(up, 'Up')
    screen.onkey(down, 'Down')

    if player.ycor() == 180:
        score.att_score()
        score.score_write()
        player.next_phase()
        acellerator *= 0.9

    time.sleep(acellerator)

    for last in cars:
        if last.distance(player) < 20:
            score.game_over()
            time.sleep(2)
            game_is_on = False

        x_ran = random.randint(600, 800)
        y_ran = random.randint(-230, 180)

        if last.xcor() <= - 300:
            last.goto(last.xcor() + x_ran, y_ran)

    screen.update()
