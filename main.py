from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()
scoreboard = Scoreboard()
bricks = Bricks()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    ball.move()
    ball.detect_wall_collision()

    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_y()

    if bricks.detect_collision(ball):
        ball.bounce_y()
        ball.move_speed += 0.1
        scoreboard.increase_score()

    if ball.ycor() < -280:
        game_on = False
        scoreboard.game_over()


screen.mainloop()


