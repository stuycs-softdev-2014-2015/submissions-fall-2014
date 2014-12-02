from flask import Flask, render_template, request, session, redirect, url_for
import hashlib
from functools import wraps
from pymongo import MongoClient

app = Flask(__name__)

def authenticate(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if "username" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home'))
    return inner

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
	username = request.form.get("username")
	password = request.form.get("password")
        users = MongoClient("mongodb://Bouowmx:ReimuHakurei@ds047440.mongolab.com:47440/account-manager")["account-manager"]["users"]
        if (username is None) and (password is None):
                return render_template("login.html", login_failed = False)
        info = users.find_one({"username": username})
        if (info["password"] != hashlib.sha256(password).hexdigest()):
                return render_template("login.html", login_failed = True)
        session["username"] = username
	return redirect(url_for("profile"))

@app.route("/register/", methods=["GET", "POST"])
def register():
	username = request.form.get("username")
	password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        age = request.form.get("age")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
	if ((username is None) and (password is None) and (password_confirm is None)):
		return render_template("register.html", password_confirm = True, username_available = True)
	if (password != password_confirm):
		return render_template("register.html", password_confirm = False, username = username)
	users = MongoClient("mongodb://Bouowmx:ReimuHakurei@ds047440.mongolab.com:47440/account-manager")["account-manager"]["users"]
	if (users.find({"username": username}).count() != 0):
		return render_template("register.html", password_confirm = True, username = username, username_available = False)
	users.insert({"username": username, "password": hashlib.sha256(password).hexdigest(), "fname": fname, "lname": lname, "age": age, "email": email, "phone": phone, "address":address})
	return render_template("registersuccess.html", fname = fname, lname = lname);

@app.route("/about/")
def about():
        return render_template("about.html")

@app.route("/profile/", methods=["GET", "POST"])
@authenticate
def profile():
        name = request.form.get("name")
        submit = request.form.get("submit")
        if (submit == "Search" or submit == None):
                users = MongoClient("mongodb://Bouowmx:ReimuHakurei@ds047440.mongolab.com:47440/account-manager")["account-manager"]["users"]

                if (name is None) or (users.find({"username": name}).count() == 0):
                        name = session["username"]

                info = users.find_one({"username": name})
                fname = info["fname"]
                lname = info["lname"]
                age = info["age"]
                email = info["email"]
                phone = info["phone"]
                address = info["address"]
                return render_template("profile.html", fname = fname, lname = lname, age = age, email = email, phone = phone, address = address)   
        else:
                session.pop("username",None)
                return redirect(url_for('home'))

app.secret_key = '\x979\xdb\x11\x8e\x1a<\xb9J\xe8;\xa0\x9fb\xb5\x11k\x8d\x7f\xa6\xd4\xe6\xa4\xb6'

if (__name__ == "__main__"):
	app.run(debug = True, port = 5000)
