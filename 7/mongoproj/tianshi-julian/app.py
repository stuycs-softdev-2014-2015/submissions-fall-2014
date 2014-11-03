from flask import Flask, render_template, request
import pymongo
import datetime
from pymongo import MongoClient

#---------MONGO------------------------------------------------------------------------
client = MongoClient('localhost', 27017)
db = client.account_manager
logins = db.logins

default_user = {'username':'jkalodog23@aim.com', 'name':'Julian', 'password':'bowtoking', 'date':datetime.datetime.utcnow()}
logins.insert(default_user)

def create_user(user, name, password):
    #Checks if the username already exists, if not adds the new user
    if(find_user(user) == None):
        new_login = {
            'username': user,
            'name':name,
            'password': password,
            'date':datetime.datetime.utcnow()
            }
        return logins.insert(new_login)
    else:
        print("username already exists")

def find_user(user):
    #finds a single user by username
    user = users.find_one({'username': user})
    return user

def find_user(user, password):
    #confirms user and password match
    user = users.find_one({'username': user, 'password': password})
    return user

def change_password(user, old_password, new_password):
    #Validates and changes password                       
    if(find_user(user, old_password) != None):
        db.users.update({'username' : user}, {'$set' : {'password':new_password}})
    if(find_user(user) != None):
        print("please enter your correct old password")
#---------MONGO------------------------------------------------------------------------


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        pw = request.form["password"]
        user = find_user(user,pw)
        if user != None:
            #redirect to personal profile.
        else:
            print("user not found")
    return render_template("login.html")
    
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method =="GET":
        return render_template("register.html")

@app.route("/logout", methods = ["GET"])
def logout():
    pass

if (__name__=='__main__'):
    app.debug=True
    app.run()
