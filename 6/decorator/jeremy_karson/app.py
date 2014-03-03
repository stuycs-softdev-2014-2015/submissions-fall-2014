from flask import Flask
from flask import request, redirect, url_for, render_template

app = Flask(__name__)

username = ""
password = ""

@app.route("/")
def home():
    return redirect(url_for("login"))


def auth(func):
    def wrapper():
        if username != "jkarson" or password != "swagu":
            return redirect(url_for("login"))
        else:
            return func()
    return wrapper


@app.route("/login", methods = ['GET','POST'])
def login():
    global username
    global password
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        return redirect("/secretpage")

@app.route("/secretpage", methods = ["GET", "POST"])
@auth
def secretpage():
    if request.method == "GET":
        return render_template("secretpage.html")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0",port=5000)

