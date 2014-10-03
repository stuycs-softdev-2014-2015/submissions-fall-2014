from flask import Flask, redirect, url_for, request, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = "abcde"

def auth(func, *args, **kwargs):
    @wraps(func)
    def inner(*args, **kwargs):
        if "user" in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return inner

@app.route('/', methods=["GET","POST"])
@auth
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return redirect(url_for("logout"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        user = request.form['user']
        pwd = request.form['pwd']
        if user == "maia" and pwd == "mypwd":
            session['user'] = user
            return render_template("home.html")
        else:
            return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
