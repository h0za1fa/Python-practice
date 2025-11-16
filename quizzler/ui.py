from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title('Quizzler')

        self.score = Label(text='Score: 0', bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(column=2, row=0, pady=20)

        self.question = 'text'
        self.canvas = Canvas()
        self.canvas.grid(column=1, row=1, columnspan=2, padx=50, pady=50)
        self.canvas.config(height=250, width=300)
        self.text = self.canvas.create_text(150, 125, text=self.question,width=280 , font=  ('Arial', 18, 'italic') )
        self.next_question()

        self.true_image = PhotoImage(file='Quizzler/images/true.png')
        self.false_image = PhotoImage(file='Quizzler/images/false.png')

        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=2, row=2, padx=20, pady=20)
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)
    
        self.window.mainloop()

    def next_question(self):
        self.question = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=self.question)

