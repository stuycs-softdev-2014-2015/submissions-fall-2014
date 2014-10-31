from flask import Flask, flash, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'secret'

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
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
         return render_template("register.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        button = request.form["b"]
        if button == "Register":
            #method to add user
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
    #add methods to actually verify the password
    return True

if __name__=="__main__":
    app.debug = True
    app.run()

