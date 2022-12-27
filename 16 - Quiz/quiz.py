import random


class Quiz:

    def __init__(self, data):
        self.quiz = data
        self.score = 0
        self.on = True

    def check_answer(self, user, answer):
        if user == answer:
            self.score += 1
        else:
            self.on = False

    def question_answer(self):
        question = random.choice(self.quiz)
        question_text = question['text']
        question_answer = question['answer']
        print('{}\n{}'.format(question_text, '-'*50))
        user_answer = (input('This is True or False')).title()

        self.check_answer(user_answer, question_answer)


    def score_game(self):
        print('Your score is : {}\n'
              '{} '.format(self.score, (50*'-')))
        game_on = self.question_answer()
        if game_on is False:
            return False



