from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.goto(0,250)
        self.level = 0
        with open('scores.txt') as file:
            self.highscore = int(file.read())
    
    def pl_level(self):
        self.clear()
        self.write(f'Score: {self.level} High Score: {self.highscore}' ,  move=False, align='center', font=("Courier", 24, "normal"))
    
    def level_up(self):
        self.level += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over' ,  move=False, align='center', font=("Courier", 24, "normal"))
    
    def update_highscore(self):
        if self.level > self.highscore :
            self.highscore = self.level
            with open('snake game\scores.txt' , mode = 'w') as file :
                file.write(f'{self.highscore}\n')
        self.level = 0
        self.pl_level()