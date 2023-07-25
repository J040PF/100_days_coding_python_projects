from data import word_list, stages, logo
import random

word = random.choice(word_list)
word_legth = len(word)
display = []
letterbyplayer = []
stage = 6
game_over = True

s = []

for l in word:
    s.append(l)

if not display:
    for x in range(word_legth):
        display.append('_')

print(logo)

while game_over:
    print(display)

    print(stages[stage])

    player = input('what letter do you want ?? \n').lower()

    for y in range(word_legth):
        if player == word[y]:
            display[y] = player

    if player not in word and player not in letterbyplayer:
        stage -= 1
        if stage == -1:
            game_over = False
            print('game over')

    letterbyplayer.append(player)

    if s == display:
        input('you win')

        game_over = False