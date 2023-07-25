import random

number = None

def user(msg):
    while True:
        try:
            aw = input(msg)
            if aw == "yes":
                break
            elif aw == 'no':
                print('stoping game')
                break
            else:
                print('you dont give the awnser Try again')
        except:
            pass

def random_n():
    global number
    n = (random.random())*100
    n = round(n)
    number = n

    print(n)

def guess_user(msg):
    global number

    def comp_number(n):

        if n == number:
            return 'you win'
        elif n > number:
            print('your number is highter ')
            return n
        else:
            print('your number is lower')
            return n
    guess = []
    while True:

        try:
            g = int(input(msg))
            dec = comp_number(g)

            if dec == 'you win':
                return print('you pit is right')
            else:
                guess.append(dec)
                print(guess)

        except:
            print('please give a number')

user('do you wanna play a guess game')
random_n()
guess_user('guess a number')