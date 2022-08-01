import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv


def random_quote():
    with open("quotes.txt", encoding="utf-8") as file:
        list_quote = file.readlines()
    return random.choice(list_quote)


def send_mail_yahoo(day, quote):
    # YAHOO
    YAHOO_SENDER = os.getenv("SMTP_YAHOO_SENDER")
    YAHOO_USERNAME = os.getenv("SMTP_YAHOO_USERNAME")
    YAHOO_EMAIL = os.getenv("SMTP_YAHOO_EMAIL")
    YAHOO_PASSWORD = os.getenv("SMTP_YAHOO_PASSWORD")
    YAHOO_RECIPIENT = os.getenv("SMTP_YAHOO_RECIPIENT")

    message = f"From: \"{YAHOO_SENDER}\" <{YAHOO_EMAIL}>\n" \
              f"To: {YAHOO_RECIPIENT}\n" \
              f"Subject: Quote of the day\n\n" \
              f"{day} Motivation\n{quote}".encode("utf-8")
    print(message)
    with smtplib.SMTP(host="smtp.mail.yahoo.co.uk", port=587) as connection:
        # Secure the connection
        connection.set_debuglevel(1)  # Set the debug level
        connection.starttls()
        connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
        connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=YAHOO_RECIPIENT, msg=message)


def send_mail_plusnet(day, quote):
    # PLUSNET
    PLUS_SENDER = os.getenv("SMTP_PLUS_SENDER")
    PLUS_USERNAME = os.getenv("SMTP_PLUS_USERNAME")
    PLUS_EMAIL = os.getenv("SMTP_PLUS_EMAIL")
    PLUS_PASSWORD = os.getenv("SMTP_PLUS_PASSWORD")
    PLUS_RECIPIENT = os.getenv("SMTP_PLUS_RECIPIENT")

    message = f"From: \"{PLUS_SENDER}\" <{PLUS_EMAIL}>\n" \
              f"To: {PLUS_RECIPIENT}\n" \
              f"Subject: Quote of the day\n\n" \
              f"{day} Motivation\n{quote}".encode("utf-8")
    print(message)
    with smtplib.SMTP("relay.plus.net") as connection:
        # Secure the connection
        connection.set_debuglevel(1)  # Set the debug level
        connection.starttls()
        connection.login(user=PLUS_USERNAME, password=PLUS_PASSWORD)
        connection.sendmail(from_addr=PLUS_EMAIL, to_addrs=PLUS_RECIPIENT, msg=message)


def send_mail_gmail(day, quote):
    # GMAIL
    GMAIL_SENDER = os.getenv("SMTP_GMAIL_SENDER")
    GMAIL_USERNAME = os.getenv("SMTP_GMAIL_USERNAME")
    GMAIL_EMAIL = os.getenv("SMTP_GMAIL_EMAIL")
    # GMAIL_PASSWORD = os.getenv("SMTP_GMAIL_PASSWORD")
    GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
    GMAIL_RECIPIENT = os.getenv("SMTP_GMAIL_RECIPIENT")

    message = f"From: \"{GMAIL_SENDER}\" <{GMAIL_EMAIL}>\n" \
              f"To: {GMAIL_RECIPIENT}\n" \
              f"Subject: Quote of the day\n\n" \
              f"{day} Motivation\n{quote}".encode("utf-8")
    print(message)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.set_debuglevel(1)  # Set the debug level
        connection.starttls()  # encrypt following SMTP commands
        connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)  # could also use user=GMAIL_EMAIL
        connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=GMAIL_RECIPIENT, msg=message)


# Used to retrieve Environment Variables from file
load_dotenv("E:/Python/EnvironmentVariables/.env")

# set a datetime object
# dob = dt.datetime(year=1955, month=8, day=5)

now = dt.datetime.now()
day_of_week = now.strftime("%A")

quote_of_the_day = random_quote()

# send_mail_yahoo(day_of_week, quote_of_the_day)
# send_mail_plusnet(day_of_week, quote_of_the_day)
send_mail_gmail(day_of_week, quote_of_the_day)
