import smtplib
sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "passkey"
msg = """Hi dear
Hope you are doing well. I am very excited to share this news with you.
I have just learnt to how to send an Email using python built-in modules and functions
and i am very intrested to learn new things ahead.

Thanks & Regard,
Nandini Yannagiri"""
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,msg)
server.quit()
print("Mail Sent Successfully!")