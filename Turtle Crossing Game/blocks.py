import random
import turtle

COLORS = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
MOVING_DISTANCE = 5
INCREMENT = 10


class Block(turtle.Turtle):
    moving_distance = MOVING_DISTANCE

    def __init__(self):
        self.blocks = []

    def create_block(self):
        new_block = turtle.Turtle("square")
        new_block.pu()
        new_block.shapesize(1,2)
        new_block.setheading(180)
        new_block.color(random.choice(COLORS))
        new_block.goto(380, random.randint(-250, 250))
        self.blocks.append(new_block)

    def move(self):
        for block in self.blocks:
            block.forward(Block.moving_distance)

    def increase(self):
        Block.moving_distance += INCREMENT

    def check(self, player):
        for block in self.blocks:
            if block.distance(player) < 20:
                return True
        return False
