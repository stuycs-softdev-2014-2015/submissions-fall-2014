#!/usr/bin/python
import mongo
from flask import Flask, render_template, request, redirect, session, flash
from functools import wraps

# the second kitten image link is broken :(

app = Flask(__name__)

def authenticate(page):
    def decorate(f):
        @wraps(f)
        def inner(*args):
            if 'user' not in session:
                flash("You need to be logged in to see that!")
                session['nextpage'] = page
                return redirect("/login")
            return f(*args)
        return inner
    return decorate

@app.route("/home")
@app.route("/")
def home():
    if 'user' in session:
        return redirect("animals")
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if 'user' in session:
        flash("Already logged in!", "error")
        return redirect("/animals")
    
    # Logging in
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        error = mongo.loginErrors(user, password)
        if error:
            flash(error, "error")
        else:
            session['user'] = user
            if 'nextpage' in session:
                page = session['nextpage']
                session.pop("nextpage")
                return redirect(page)
            else:
                return redirect("animals")
    # If error or method == GET
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if 'user' in session:
        flash("Already logged in!", "error")
        return redirect("animals")

    # Registering
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        error = mongo.registerErrors(user,password)
        if error:
            flash(error, "error")
        else:
            mongo.addAccount(user,password)
            flash("Successfully registered")
            return redirect("/login")
    # If error or method == GET
    return render_template("register.html")

@app.route("/logout", methods=["GET","POST"])
def logout():
    if 'user' not in session:
        flash("Not logged in!", "error")
        return redirect("login")

    if request.method == "POST":
        session.pop("user")
        return redirect("/")
    else:
        return render_template("logout.html")

@app.route("/animals")
@authenticate("/animals")
def animals():
    return render_template("animals.html")

@app.route("/otter")
@authenticate("/otter")
def otter():
    return render_template("otter.html")

@app.route("/kitten", methods=["GET","POST"])
@authenticate("/kitten")
def kitten():
    return render_template("kitten.html")


#======================END-DEFINITIONS======================


app.secret_key = '\x90\x9c\xe3C<\x12]^v0p\xde\xc7\xb2\xa1\xea\x90e\x10\xfe\xf1\xd0\xa7g'

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0")
