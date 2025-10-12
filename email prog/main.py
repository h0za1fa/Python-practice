import smtplib

my_email = 'hozaifaco@gmail.com'
my_password = '12345678'

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs='amashkh198@gmail.com', msg='subject: test message\n\nspeeling')

connection.close()