from turtle import Turtle
import os

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.goto(0,250)
        self.level = 0
        self.score_file = os.path.join(os.path.dirname(__file__), 'scores.txt')
        with open(self.score_file) as file:
            self.highscore = int(file.read())
        self.pl_level()
    
    def pl_level(self):
        self.clear()
        self.write(f'Score: {self.level} High Score: {self.highscore}' ,  move=False, align='center', font=("Courier", 24, "normal"))
    
    def level_up(self):
        self.level += 1
        self.pl_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over' ,  move=False, align='center', font=("Courier", 24, "normal"))
    
    def update_highscore(self):
        if self.level > self.highscore :
            self.highscore = self.level
            with open(self.score_file, mode = 'w') as file :
                file.write(f'{self.highscore}\n')
        self.level = 0
        self.pl_level()