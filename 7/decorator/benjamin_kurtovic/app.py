from functools import wraps

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "58ifvE7YwwANMIJL8b1AQg4Mb9ZGSQFd"

def auth(func):
    @wraps(func)
    def inner():
        if "username" in session:
            return func()
        session["next"] = request.path
        return redirect("/login")
    return inner

@app.route("/")
@auth
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form.get("user")
    password = request.form.get("password")
    if username != "admin" or password != "admin":
        return render_template("login.html", error="Invalid login info.")
    session["username"] = username
    return redirect(session.pop("next", "/"))

@app.route("/logout")
@auth
def logout():
    if "username" in session:
        del session["username"]
    return redirect("/")

@app.route("/page1")
@auth
def page1():
    return render_template("page1.html")

@app.route("/page2")
@auth
def page2():
    return render_template("page2.html")

@app.route("/page3")
@auth
def page3():
    return render_template("page3.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
