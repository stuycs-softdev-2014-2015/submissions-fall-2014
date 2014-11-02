# Justin Strauss and Derek Tsui
# Software Development Period 7
# MongoDB Project

import random
from flask import Flask, render_template, request
from pymongo import Connection
#let this be the main file

app = Flask(__name__)
app.secret_key = "don't store this on github"

@app.route('/', methods=["POST","GET"])
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
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")



if __name__ == '__main__':
    # conn = Connection()
    # db = conn['jsdt']
    app.debug = True
    app.run(host='0.0.0.0')
    


    
    


