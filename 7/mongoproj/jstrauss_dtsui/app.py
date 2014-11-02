# Justin Strauss and Derek Tsui
# Software Development Period 7
# MongoDB Project

import random
from flask import Flask, render_template, request, redirect, session
from pymongo import Connection

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
    # if request.method == "POST":
    #     form = request.form

    # db.jsdt.drop()
        
    # users = {'thluffy':0001,'dennis':0002,'bucky':0003,'doughjoe':0004}

    # dlist = []
    # for i in users:
    #     #d = {i:users[i]}
    #     d = {'name':i,'pw':users[i]}
    #     dlist.append(d)

    # db.jsdt.insert(dlist)
    # print "COLLECTION"
    # print(db.collection_names())
    # print "FIND"
    # res = db.jsdt.find({})
    # info = [x for x in res]
    # print info
    return render_template("index.html",user=None)

@app.route("/login")
def login():
    return render_template("login.html",user=None)

@app.route("/register")
def register():
    if request.method == "GET":
        return render_template("register.html",user=None)

@app.route("/profile")
def profile():
    return render_template("profile.html",user=None)

@app.route("/contacts")
def contacts():
    return render_template("contacts.html",user=None)



if __name__ == '__main__':
    # conn = Connection()
    # db = conn['jsdt']
    app.secret_key = "don't store this on github"
    app.debug = True
    app.run(host='0.0.0.0')
    


    
    


