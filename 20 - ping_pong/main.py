import time
from turtle import Screen
from ball import BallGame
from paddles import Paddles


def screen():

    tela = Screen()
    tela.setup(600, 500)
    tela.colormode(255)
    tela.bgcolor('black')
    tela.title('Ping Pong')
    tela.tracer(0)
    return tela


tela_game = screen()
padle = Paddles()
ba = BallGame()

tela_game.listen()

tela_game.onkey(fun=padle.padle_up, key="Up")
tela_game.onkey(fun=padle.padle_down, key='Down')
tela_game.onkey(fun=padle.padle_up_s, key="w")
tela_game.onkey(fun=padle.padle_down_s, key='s')

while True:
    ba.move_ball()
    ba.bounce_paddle(padle.pade_rigth, padle.pade_left)
    tela_game.update()


tela_game.exitonclick()