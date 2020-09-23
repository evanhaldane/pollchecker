import os
from yagmail import SMTP


def send_message():

    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
    yag = SMTP(SENDER_EMAIL, oauth2_file="oauth2_creds.json")
    body = "{} There are new polls available at: https://projects.fivethirtyeight.com/polls/".format(
        datetime.now()
    )
    yag.send(to=RECIPIENT_EMAIL, subject="New Poll", contents=body)

