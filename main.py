import time
from turtle import Screen
from bird import Bird
from colums import Colum
from scoreboard import Scoreboard
from tkinter import *

# class instances
screen = Screen()

# screen config
screen.setup(width=1000, height=800)
screen.bgcolor("white")
screen.bgpic("bg.png")
screen.title("Flappy Bird")

# off animation
screen.tracer(0)
bird = Bird()

# listeners
screen.listen()
screen.onkey(bird.up, "Up")
screen.onkey(bird.down, "Down")
screen.onkey(bird.left, "Left")
screen.onkey(bird.right, "Right")

# after turning off animation, colums and scoreboard will be created without any animation
colums = Colum()
scoreboard = Scoreboard()

# main game point
game_is_on = True
# for adding colums in effective way
controller = 0
# increase speed after getting point
move_speed = 0.1

while game_is_on:
    # screen update
    screen.update()
    time.sleep(move_speed)
    
    # bird gravity
    bird.gravity()

    # extending colums in better way with controller
    if colums.segments[controller][0].xcor() < -500:
        colums.extend_colum()
        controller += 1

    # bird collision with the wall
    if bird.xcor() > 500 or bird.xcor() < -500 or bird.ycor() > 400 or bird.ycor() < -400:
        game_is_on = False
        scoreboard.game_over()


    # bird collision with the colums and update score
    for i in colums.segments:

        # adding score
        if bird.xcor() == i[0].xcor() or bird.xcor() == i[1].xcor():
            scoreboard.add_score()
            move_speed *= 0.95
    
        #detect collision
        if bird.xcor() + 10 > i[0].xcor() - 75 and bird.xcor() - 10 < i[0].xcor() + 50 or bird.xcor() > i[1].xcor() + 10 - 75 and bird.xcor() - 10 < i[1].xcor() + 50:

            if bird.ycor() > i[0].ycor() - 800 or bird.ycor() < i[1].ycor() + 800:
                game_is_on = False
                scoreboard.game_over()

    
    # movement of colums
    colums.movement_colums()

# screen will be closed after clicking on screen
screen.exitonclick()