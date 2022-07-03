import turtle

FONT = ('Times New Roman', 20, 'bold')


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.pu()
        self.goto((-300, 270))
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="right", font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write(f"Game Over", align="center", font=FONT)
