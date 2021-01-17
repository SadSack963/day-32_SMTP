import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
YAHOO_SENDER = os.getenv("SMTP_YAHOO_SENDER")
YAHOO_USERNAME = os.getenv("SMTP_YAHOO_USERNAME")
YAHOO_EMAIL = os.getenv("SMTP_YAHOO_EMAIL")
YAHOO_PASSWORD = os.getenv("SMTP_YAHOO_PASSWORD")
YAHOO_RECIPIENT = os.getenv("SMTP_YAHOO_RECIPIENT")

# PLUS_SENDER = os.getenv("SMTP_PLUS_SENDER")
# PLUS_USERNAME = os.getenv("SMTP_PLUS_USERNAME")
# PLUS_EMAIL = os.getenv("SMTP_PLUS_EMAIL")
# PLUS_PASSWORD = os.getenv("SMTP_PLUS_PASSWORD")
# PLUS_RECIPIENT = os.getenv("SMTP_PLUS_RECIPIENT")


def random_quote():
    with open("quotes.txt", encoding="utf-8") as file:
        list_quote = file.readlines()
    return random.choice(list_quote)


def send_mail(day, quote):
    # PLUSNET
    # message = f"From: \"{PLUS_SENDER}\" <{PLUS_EMAIL}>\n" \
    #           f"To: {PLUS_RECIPIENT}\n" \
    #           f"Subject: Quote of the day\n\n" \
    #           f"{day} Motivation\n{quote}".encode("utf-8")
    # print(message)
    # with smtplib.SMTP("relay.plus.net") as connection:
    #     # Secure the connection
    #     connection.starttls()
    #     connection.login(user=PLUS_USERNAME, password=PLUS_PASSWORD)
    #     connection.sendmail(from_addr=PLUS_EMAIL, to_addrs=PLUS_RECIPIENT, msg=message)

    # YAHOO
    message = f"From: \"{YAHOO_SENDER}\" <{YAHOO_EMAIL}>\n" \
              f"To: {YAHOO_RECIPIENT}\n" \
              f"Subject: Quote of the day\n\n" \
              f"{day} Motivation\n{quote}".encode("utf-8")
    print(message)
    with smtplib.SMTP(host="smtp.mail.yahoo.co.uk", port=587) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
        connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=YAHOO_RECIPIENT, msg=message)


# set a datetime object
# dob = dt.datetime(year=1955, month=8, day=5)

now = dt.datetime.now()
day_of_week = now.strftime("%A")

quote_of_the_day = random_quote()

send_mail(day_of_week, quote_of_the_day)

