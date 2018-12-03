from flask import Flask
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import json
import os
import time, threading
import emoji
import unicodedata
import datetime
import nltk
import getTweets
from nltk.sentiment.vader import SentimentIntensityAnalyzer


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

update_json()
app.run(port=1337)
