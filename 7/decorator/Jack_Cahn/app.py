#!/usr/bin/env python
from flask import Flask, session, redirect, url_for, escape, request, render_template
app = Flask(__name__)
app.secret_key = 'Cahn'

import db

def auth(func, *args, **kwargs):
    def wrapouter(func):
        print "authorization process will now begin"
        def wrapinner(*args, **kwargs):
            if "username" in session: 
                return func()
            else:
                return home("You must log in to access this feature")
        return wrapinner
    return wrapouter

@app.route('/')
def home():
    return "Home Page"
                
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home',loggedin=True))
    elif request.method == "GET":
        return render_template("register.html",message = "")
    else:
        button = request.form['button'].encode("utf8")
        if button == "Register":
            if db.register(request.form['user'], request.form['pass']):
                session['user'] = request.form['user']
                return redirect(url_for('home',loggedin=True))
            else:
                return render_template("register.html", message = "User already exists. Please login.")
                
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home',loggedin=True))
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        user = request.form['user'].encode ('ascii',"ignore")
        pw = request.form['pass'].encode ('ascii',"ignore")
        if user == "" or pw == "":
            return render_template("login.html", message = "Please enter your username and password.")
        elif db.login(user, pw):
            session['user'] = user
            return redirect(url_for('home',loggedin=True))
        else:
            return render_template("login.html", message = "Invalid username and password combination. Usernames and passwords are case sensitive. Please try again.")   

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run(port=5005)
