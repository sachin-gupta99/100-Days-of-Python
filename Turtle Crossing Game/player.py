import turtle


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto((0, -280))
        self.setheading(90)

    def up(self):
        self.forward(20)
