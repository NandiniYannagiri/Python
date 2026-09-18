import smtplib

sender = "sender@gmail.com"
password = "passkey"

contacts = [
    {"name": "user1_name", "email": "user1@gmail.com"},
    {"name": "user2_name", "email": "user2@gmail.com"},
    {"name": "user3_name", "email": "user3@gmail.com"},
]

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

for contact in contacts:

    msg = f"""Hi {contact["name"]},

Hope you are doing well.

I am very excited to share this news with you.
I have just learnt how to send emails using Python.

Thanks & Regards,
Nandini Yannagiri
"""

    server.sendmail(sender, contact["email"], msg)
    print(f"Mail sent to {contact['email']}")

server.quit()

print("All emails sent successfully!")
