from flask import Flask
from flask import request, jsonify
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import getTweets
import emoji
import json
import datetime

sendJson = ""

consumer_key = "kEaMOwaPFjdwXelB8rwMXh1Yg"
consumer_secret = "2AKsg0BwxI1bDErlQDUgmNVDvOwzx98htaiYKGXeZzoHv71Jy6"

access_token = "839692039-VulkCGE4QZRZlKYQtDuNjRWgJnxsCdeSfqaPuObs"
access_token_secret = "08AltS6hMTj5Y7sDh2cSLZCrtuqfEYQJ5LTqEI2N4FLN0"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)
@app.route('/')
def index():
    return "Invalid API endpoint"

@app.route('/api/get_flights')
def get_flights():
    return "{'key':'value'}"
@app.route('/api/get_tweets')
def get_tweets():
    parmas = request.args
    airline = parmas['airline']
    myStreamListener = listener()
    myStream = Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(languages=["en"], track=[airline])
@app.route('/api/send_tweet')
def send_tweet(tweet):
    return tweet

if __name__ == '__main__':
    app.run(port=1337)
