from flask import Flask, render_template, request, flash, redirect, url_for, session, escape, g
from functools import wraps
import mongo

app = Flask(__name__)
un = None
loggedin = False
app.secret_key = "super_secret_shhh"

@app.route("/", methods=["POST", "GET"])
def index():
    global loggedin, un
    if request.method == "POST":
        b = request.form["b"]
        if b == "About":
            return redirect(url_for("about", logout = True))
        elif b == "Log Out":
            un = None      
            loggedin = False
        elif b == "Register":
            return redirect(url_for("register"))
        elif b == "Log In":
            return redirect(url_for("login"))
    if loggedin: 
        return render_template("index.html", username = un, loggedin = loggedin, logout = True)
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpw = request.form["confirmpw"]
        if mongo.validusername(username):
            if password == confirmpw:
                mongo.adduser(username, password)
                return render_template("login.html", message = "Register Successful")
            else:
                return render_template("register.html", message = "Passwords do not match")
        else:
            return render_template("register.html", message = "That username is already taken")
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
@authenticate
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if mongo.checkcombo(username, password):
            global un
            global loggedin
            un = username
            loggedin = True
            return redirect(url_for('index'))      
        else:
            return render_template("login.html", message = "Incorrect username or password")
    return render_template("login.html")

def authenticate(f):
    def inner(*args):
        ##code
        return f(*args)
    return inner

@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html", logout = True)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
