
# This code was written for the purpose of sending loud emails at 
#the end of compiling a python code. To generate I followed the 
#security settings from the link below. You may need to do the 
#same if you run it on another computer or in another email.

#https://realpython.com/python-send-email/

your_email = "your_email@gmail.com"

import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email =  "sender_email@gmail.com" # Enter your address
receiver_email = your_email  # Enter receiver address
password = input("write your password")
message = """\
Subject:[COSMOSERVER] Results Ready!

Congratulations your code has finished running!

cosmoserver
Bingo Collaboration
National Institute for Space Research"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
