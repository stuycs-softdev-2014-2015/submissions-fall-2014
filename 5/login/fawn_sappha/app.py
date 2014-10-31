from flask import Flask, render_template, request
from pymongo import Connection

app = Flask(__name__)
conn = Connection()
db = conn["fawn-sappha"]

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpw = request.form["confirmpw"]
        accounts = db.accounts.find({}, {"_id":False})
        if not username in accounts:
            if password == confirmpw:
                new = {"username": username, "password": password}
                db.accounts.insert(new)
                return render_template("login.html", message = "Register Successful")
            else:
                return render_template("register.html", message = "Passwords do not match")
        else:
            return render_template("register.html", message = "That username is already taken")
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]       
    accounts= db.accounts.find({},{"_if":False})
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
