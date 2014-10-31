import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request

app = Flask(__name__)

# Create a MongoClient to the running mongod instance.
# Assumes that a MongoDB instance is running on default host and port
# http://api.mongodb.org/python/current/tutorial.html
client = MongoClient()

db = client.test_database
collection = db.test

@app.route('/')
def home():
    pass


if __name__ == "__main__":
    app.debug=True
    app.run(port = 5005)
    
