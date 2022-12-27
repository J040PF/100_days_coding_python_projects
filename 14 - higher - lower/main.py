from game_data import data
import random

sc = 0


def random_selec():

    option = []

    for x in range(0, 2):
        n = random.choice(data)
        if n not in option:
            option.append(n)
        else:
            while True:
                r = random.choice(data)
                if r not in option:
                    option.append(n)
                    break

    return option


def score():
    list = random_selec()
    op1 = list[0]
    op2 = list[1]

    name = op1['name']
    des = op1['description']
    f = op1['follower_count']
    fro = op1['country']

    name2 = op2['name']
    des2 = op2['description']
    f2 = op2['follower_count']
    fro2 = op2['country']

    print('{}, {} from {}'.format(name, des, fro))
    print('vs')
    print('{}, {} from {}'.format(name2, des2, fro2))

    if f2 > f:
        return 2
    else:
        return 1


def check(us, re):
    global sc

    if us == re:
        sc += 1
    else:
        print('You loss')
        return 'loss'


def main():

    global sc
    while True:

        try:
            print('Your score is {}\n'.format(sc))
            s = int(score())

            user_awnser = int(input('who have the highest numbers of follower??\n'))
            c = check(user_awnser, s)
            if c == 'loss':
                print('you loss , your score is ...\n {}'.format(sc))
                break

        except:
            print('you dont give any awnser, try again')


main()
