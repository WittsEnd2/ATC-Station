from flask import Flask
import json
import os
import time, threading
import unicodedata
import datetime
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

data = []
DATAFOLDER = "data/"


def update_json():
    files = os.listdir(DATAFOLDER)
    for name in files:
        f = open(DATAFOLDER + "" + name, "r")
        x = f.read()
        f.close()
        y = json.loads(x)
        # 1. Get flight name
        data.append(y)
        # 2. Lookup keywords to get from Twitter
        # 3. Create a new Tweet stream with a filter for those tweet keywords
        # 4. Then get the data every 10 seconds using the threading below
        # 5. Pass to sentiment
        # 6. Serve json dumps

    threading.Timer(10, update_json).start()


@app.route("/")
def index():
    return "Invalid API endpoint"


@app.route("/api/get_flights")
def get_flights():
    return json.dumps(data)


@app.route("/api/get_tweets")
def get_tweets():
    # add flight id as key to getTweets.tweets
    return json.dumps(getTweets.tweets)


@app.route("/api/test")
def test():
    return str(getTweets.foundFlights)


def normalize(data):
    x = ""
    for i in data:
        if ord(i) > 127:
            x += " "
        else:
            x += i

    return x


@app.route("/api/airline/<airline>")
def get_airline(airline):
    data = []
    output = ""
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        cols = [x.text.strip() for x in cols]
        data.append(cols)

    for x in data:
        if len(x) > 2:
            code = x[1]
            if airline in code:
                output = x[2]
                break

    return json.dumps({"name": output})


update_json()
r = requests.get("https://en.wikipedia.org/wiki/List_of_airline_codes").text
soup = BeautifulSoup(r, "lxml")
table = soup.find("table", {"class": "wikitable sortable"})

app.run(port=1337)
