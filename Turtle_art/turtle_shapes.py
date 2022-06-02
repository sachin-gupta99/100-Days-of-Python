import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.setposition((-100.00, 100.00))
my_turtle.clear()
a = 2

for _ in range(8):
    sides = a+1
    angle = int(360/sides)
    r = random.random()
    g = random.random()
    b = random.random()
    my_turtle.pencolor((r, g, b))
    while sides != 0:
        my_turtle.forward(100)
        my_turtle.right(angle)
        sides -= 1

    my_turtle.setposition((-100.00, 100.00))
    my_turtle.setheading(0)
    a += 1

my_screen = turtle.Screen()
my_screen.exitonclick()