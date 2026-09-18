import smtplib
from email.message import EmailMessage
sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "passkey"
# 1. Create a file containing prime numbers from 2 to 100
with open("prime_numbers.txt", "w") as file:
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            file.write(str(num) + "\n")

# 2. Create the email
msg = EmailMessage()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Prime Numbers"
msg.set_content("""Hi,
Please find the prime numbers from 2 to 100 attached.

Thanks & Regards,
Nandini Yannagiri
""")
# 3. Attach the file
with open("prime_numbers.txt", "rb") as file:
    file_data = file.read()
msg.add_attachment(
    file_data,
    maintype="text",
    subtype="plain",
    filename="prime_numbers.txt"
)
# 4. Send the email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.send_message(msg)
server.quit()
print("Mail sent successfully with attachment!")
