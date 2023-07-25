import pandas
from turtle import Screen, Turtle

writer = Turtle()
writer.penup()
writer.hideturtle()
data = pandas.read_csv('25 - US_states_game/50_states.csv')

screen = Screen()
screen.setup(725, 491)
screen.bgpic('25 - US_states_game/blank_states_img.gif')
game_is_on = True
phase = 0
n = len(data)


def state_pos(state):
    global game_is_on, phase

    try:

        state = str(state)
        state = state.title()
        is_in = data[data['state'] == state]
        x_w = int(is_in['x'])
        y_w = int(is_in['y'])
        writer.goto(x_w, y_w)
        writer.write(state, font=('arial', 5, 'bold'))
        if x_w:
            phase += 1

    except:

        if state == 'Exit':
            game_is_on = False
        else:
            print('Try again')
            pass


while game_is_on:

    state = screen.textinput('{}/{}'.format(phase, n), 'Guess a State')
    state_pos(state)
    screen.update()