import turtle
import random

turtles = []
color_list = ["white", "indigo", "blue", "green", "gold", "brown", "red"]
offset = 0

s = turtle.Screen()
s.setup(width=500, height=500)
s.bgcolor("moccasin")
s.title("Turtle Race")


for _ in range(6):
    t1 = turtle.Turtle(shape="turtle")
    t1.pu()
    color = random.choice(color_list)
    color_list.remove(color)
    t1.color(color)
    t1.setposition(-240, -70+offset)
    offset += 40
    turtles.append(t1)


def check(timmy):
    if timmy.xcor() > 220:
        return 1
    return 0


user_bet = s.textinput("User\'s bet", "What\'s your bet : ")
winner = 0
while True:
    for tu in s.turtles():
        tu.forward(random.randint(1, 10))

    result = list(map(check, s.turtles()))
    if 1 in result:
        winner = result.index(1)
        break

winner = turtles[winner].color()[0].capitalize()

if user_bet == winner:
    print('You won the bet')
else:
    print('You lost')


print(winner + " turtle won the race")

s.exitonclick()

