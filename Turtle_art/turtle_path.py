import turtle
import random

my_turtle = turtle.Turtle()
directions = [0, 90, 180, 270]

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = []
    color.extend((r, g, b))
    return tuple(color)


my_turtle.width(10)
my_turtle.speed(10)

for _ in range(200):
    my_turtle.pencolor(random_color())
    my_turtle.setheading(random.choice(directions))
    my_turtle.forward(30)

my_screen = turtle.Screen()
my_screen.exitonclick()
