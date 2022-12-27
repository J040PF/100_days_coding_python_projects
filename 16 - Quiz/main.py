from quiz import Quiz
import data


print('{}\n'
      'Welcome to the show quiz\n'
      '{}'.format((50*'-'), (50*'-')))

option = input('do you wanna play a game ?\n')

if option == 'y':
    ini = Quiz(data.question_data)
    while ini.on:
        ini.score_game()

    print('Your score is : {}'.format(ini.score))

