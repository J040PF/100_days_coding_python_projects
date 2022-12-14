import random

p = "paper"
s = "stone"
sc = "scissor"

list = ["paper", "stone", "scissor"]
w_l = {p: [s], s: [sc], sc: [p]}

while True:

    player = input("what do you want ?..."
                   "paper stone scissor\n")
    machine = random.choice(list)

    print('you : {} - machine:{}'.format(player, machine))

    if machine == player:
        print('draw')       
    elif w_l[player][0] == machine:
        print('you win')
    elif w_l[machine][0] == player:
        print('you loss')
