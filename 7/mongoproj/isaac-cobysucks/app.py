import datetime
from flask import Flask, flash, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'secret'

# MongoDB
client = MongoClient('localhost', 27017)
db = client.mongo_project
users = db.users

def create_user(username, password, name, birthday):
	'''Adds user to the database, returns their mongo _id'''
	user = {
	'username' : username,
	'password' : password,
    'name' : name,
    'birthday' : birthday,
	'date' : datetime.datetime.utcnow()
	}
	return users.insert(user)

def find_user(username):
    user = users.find_one({'username': username})
    return user

# update dict must be in the form {field_to_update : new_val}
def update_user(username, update_dict):
    update_dict.update( {'date' : datetime.datetime.utcnow()} )
    db.users.update({'username' : username}, {'$set' : update_dict}, upsert=False)
    return True
# End MongoDB


# Login page
@app.route("/", methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html", message = "")
    else:
        # Get form data
        username = request.form["username"]
        password = request.form["password"]
        button = request.form["b"]
        if button == "Login":
            validity = authenticate(username, password)
            if validity:
                flash("You successfully logged in!")
                return redirect(url_for('profile'))
            else:
                return render_template("login.html", message = "Username/Password Invalid")
        elif button == "About":
            return redirect(url_for('about'))
        else:
            return redirect(url_for('register'))

# Register Page
# STILL NEEDS TO CHECK AGAIST EXISTING USERNAMES & PWORD VALIDITY
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
         return render_template("register.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        password_check = request.form["confirm_password"]
        name = request.form["name"]
        button = request.form["b"]

        if button == "Register":
            create_user(username, password, name, None)
            return redirect(url_for('login'))
        else:
            return render_template("register.html")

# About Page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

# Profile Page
@app.route("/profile", methods=["GET","POST"])
def profile():
    if request.method=="GET":
        return render_template("profile.html")
    else:
        #replace with appropriate stuff
        return render_template("profile.html")

def authenticate(username, password):
    user = find_user(username)
    # No such user
    if user == None:
        return False
    # Username/Password combo don't match
    elif str(user['username']) != username or str(user['password']) != password:
        return False
    # We good
    else:
        return True

if __name__=="__main__":
    app.debug = True
    app.run()

