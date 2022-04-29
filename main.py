import pandas as pd
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import sender_email, sender_password
import message as Message

data = pd.read_excel('mail.xlsx')

email_col = data.get('email')
emails = email_col.tolist()
print(emails)

try:
    server = smtp.SMTP_SSL('smtp.gmail.com', 465)
    server.starttls
    server.login(sender_email, sender_password)
    from_ = sender_email
    to_ = emails

    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Return 0 HackerRank Contest (Reminder)"
    msg['From'] = from_

    html = Message.HTML_MESSAGE

    text = MIMEText(html, 'html')

    msg.attach(text)

    server.sendmail(from_, to_, msg.as_string())
    print("Email sent successfully")
    server.quit()

except Exception as e:
    print(e)
