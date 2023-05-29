from turtle import Turtle

class Bird(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark orange")
        self.shapesize(2)
        self.penup()
        self.goto(-400, 0)

    def gravity(self): 
        ycor = self.ycor() - 10
        self.goto(self.xcor(), ycor)

    def up(self): 
        ycor = self.ycor() + 35
        self.goto(self.xcor(), ycor)

    def down(self): 
        ycor = self.ycor() - 10
        self.goto(self.xcor(), ycor)

    def left(self):
        xcor = self.xcor() - 10
        self.goto(xcor, self.ycor()) 

    def right(self): 
        xcor = self.xcor() + 10
        self.goto(xcor, self.ycor())                    


  
