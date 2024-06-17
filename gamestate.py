from turtle import Turtle
from brick import Brick


class GameState(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 5
        self.start = True
        self.bricks = []
        self.show_lives()

    def show_lives(self):
        self.clear()
        self.goto(360, 280)
        self.write('Lives', align='center', font=('Courier', 10, 'normal'))
        self.goto(360, 230)
        self.write(self.lives, align='center', font=('Courier', 50, 'normal'))

    def lost_live(self):
        self.lives -= 1
        self.show_lives()

    def check_end_game(self):
        if self.lives > 0:
            visible_bricks = [brick for brick in self.bricks if brick.isvisible()]
            if len(visible_bricks) == 0:
                self.start = False
                self.end_game('You Win!')
        else:
            self.start = False
            self.end_game('You Lose!')

    def end_game(self, end_text):
        self.clear()
        self.goto(-0, 0)
        self.write(end_text, align='center', font=('Courier', 60, 'normal'))

    def generate_bricks(self):
        for y in range(100, 250, 50):
            for x in range(-350, 400, 50):
                new_brick = Brick((x, y))
                self.bricks.append(new_brick)



