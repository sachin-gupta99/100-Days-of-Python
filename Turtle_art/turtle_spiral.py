import turtle
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = []
    color.extend((r, g, b))
    return tuple(color)


t = turtle.Turtle()
t.speed("fastest")


def spirograph(density):

    for _ in range(int(360/density)):
        t.pencolor(random_color())
        t.circle(100)
        t.setheading(density+t.heading())

spirograph(1)


s = turtle.Screen()
s.exitonclick()