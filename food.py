import turtle as t
import random


class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        """
        Inherit from turtle class and randomly create the food spot on the screen 
        """
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # normal size is 20*20, now it shrinks to 10*10
        self.color('blue')
        self.speed('fastest')

        self.refresh()  # create random position

    def refresh(self):
        """
        Once the snake head collided with the food, randomly create a new location for the food.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


