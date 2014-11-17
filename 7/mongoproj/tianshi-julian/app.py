from flask import Flask, render_template, request, url_for, redirect, session, escape
import pymongo
import datetime
from pymongo import MongoClient

#---------MONGO------------------------------------------------------------------------
client = MongoClient('localhost', 27017)
db = client.account_manager
logins = db.logins

default_user = {'username':'jkalodog23@aim.com', 'password':'bowtoking', 'date':datetime.datetime.utcnow()}
logins.insert(default_user)

def create_user(user, password):
    #Checks if the username already exists, if not adds the new user
    if(user_exists(user) == None):
        new_login = {
            'username': user,
            'password': password,
            'date':datetime.datetime.utcnow()
            }
        return logins.insert(new_login)
    else:
        print("username already exists")


        
def user_exists(user):
    #finds a single user by username
    user = logins.find_one({'username': user})
    return user

def find_user(user, password):
    #confirms user and password match
    user = logins.find_one({'username': user, 'password': password})
    return user

def change_password(user, old_password, new_password):
    #Validates and changes password                       
    if(find_user(user, old_password) != None):
        db.logins.update({'username' : user}, {'$set' : {'password':new_password}})
    if(find_user(user) != None):
        print("please enter your correct old password")
#---------MONGO------------------------------------------------------------------------


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET","POST"])
def home():
    if 'email' in session:
        return 'Logged in as %s' % escape(session['username'])
    return render_template("home.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        pw = request.form["password"]
        login = authenticate(email,pw)
        if login:
            #redirect to personal profile.
            session['email']=request.form['email']
            redirect(url_for("/profile"))
        else:
            print ("user not found")
            return render_template("login.html")
    return render_template("login.html")
    
@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method =="GET":
        return render_template("register.html")
    else:
        email = request.form["email"]
        pw = request.form["password"]
        success=create_user(email,pw)
        if (success != None):
            return render_template("login.html")
        else:
            return render_template("register.html")

@app.route("/profile", methods=["GET","POST"])
def profile():
    return render_template("/profile",session=session)


@app.route("/logout", methods = ["GET"])
def logout():
    session.pop('email', None)
    return redirect("/")

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if (__name__=='__main__'):
    app.debug=True
    app.run()
