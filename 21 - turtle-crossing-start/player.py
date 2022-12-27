from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 180


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.passo = 10

    def move_up(self):
        self.goto(self.xcor(), (self.ycor()+self.passo))

    def move_down(self):
        self.goto(self.xcor(), (self.ycor() - self.passo))

    def next_phase(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

