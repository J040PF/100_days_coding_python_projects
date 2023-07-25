from turtle import Screen
from snake import Snake
from score import Score
from food import Food


def back_screen(**setup):
    back = Screen()
    back.title('SNAKE GAME')
    back.colormode(255)
    back.bgcolor('black')
    back.setup(565, 560)
    back.tracer(0)

    return back


food = Food()
u = Snake()
va = 0
s = Score()
s.update(va)


while True:

    back_screen().update()

    x, y = u.snake_move()

    if x == 260 or x == - 260 or y == 260 or y == -260:
        s.game_over()
        break

    aliment = food.food_colision(x, y)

    if aliment:
        u.new_seg()
        va += 1
        s.update(va)
        back_screen().update()

    a = back_screen().listen()

    back_screen().onkey(fun=u.snake_left, key='Left')
    back_screen().onkey(fun=u.snake_right, key='Right')
    back_screen().onkey(fun=u.snake_up, key='Up')
    back_screen().onkey(fun=u.snake_down, key='Down')


back_screen().exitonclick()
