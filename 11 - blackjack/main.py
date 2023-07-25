import random


dealer = []
player = []


def random_cards():
    # return a random card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card


def check_value():
    # check if the value is under 21
    player_score = sum(player)
    dealer_score = sum(dealer)
    print( 'player= {} , dealer = {}'.format(player_score, dealer_score))

    def under_21():

        if player_score > 21:
            print(input('dealer win'))
            return False

        elif dealer_score > 21:
            print(input('player win'))
            return False
        
        else:
            return True

    if player_score > 21 or dealer_score > 21:
         return under_21()


def get_card(*player):
    de = [player]

    for y in de[0]:
        try:
            y.append(random_cards())
        except:
            pass


def main():

    while True:
        if check_value() is False:
            break

        user_anwser = str(input('Do you want take a card.. n/y '))

        if user_anwser == "n":

            while True:
                if check_value() is False:
                    break
                get_card(dealer)

        else:
            get_card(player, dealer)

main()




