import os
from pathlib import Path
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

# Get path to the root directory (one level above src/)
root_dir = Path(__file__).resolve().parent.parent
dotenv_path = root_dir / ".env"

load_dotenv(dotenv_path)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587 

def send_email(subject, message, to=EMAIL_RECEIVER):
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


"""
if __name__ == "__main__":
    send_email(
        subject="Tennis Match Alert 🎾",
        body="Don't forget Nadal vs Federer at 8pm!",
        to=EMAIL_RECEIVER
    )
"""