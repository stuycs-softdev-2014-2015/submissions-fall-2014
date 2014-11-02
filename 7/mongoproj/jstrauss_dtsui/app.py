# Justin Strauss and Derek Tsui
# Software Development Period 7
# MongoDB Project

import db
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
    if "name" not in session:
        session["name"] = None
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        passwork = request.form["password"]
        #if authenticate(username,password):
        session['name'] = username
        global prevpage
        page = prevpage
        prevpage = "index"
        return redirect(url_for(page))
        #else:
        #   flash(message)
        # username does not exist
        # incorrect password
    else:
        return render_template("login.html")

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
        return render_template("register.html")

@app.route("/profile")
def profile():
    if session["name"]==None:
        flash("You must login to access Profile, which is a protected page!")
        global prevpage
        prevpage = "profile"
        return redirect(url_for('login'))
    else:
        return render_template("profile.html")

@app.route("/contacts")
def contacts():
    if session["name"]==None:
        flash("You must login to access Contacts, which is a protected page!")
        global prevpage 
        prevpage = "contacts"
        return redirect(url_for('login'))
    else:
        return render_template("contacts.html")

if __name__ == '__main__':
    #db.setup()
    prevpage = "index"
    app.secret_key = "don't store this on github"
    app.debug = True
    app.run(host='0.0.0.0')
    


    
    


