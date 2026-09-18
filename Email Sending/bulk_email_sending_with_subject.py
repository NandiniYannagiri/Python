import smtplib
from email.message import EmailMessage
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
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = contact["email"]
    msg["Subject"] = f"Hello {contact['name']}!"
    message = f"""Hi {contact["name"]},

Hope you are doing well.

I am very excited to share this news with you.
I have just learnt how to send emails using Python
and I am very interested in learning new things ahead.

Thanks & Regards,
Nandini Yannagiri
"""
    msg.set_content(message)
    server.send_message(msg)
    print(f"Mail sent to {contact['email']}")
server.quit()
print("All emails sent successfully!")