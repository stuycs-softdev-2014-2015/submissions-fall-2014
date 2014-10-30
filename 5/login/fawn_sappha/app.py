from flask import Flask, render_template, request
from pymongo import Connection

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if method = "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpw = request.form["confirmpw"]
        conn = Connection()
        db = conn["fawn-sappha"]
        accounts = db.accounts.find({}, {"_id":False})
        if not username in accounts.username:
            if password == confirmpw:
                new = {"username": username, "password": password}
                db.accounts.insert(new)
                return render_template("login.html")
    
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
