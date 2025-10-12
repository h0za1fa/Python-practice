##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib as sm
import letter_templates as lt
import random as rn
import pandas as pd
import datetime as dt

my_gmail = 'hozaifaco@gmail.com'
my_password = ''
letters = [ 'letter_1.txt' , 'letter_2.txt' , 'letter_3.txt' ]

now = dt.datetime.now()
today = now.day
this_month = now.month
# print(today)
# print(this_month )

data = pd.read_csv('bday wisher/birthdays.csv')
data_dict = data.to_dict(orient='records')
# print(data_dict)
for birthday in data_dict:
    if birthday['month'] == this_month and birthday['day'] == today:
        letter = rn.choice(letters)
        with open(f'bday wisher/letter_templates/{letter}') as file:
            text = file.read()
            text = text.replace('[NAME]', birthday['name'])
            # print(text)
        with sm.SMTP('smtp.gmail.com', 587) as connection :
            bday_email = birthday['email']
            connection.starttls()
            connection.login(user=my_gmail ,password=my_password )
            connection.sendmail(from_addr=my_gmail, to_addrs=bday_email, msg=f'subject: Happy Birthday!\n\n{text}')
            # print('sent')