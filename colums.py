from turtle import Turtle
from random import randint

TOP1 = randint(600, 1200)
BOTTOM1 = TOP1 - 800 - 200 - 800

TOP2 = randint(600, 1200)
BOTTOM2 = TOP2 - 800 - 200 - 800

TOP3 = randint(600, 1200)
BOTTOM3 = TOP3 - 800 - 200 - 800

TOP4 = randint(600, 1200)
BOTTOM4 = TOP4 - 800 - 200 - 800

STARTING_POSITION = [[(500, TOP1),(500, BOTTOM1)],[(900, TOP2), (900, BOTTOM2)],[(1300, TOP3), (1300, BOTTOM3)],[(1700, TOP4), (1700, BOTTOM4)]]


class Colum():
    def __init__(self):
        self.segments = []
        self.colum_add()
        

    def colum_add(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment1 = Turtle("square")
        new_segment2 = Turtle("square")

        new_segment1.penup()
        new_segment2.penup()

        # color config
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255) 


        new_segment1.color("SpringGreen4")
        new_segment2.color("SpringGreen4")

        new_segment1.goto(position[0][0], position[0][1])
        new_segment2.goto(position[1][0], position[1][1])


        new_segment1.shapesize(80, 5)
        new_segment2.shapesize(80, 5)


        self.segments.append([new_segment1, new_segment2])

    def extend_colum(self):
        TOP = randint(600, 1200)
        BOTTOM = TOP - 800 - 200 - 800
        self.add_segment([(self.segments[-1][0].xcor() + 400, TOP),(self.segments[-1][1].xcor() + 400, BOTTOM)])    


    def movement_colums(self):
        for i in self.segments:
            xcor_segment1 = i[0].xcor()
            xcor_segment2 = i[1].xcor()
            i[0].goto(xcor_segment1 - 10, i[0].ycor())
            i[1].goto(xcor_segment2 - 10, i[1].ycor())   

   