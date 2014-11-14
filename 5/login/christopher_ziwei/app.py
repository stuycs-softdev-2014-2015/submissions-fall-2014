#! /usr/bin/python
from flask import Flask, render_template, session, url_for, request, redirect
from pymongo import MongoClient
from mongoauth import *

app = Flask(__name__)
app.secret_key = "secret"

conn = MongoClient()
db = conn['userdatabase']

def dbadd(user, password):
    #(notvalid(user) or notvalid(password)) and 
  if db.database.find({'username' : user}).count() == 0:
    db.database.insert({'username': user, 'password': password})
    return True
  return False  
    
def dbverify(user, password):
  return db.database.find({'username': user, 'password': password}).count() == 1
  
def notvalid(string):
  return len([filter(lambda x: x in "+=\\#[]{}()'\"", string)]) > 0

def needlogin(f):
    def inner(*args):
        if 'user' not in session
            return redirect(.....)
        return f
    return inner

@app.route("/" , methods = ["GET" , "POST"])
def mainpage():
    return redirect("/home") if 'user' in session else redirect("/login")

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user', None)
    return render_template("/")

@app.route("/login", methods = ["GET" , "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if dbverify(username, password):
            session["user"] = username
            return redirect("/")
        return render_template("login.html") 
    else:
        return redirect("/home") if 'user' in session else render_template("login.html")


@app.route("/register", methods = ["GET" , "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if dbadd(username, password):
            return redirect("/")
        add( username , password )
        return render_template("register.html")
    else:
        return render_template("register.html")

        
@app.route("/home")
def home():
    return render_template("home.html", name=session['user']) if 'user' in session else redirect("/login")

@app.route("/game")
def page2():
    return render_template("game.html")
    
if __name__ == "__main__":
    app.run(debug=True)
