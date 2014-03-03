from flask import Flask, session, redirect, url_for, escape, request, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.jinja_env.line_statement_prefix = "="

@app.route('/')
def home(msg = None):
    return render_template("home.html", msg=msg)

def auth(func, *args, **kwargs):
    @wraps(func)
    def inner(*args, **kwargs):
        if "username" in session:
            return func()
        else:
            return home("Please log in!")
    return inner

@app.route('/hidden')
@auth
def hidden():
    return render_template("hidden.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            session['username'] = username
            return home("Logged in!")
        else:
            return render_template("login.html",msg="Incorrect Username or Password!")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("home.html", msg="Logged out")

def authenticate(username, password):
    return username == "sweyn" and password == "password"

if __name__ == "__main__":
    app.run(debug = True)