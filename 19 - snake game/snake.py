from turtle import Turtle

position_shape = [(0, 0), (-20, 0), (-40, 0)]
vel = 5


class Snake():

    def __init__(self):

        self.segments = []
        self.snake_shape()
        self.head = self.segments[0]

    def snake_shape(self):

        for position in position_shape:
            self.snake = Turtle()
            self.snake.penup()
            self.snake.color('white')
            self.snake.shape('square')
            self.snake.goto(position)
            self.segments.append(self.snake)

    def snake_up(self):

        if self.head.heading() != 270.0:
            self.segments[0].setheading(90)

    def snake_down(self):

        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def snake_right(self):

        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def snake_left(self):

        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def snake_move(self):

        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(vel)
        return self.head.xcor(), self.head.ycor()

    def new_seg(self):
        self.snake = Turtle()
        self.snake.penup()
        self.snake.goto(self.segments[-1].pos())
        self.snake.color('white')
        self.snake.shape('square')
        self.segments.append(self.snake)