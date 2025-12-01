import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "creator2282005@gmail.com"
APP_PASSWORD= "vrwv evhm alsb gvof"
RECEIVER ="dream.iit.divyansh@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "HELLO THIS IS PY..."
msg.set_content("this email was shared by python code...")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)
