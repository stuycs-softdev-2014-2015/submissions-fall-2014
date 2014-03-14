from flask import Flask, session, redirect,  url_for, render_template, request
from functools import wraps

app = Flask(__name__)
app.secret_key = "sekrit club"


@app.route('/',methods=["GET","POST"])
def home():
    return render_template("home.html")

def auth(func):
    @wraps(func)
    def wrapper(*args):
        if "user" in session:
            return func(*args)
        else:
            return redirect(url_for("login", takao=request.endpoint))
    return wrapper

@app.route('/takao')
@auth
def takao():
    return render_template("takao.html")

@app.route('/login',methods=["GET","POST"])
def login(takao='takao'):
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        user = request.form["user"]
        pw = request.form["pw"]
        if user == "admin" and pw == "takaobestgirl":
            session["user"] = "admin"
        return redirect(url_for(takao))
    
@app.route('/logout')
def logout():
    if "user" in session:
        session.pop("user")
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
