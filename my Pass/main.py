import tkinter as tk
from tkinter import messagebox
import random
import pyperclip as pyc
import json

email = 'YOUR_EMAIL_HERE'

# ---------------------------- SEARCH ------------------------------- #

def search():
    web = website_entry.get()
    try:
        with open('my Pass/data.json') as file :
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Erroe',message='File not found!')
    else:
        if web in data :
            details = data[web]
            password = details['password']
            mail = details['email']
            pyc.copy(password)
            messagebox.showinfo(title='Details', message=f'Email: {mail}\nPassword: {password}')
        else:
            messagebox.showerror(title='Error', message=f'{web} is not saved')
    finally:
        website_entry.delete(0, tk.END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    
    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_data():
    web = website_entry.get()
    mail = email_entry.get()
    pasw = password_entry.get()
    data = {
        web: {
            'email': mail,
            'password': pasw
        } 
    }
    if web == '' or mail == '' or pasw == '' :
        messagebox.showerror(title='Error', message = 'Please fill all the details!')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'You entered:\nwebsite: {web}\nemail: {mail}\npassword: {pasw}')
        if is_ok :
            try:
                with open('my pass/data.json', mode='r') as file :
                    existing_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                with open('my pass/data.json', mode='w') as file :
                    json.dump(data, file, indent=4)
            else:
                existing_data.update(data)
                with open('my pass/data.json', mode='w') as file :
                    json.dump( existing_data, file, indent=4 )
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            pyc.copy(pasw)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=50,pady=50)

image = tk.PhotoImage(file='my Pass/logo.png')
logo_canvas = tk.Canvas(width=200,height=200)
logo_canvas.create_image(100,100,image=image)
logo_canvas.grid(row=1,column=2)

website_label = tk.Label(text='website:')
website_label.grid(row=2,column=1)

email_label = tk.Label(text='Email/Username:')
email_label.grid(row=3,column=1)

password_label = tk.Label(text='Password:')
password_label.grid(row=4,column=1)

website_entry = tk.Entry(width=33)
website_entry.focus()
website_entry.grid(row=2, column=2)

email_entry = tk.Entry(width=43)
email_entry.insert(0,email)
email_entry.grid(row=3, column=2, columnspan=3)

password_entry = tk.Entry(width=33)
password_entry.grid(row=4,column=2, padx=0)

generate_button = tk.Button(text='Generate', padx=0, command=generate_password)
generate_button.grid(row=4,column=3, padx=0)

add_button = tk.Button(text='Add' , width=36, command=write_data)
add_button.grid(row=5,column=2,columnspan=3)

search_button = tk.Button(text='Search', padx=0, width=7 , command=search)
search_button.grid(row=2,column=3, padx=0)

window.mainloop()