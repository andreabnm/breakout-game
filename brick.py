from turtle import Turtle
import random


class Brick(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape('square')

        random_int = random.randint(1, 4)
        if random_int == 1:
            self.color('red')
        elif random_int == 2:
            self.color('blue')
        elif random_int == 3:
            self.color('yellow')
        elif random_int == 4:
            self.color('green')

        self.shapesize(stretch_wid=1, stretch_len=random.randint(1, 2))
        self.goto(pos[0], pos[1])
