from flask import Flask, render_template, redirect, url_for, session

from functools import wraps

app = Flask(__name__)
app.secret_key = "a;sldkja"

usename = "jyin"
password = "qweasd"

def auth(myFunction):
    @wraps(myFunction)
    def wrapper(*args):
        if "user" in session:
            #all is well, carry on!
            return myFunction(*args)
        else:
            return redirect(url_for("login"))
    return wrapper

@app.route("/",methods = ["GET","POST"])
@auth
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    #so much hax right here
    session["username"] = username
    return render_template("login.html")


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user",None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
