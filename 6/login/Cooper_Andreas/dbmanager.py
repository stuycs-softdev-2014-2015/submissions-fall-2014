from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient

#returns true if password if valid
def authenticate(email, password):
    client = MongoClient()
    db = client.users
    posts = db.posts
    if posts.find({"user": email, "pword": password}).count() > 0:
        return True
    return False

#return the name attached to the email
def getName(email):
    client = MongoClient()
    db = client.users
    posts = db.posts
    post = posts.find_one({"user": email})
    if post != None:
        return post["name"]
    return None
#check if email exists 
def checkEmail(email):
    client = MongoClient()
    db = client.users
    posts = db.posts
    return posts.find_one({"user": email}) != None

def add(name, email, password):
    client = MongoClient()
    db = client.users
    posts = db.posts
    posts.insert({"name": name, "user": email, "pword": password})
    
    
def print_Everything():
    client = MongoClient()
    db = client.users
    print "Printing everything"
    for posts in db.posts.find():
            print posts
            
