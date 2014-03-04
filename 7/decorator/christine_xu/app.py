
from flask import Flask
from flask import render_template, session, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "awesome"

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return func()
        else:
            return redirect(url_for("login"))
    return wrapper

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        session['user'] = username
    return redirect(url_for("index"))
		
@app.route('/Home', methods = ["POST", "GET"])
def Home():
    if request.method == "GET":
        return render_template('Home.html')


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)
