import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

# Create a MongoClient to the running mongod instance.
# Assumes that a MongoDB instance is running on default host and port
# http://api.mongodb.org/python/current/tutorial.html
client = MongoClient()

collection = db.test

@app.route('/')
def home():
    pass

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.debug=True
    app.run(port = 5005)
    
