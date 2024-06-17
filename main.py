from turtle import Screen
from paddle import Paddle
from ball import Ball
from gamestate import GameState
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title('Breakout')

paddle = Paddle((0, -260))
ball = Ball()
gs = GameState()
gs.generate_bricks()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

while gs.start:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with a wall
    # upper wall
    if ball.ycor() > 280:
        ball.bounce_y()
    # left and right wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -245:
        ball.bounce_y()

    # detect collision with a brick
    for brick in gs.bricks:
        if brick.isvisible():
            if ball.distance(brick) < 30:
                brick.hideturtle()
                ball.bounce_y()

    # detect out of bounds
    if ball.ycor() < -300:
        gs.lost_live()
        ball.reset_position()

    gs.check_end_game()

screen.exitonclick()
