from data import logo

print(logo)

players = {}


def checkwinner():
    global players
    lu = []
    listbids = []
    for x in players:
        lu.append(x)
        listbids.append(players[x])
    if len(lu) > 1:
        winner = max(listbids)
        w = listbids.index(winner)
        print(lu[w])
    else:
        print(lu[0])


while True:

    new_player = input('someone has a beat...')
    if new_player == 'yes':
        name = input('whats you name ')
        bid = int(input('whats you bid'))
        players[name] = bid
    else:
        print('auction finished')
        checkwinner()
        break