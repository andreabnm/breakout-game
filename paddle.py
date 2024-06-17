from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(pos[0], pos[1])

    def move_right(self):
        if self.xcor() < 340:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_left(self):
        if self.xcor() > -340:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
