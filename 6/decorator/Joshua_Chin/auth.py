from flask import Flask, request, session, redirect, url_for
from functools import wraps

def auth(func):
    return wraps(func)(
        lambda *args, **kwargs: func(*args, **kwargs)
        if "logged" in session
        else redirect(url_for("login", redirect=func.__name__)))

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["logged"] = "in"
        return redirect(url_for(request.args["redirect"]))
    else:
        return '<form method="post"><input type="submit"value="Login"/></form>'

@app.route("/logout")
def logout():
    session.pop("logged", None)
    return redirect(url_for("index"))

@app.route("/")
def index():
    return '<a href="%s">page0</a><br><a href="%s">page1</a>'%(url_for("page0"), url_for("page1"))

@app.route("/page0")
@auth
def page0(): return '<a href="%s">logout</a>'%(url_for("logout"),)

@app.route("/page1")
@auth
def page1(): return '<a href="%s">logout</a>'%(url_for("logout"),)

if __name__ == "__main__":
    app.debug = True
    app.run()
