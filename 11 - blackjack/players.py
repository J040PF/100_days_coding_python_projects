import random


class Player:

    def __init__(self):
        self.score = 0

    def random_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        self.score += card

    def delear_brain(self, pla):
        response = []

        if pla.score >= self.score and response == []:
            return 1

        elif 15 >= self.score <= 21:
            response.append(0)
            return 0

    def anwser(self,user , dealer):
        playerson = []
        u = []
        d = []
        u.append(user)
        d.append(dealer)
        test = [u, d]

        for h in test:
            if h[-1] == 0:
                pass