import time
import turtle
from player import Player
from blocks import Block
from score import Score

turtle.tracer(0)

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("beige")

player = Player()
score = Score()
blocks = Block()

screen.listen()
screen.onkeypress(player.up, "Up")

game = True
loop = 0
sleep_time = 0.1
while game:
    time.sleep(sleep_time)
    turtle.update()
    if loop == 3:
        blocks.create_block()
        loop = 0

    blocks.move()

    collided = blocks.check(player)
    if collided:
        score.game_over()
        game = False
        break
    if player.ycor() > 280:
        score.level += 1
        score.display_level()
        sleep_time *= 0.7
        player.goto((0, -280))
    loop += 1

screen.exitonclick()
