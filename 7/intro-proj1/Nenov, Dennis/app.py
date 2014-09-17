#! /usr/bin/python
# -*- coding: cp1252 -*-
from flask import Flask, render_template, request
import sys
import cgitb
import re
import urllib

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/analyzeTopic", methods=['POST', 'GET'])
def analyzeTopic():
    topic_to_analyze = request.form['topic']
    tweets = get_tweets(str(topic_to_analyze))
    tweets = filterTweets(tweets)
    sentiment = getSentiment(tweets)
    return render_template('analyzeTweets.html', tweets=tweets, sentiment=sentiment)

@app.route("/analyzeTweet", methods=['POST', 'GET'])
def analyzeTweet():
    tweets = make_list(request.form['tweet'])
    tweets = filterTweets(tweets)
    sentiment = getSentiment(tweets)
    return render_template('analyzeTweets.html', tweets=tweets, sentiment=sentiment)

def filterTweets(tweets):
    newlist = []
    for tweet in tweets:
        newlist.append(strip_html(tweet).decode('utf-8', 'ignore'))
    return newlist

def getSentiment(tweets):
    newlist = []
    for tweet in tweets:
        newlist.append(sentiment_analysis(tweet))
    return newlist

def sentiment_analysis(inputstring):
    inputstring = re.sub('[!@#$]', '', inputstring)
    list_of_words = inputstring.split()
    positive_words = [":)", ":D", ":D", "good", "great", "positive", "dazzling", "brilliant", "phenomenal", "excellent", "fantastic", "gripping", "mesmerizing", "riveting", "spectacular", "cool", "awesome", "thrilling", "badass", "excellent", "love", "wonderful", "best", "superb", "still", "beautiful", "moving","exciting"]
    negative_words = ["shit", "suck", "bitch", "kill" "angry", "dislike", "terrible", "awful", "unwatchable", "hideous", "cliched", "sucks", "boring", "stupid", "slow", "bad", "worst", "stupid", "waste", "boring", ":(", ":'(", ":|"]
    flip_words = ["can't", "not", "shouldn't", "wouldn't", "don't"]
    feeling = 0
    sarcasm = 0
    for word in list_of_words:
        if word.lower() in positive_words:            
            feeling += 1
        if word.lower() in negative_words:
            feeling -= 1
        if word.lower() in flip_words:
            sarcasm += 1
    if sarcasm > 0:
        feeling = feeling * -1
    if feeling == 0:
        return "Neutral"
    if feeling > 0:
        return "Positive"
    if feeling < 0:
        return "Negative"

def make_list(inputstring):
    newlist =[]
    newlist.append(inputstring)
    return newlist

def strip_html(inputstring):
    inputstring = re.sub("</?[^\W].*?>", "", inputstring)
    inputstring = re.sub("â€¦", "", inputstring)
    inputstring = re.sub("â€", "", inputstring)
    inputstring = re.sub("â", "", inputstring)
    inputstring = re.sub("™", "", inputstring)
    inputstring = inputstring.strip()
    inputstring = " ".join(inputstring.split())
    return inputstring

def get_tweets(query):
    base_url = 'https://twitter.com/search?q='
    content = urllib.urlopen(base_url + query).read()
    m = re.findall('<p class="js-tweet-text tweet-text">(.*?)</p>', content)
    return m

if __name__ == "__main__":
    app.debug = True
    app.run()
