from flask import Flask, render_template, request
from pymongo import Connection

app = Flask(__name__)
conn = Connection()
db = conn["fawn-sappha"]

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        account = db.accounts.find({username: username},{"_if":False})
        #find a better way of doing this
        a = {}
        for q in account:
            a["user"]= q.get(username)
            a["passw"]  = q.get(password)
        if a == {} or a["passw"] != password:
            return render_template("login.html", message = "Incorrect username or password")
        else:
            return render_template("index.html", username = username, loggedin = True)
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpw = request.form["confirmpw"]
        accounts = db.accounts.find({}, {"_id":False})
        uns = []
        for q in accounts:
            uns.append(q.get(username))
        if not username in uns:
            if password == confirmpw:
                new = {username: username, password: password}
                db.accounts.insert(new)
                return render_template("login.html", message = "Register Successful")
            else:
                return render_template("register.html", message = "Passwords do not match")
        else:
            return render_template("register.html", message = "That username is already taken")
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
