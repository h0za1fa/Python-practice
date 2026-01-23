import tkinter as tk
import math as mt

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset() :
    global reps
    checkmarks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text='Timer',fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    mins = 0
    reps += 1
    if reps == 8 :
        mins = LONG_BREAK_MIN
        timer_label.config(text='Break',fg=GREEN)
    elif reps % 2 == 0 :
        mins = SHORT_BREAK_MIN
        timer_label.config(text='Break',fg=GREEN)
    else :
        mins = WORK_MIN
        timer_label.config(text='Work',fg=RED)
    canvas.itemconfig(timer_text)
    count_down(mins * 60)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):   
    count_min = mt.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10 :
        count_sec = f'0{count_sec}'
    if count_sec == 0 :
        count_sec = '00'
    
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0 :
        global timer
        timer = window.after(1000,count_down, count-1)
    else :
        start_timer()
        
        if reps % 2 == 1 :
            checks = ''
            for _ in range(mt.floor(reps/2)) :
                checks += '✔'
            checkmarks.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg= YELLOW)

canvas = tk.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image = tk.PhotoImage(file = 'tomato.png')
canvas.create_image(100,112,image=image)

timer_text = canvas.create_text(100,130, text='00:00',fill='white', font=(FONT_NAME,24,'bold'))
canvas.grid(row=2,column=2)

timer_label = tk.Label(text = 'Timer', font=(FONT_NAME,40,'bold'), fg=GREEN , bg=YELLOW)
timer_label.grid(row=1,column=2)

start_button = tk.Button(text='Start', command=start_timer)
start_button.grid(row=3,column=1)

reset_button = tk.Button(text='Reset', command=reset)
reset_button.grid(row=3,column=3)

checkmarks = tk.Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(row=4,column=2)

window.mainloop()