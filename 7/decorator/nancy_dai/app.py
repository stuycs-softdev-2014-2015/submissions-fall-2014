from flask import Flask, session, render_template, request, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret"

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return func()
        else:
            return redirect(url_for('login'))
    return wrapper

@app.route("/")
@auth
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form["user"]
        pw = request.form["pw"]
        if user == "strawberry" and pw == "short cake":
            session['user'] = user
            return redirect(url_for('home'))
        return render_template("login.html")

@app.route("/logout")
@auth
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()
