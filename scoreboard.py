import turtle as t

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write('Score: {}'.format(self.score), move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()  # to clear the previous score and write the new score
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=('Courier', 40, 'bold'))
