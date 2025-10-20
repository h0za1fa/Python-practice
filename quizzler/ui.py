THEME_COLOR = "#375362"
import tkinter

class QuizUi:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        
        self.question = tkinter.Canvas()
        self.question.config(height=250, width=300)
        self.question.grid(row=1,column=1 ,columnspan=2, padx=50,pady=50)

        true = tkinter.PhotoImage('images/true.png')
        false = tkinter.PhotoImage('images/false.png')
        self.true = tkinter.Button(image=true) 
        self.true.grid(row=2,column=1)
        self.false = tkinter.Button(image=false)
        self.false.grid(row=2,column=2) 


        self.window.mainloop()