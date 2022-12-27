import random


dealer = []
player = []


def random_cands():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card


def check_value():
    player_score = sum(player)
    dealer_score = sum(dealer)
    print( 'player= {} , dealer = {}'.format(player_score, dealer_score))

    def under_21():
        if player_score > 21:
            print(input('dealer win'))

        elif dealer_score > 21:
            print(input('player win'))

    if player_score > 21 or dealer_score > 21:
        under_21()


def get_card(*p):
    de = [p]

    for y in de[0]:
        try:
            y.append(random_cands())
        except:
            pass


while True:
    check_value()

    user_anwser = int(input('do you want take a card.. 1/0 '))

    if user_anwser == 1:

        while True:
            check_value()
            get_card(dealer)

    else:
        get_card(player, dealer)





