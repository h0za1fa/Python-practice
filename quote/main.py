import smtplib
import random
import datetime

with open('quote/quotes.txt') as file :
    quotes = file.readlines()
    quote = random.choice(quotes)

with open('quote/mails.txt') as file:
    emails = file.readlines()

my_gmail = 'hozaifaco@gmail.com'
my_password = ''

now = datetime.datetime.now()

for mail_id in emails :
    with smtplib.SMTP('smtp.gmail.com', 587) as connection :
        connection.starttls()
        connection.login(user=my_gmail, password=my_password)

        connection.sendmail(from_addr=my_gmail, to_addrs=mail_id, msg=f'subject: Wakey Wakey\n\n{quote}')
