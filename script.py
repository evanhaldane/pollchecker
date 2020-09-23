import json
import requests
from gmail import send_message
import os.path

with open("polls-initial.json") as f:
    saved_polls = json.load(f)

saved_president = [x for x in saved_polls if x["type"] == "president-general"]

URL = "https://projects.fivethirtyeight.com/polls/polls-initial.json"
r = requests.get(URL)
r.raise_for_status()
polls = r.json()
president = [x for x in polls if x["type"] == "president-general"]

# no timestamp, only ids and ordering
max_id = max([x["id"] for x in president])
max_saved_id = max([x["id"] for x in saved_president])

new_poll_found = max_id != max_saved_id

if new_poll_found:
    print("sending email...")
    send_message()
    print("email sent")
    with open("polls-initial.json", "wb") as f:
        f.write(r.content)
        print("saving new polls-initial.json")
else:
    print("No new polls found.")
