from flask import Flask
from flask import request, render_template, url_for, redirect, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "my secret key"


def auth(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if "user" in session:
            return func(*args,**kwargs)
        return redirect(url_for("login"))
    return wrapper
        
@app.route("/", methods = ["GET","POST"])
@auth
def home():
    if request.method == "POST":
        return redirect(url_for("logout"))
    return render_template("loggedin.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form["user"]
    password = request.form["pass"]
    if username == "user" and password == "pass":
        session["user"] = "pass"
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()

