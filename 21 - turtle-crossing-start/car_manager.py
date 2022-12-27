import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.cars_generator()

    def random_Car(self):
        self.penup()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y = random.randint(-200, 200)
        self.x = 200
        r_init = random.randint(-200, 200)
        self.goto(self.x + r_init, self.y)

    def car_move(self):
        global MOVE_INCREMENT, STARTING_MOVE_DISTANCE
        x = self.xcor() - MOVE_INCREMENT
        self.goto(x, self.ycor())

    def cars_generator(self):
        for t in range(0, 10):
            self.Car = self.random_Car()
            self.cars.append(self.Car)