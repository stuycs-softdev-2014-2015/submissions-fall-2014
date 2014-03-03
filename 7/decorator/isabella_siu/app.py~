from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request, send_from_directory
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret"
app.jinja_env.line_statement_prefix = "="

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" in session:
            return func()
        else:
            return index("Remember to log in!")
    return wrapper

@app.route("/")
def index(msg = None):
    return render_template("index.html", msg = msg)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == "milk" and password == "and cookies":
            session["username"] = "milk"
            return redirect(url_for("content"))
        else:
            return index("There is no such user. Please try again.")

@app.route("/content")
@auth
def content():
    return render_template("content.html")

@app.route("/logout")
@auth
def logout():
    session.pop("username")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.run()
