from turtle import Turtle
HIGHSCORE = 0
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 50, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("gray30")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 300)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def add_score(self):
        global HIGHSCORE
        self.score += 1
        HIGHSCORE = self.score
        self.clear()
        self.update_scoreboard()
