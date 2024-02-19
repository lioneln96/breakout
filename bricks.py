from turtle import Turtle
import random

class Bricks:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        brick_width = 100
        brick_height = 25

        start_x = -350
        start_y = 250

        for _ in range(7):
            for _ in range(7):
                brick = Turtle("square")
                brick.shapesize(stretch_wid=1, stretch_len=4)
                brick.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
                brick.penup()
                brick.goto(start_x, start_y)
                self.bricks.append(brick)
                start_x += brick_width + 10
            start_x = -350
            start_y -= brick_height + 10

    def detect_collision(self, ball):
        for brick in self.bricks:
            if brick.distance(ball) < 20:
                self.bricks.remove(brick)
                brick.hideturtle()
                return True
        return False


