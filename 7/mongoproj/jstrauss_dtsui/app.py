import random
from flask import Flask, render_template, request
from pymongo import Connection
#let this be the main file

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    conn = Connection('localhost',5000)
    if request.method == "POST":
        form = request.form
    
    '''
    db = conn['jsdt']
    
    users = {'thluffy':0001,'dennis':0002,'bucky':0003,'doughjoe':0004}

    dlist = []
    for i in users:
        d = {i:users[i]}
        dlist.append(d)

    db.jsdt.insert(dlist)
    '''
    print "COLLECTION"
    '''
    print(db.collection_names())
    print "FIND"
    print db.jsdt.find({})
    '''
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    


    
    


