from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "key"

def auth(func):
    def wrapper():
        if 'user' in session:
            return func()
        else:
            return redirect(url_for("login"))
        return wrapper

@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        session['user'] = username
    return redirect(url_for("index"))

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.run()
