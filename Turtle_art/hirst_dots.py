import turtle
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    return color


t = turtle.Turtle()
t.penup()
t.hideturtle()
t.setposition((-200.00, 200.00))
t.speed("fastest")


def decide_direction(flag):
    if flag:
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
    else:
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(40)


def draw_next_dot(t):
    t.dot(20, random_color())
    t.forward(40)


flag = True
for _ in range(10):
    for _ in range(10):
        draw_next_dot(t)
    decide_direction(flag)
    flag = False if flag else True

t.hideturtle()

s = turtle.Screen()
s.exitonclick()
