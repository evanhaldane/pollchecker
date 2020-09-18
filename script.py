import json
import requests
from gmail import send_message
import os.path

with open("polls-initial.json") as f:
    saved_polls = json.load(f)

saved_president = filter(lambda x: x["type"] == "president-general", saved_polls)

URL = "https://projects.fivethirtyeight.com/polls/polls-initial.json"
r = requests.get(URL)
r.raise_for_status()
polls = r.json()
president = filter(lambda x: x["type"] == "president-general", polls)

# no timestamp, only ids and ordering
# assume ordered and just check first item
new_poll_found = next(president) != next(saved_president)

if new_poll_found:
    print("sending email...")
    send_message()
    print("email sent")
    with open("polls-initial.json", "wb") as f:
        f.write(r.content)
        print("saving new polls-initial.json")
else:
    print("No new polls found.")
