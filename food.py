from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 270)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 270)
        self.goto(random_x, random_y)

    def disappear(self):
        self.goto(1000, 1000)