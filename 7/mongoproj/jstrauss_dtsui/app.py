# Justin Strauss and Derek Tsui
# Software Development Period 7
# MongoDB Project

import random
from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import Connection

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
    if "name" not in session:
        session["name"] = None
    return render_template("index.html",user=session['name'])

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


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        passwork = request.form["password"]
        #if authenticate(username,password):
        session['name'] = username
        return redirect(url_for('index'))
        #else:
        #   flash("username/password invalid")
    else:
        return render_template("login.html",user=session['name'])

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    return redirect(url_for('index'))

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        #add info to database
        return
    else:
        return render_template("register.html",user=session['name'])

@app.route("/profile")
def profile():
    return render_template("profile.html",user=session['name'])

@app.route("/contacts")
def contacts():
    return render_template("contacts.html",user=session['name'])



if __name__ == '__main__':
    # conn = Connection()
    # db = conn['jsdt']
    app.secret_key = "don't store this on github"
    app.debug = True
    app.run(host='0.0.0.0')
    


    
    


