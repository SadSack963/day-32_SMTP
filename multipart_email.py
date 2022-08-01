import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


def send_multipart_email(image_path):
    # GMAIL
    GMAIL_SENDER = os.getenv("SMTP_GMAIL_SENDER")
    GMAIL_USERNAME = os.getenv("SMTP_GMAIL_USERNAME")
    GMAIL_EMAIL = os.getenv("SMTP_GMAIL_EMAIL")
    # GMAIL_PASSWORD = os.getenv("SMTP_GMAIL_PASSWORD")
    GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
    GMAIL_RECIPIENT = os.getenv("SMTP_GMAIL_RECIPIENT")

    with open(image_path, 'rb') as fp:
        img = MIMEImage(fp.read())

    body_text = MIMEText(
        '<h1>Some email body text here</h1>'
        '<p>You can use <b>HTML tags</b> for formatting.</p>'
        '<p>You could also use an <em><i>f-string</i></em> to include variable values.</p>'
        f'<p>&nbsp;&nbsp;&nbsp;e.g. Attached Image Filename: {image_path}</p>',
        'html'
    )

    message = MIMEMultipart()
    message["From"] = f'"{GMAIL_SENDER}" <{GMAIL_EMAIL}>'
    message["To"] = f'{GMAIL_RECIPIENT}'
    message["Subject"] = 'Test Image Attachment'
    message.attach(body_text)
    message.attach(img)

    # print(message)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.set_debuglevel(1)  # Set the debug level
        connection.starttls()
        connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=GMAIL_RECIPIENT, msg=message.as_string())


# Used to retrieve Environment Variables from file
load_dotenv("E:/Python/EnvironmentVariables/.env")

send_multipart_email("hirst-painting.jpg")
