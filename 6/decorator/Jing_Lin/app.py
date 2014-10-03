# Andrew Zarenberg                                                                                                                                                                                                   
# Jing Lin                                                                                                                                                                                                           
# SoftDev Period 6                                                                                                                                                                                                                                                                                                  
from flask import Flask
from flask import render_template, session, redirect, url_for, request
from functools import wraps 

app = Flask(__name__)
app.debug = True
app.secret_key = "abc123"

def auth(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        if "username" in session:
            return func()
        else:
            return index('Please Log In')
    return wrapper

@app.route("/")
def index(msg = None):
    return render_template('index.html', msg = msg)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "username" and password == "password":
            session['username'] = username
            return index('Hooray!')
        else:
            return index('Booooo')

@app.route("/secret")
@auth
def secret():
    return render_template("secret.html")

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
