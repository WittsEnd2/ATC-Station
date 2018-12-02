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


# consumer_key = "kEaMOwaPFjdwXelB8rwMXh1Yg"
# consumer_secret = "2AKsg0BwxI1bDErlQDUgmNVDvOwzx98htaiYKGXeZzoHv71Jy6"

# access_token = "839692039-VulkCGE4QZRZlKYQtDuNjRWgJnxsCdeSfqaPuObs"
# access_token_secret = "08AltS6hMTj5Y7sDh2cSLZCrtuqfEYQJ5LTqEI2N4FLN0"

# tweets = []
# foundFlights = ["Microsoft", "Google"]

# def getSentiment(tweet):
#     sid = SentimentIntensityAnalyzer()
#     sent = 0.0
#     count = 0
#     sentList = nltk.tokenize.sent_tokenize(tweet)

#     # Go through each sentence in tweet
#     for sentence in sentList:
#         count += 1
#         ss = sid.polarity_scores(sentence)
#         sent += ss["compound"]  # Tally up the overall sentiment

#     if count != 0:
#         sent = float(sent / count)

#     return sent


# class listener(StreamListener):
#     def __init__(self):
#         # super().__init__()
#         self.counter = 0
#         # def on_status(self, status):
#         # 	print(status)
#         # def on_data(self, data):
#         # 	print(data)

#     def on_data(self, data):

#         data = str(emoji.demojize(data))

#         decoded = json.loads(str(data))
#         # if 'place' in decoded and decoded['place'] is not None:
#         # loc = decoded['place']['bounding_box']['coordinates'][0][0]
#         if 'place' in decoded and decoded['place'] is not None:
#             loc = decoded['place']['bounding_box']['coordinates'][0][0]
#             tweet = str(emoji.demojize(decoded["text"]).encode("unicode_escape"))
#             tweet = tweet[1:]
#             tweet = tweet.strip("\n")
#             tweet = tweet.strip("\.")

#             tweet = tweet.replace("\n", ". ")
#             tweet = tweet.replace("\\'", "'")
#             tweet = tweet.replace("\\", "")
#             tweet = tweet.replace("\\\.", ".")
#             tweet = tweet.replace('"', "'")
#             tweet = tweet.replace("\\n", ". ")
#             tweet = tweet.replace("\\,", "")
#             tweet = tweet.replace(",", "")
#             print(tweet)
#             sid = SentimentIntensityAnalyzer()
#             print(getSentiment(tweet))

#             sendJson = '{"time": "' + str(datetime.datetime.now()) + '", "tweet": "' + tweet + '", "coordinates": ' + str(loc) + '}'

#             tweets.append(sendJson)

#     def on_error(self, status):
#         print(status)


# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# myStreamListener = listener()
# myStream = Stream(auth = api.auth, listener=myStreamListener)
# myStream.filter(languages=['en'], track=foundFlights)

# myStreamListener = listener()
# myStream = Stream(auth=api.auth, listener=myStreamListener)
# myStream.filter(languages=["en"], track=["United Airlines", "airlines", foundFlights])


app = Flask(__name__)

data = []
DATAFOLDER = "data/"


def update_json():
    files = os.listdir(DATAFOLDER)
    for name in files:
        if "history" in name:
            f = open(DATAFOLDER + "" + name, "r")
            x = f.read()
            f.close()
            y = json.loads(x)
            if y not in data:
                # 1. Get flight name
                data.append(y)

                if y.has_key("flights"):
                    getTweets.foundFlights.append(y["flights"]) 
                    if getTweets.myStream.running is True:
                        getTweets.myStream.disconnect()
                    getTweets.myStream.filter(languages=["en"], track=getTweets.foundFlights, async=True)

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
    # getTweets.foundFlights.append("Mark Zuckerberg") 
    # add flight id as key to getTweets.tweets
    return json.dumps(getTweets.tweets)


if __name__ == "__main__":
    update_json()

    #     myStream.filter(languages=["en"], track=foundFlights, async=True)
    #     time.sleep(60)
    app.run(port=1337)
