from utils import confirmation
from flask import Flask, flash, render_template, request, redirect, url_for, session, escape
from pymongo import MongoClient
import datetime
from functools import wraps


app = Flask(__name__)
app.secret_key = 'secret'

client = MongoClient('localhost', 27017)
db = client.proj
users = db.users

def authenticate(f):
    @wraps(f)
    def inner(*args):
        if 'username' in session:
            return f(*args)
        else:
            session['next'] = f.__name__
            return redirect( url_for('home') )
    return inner

def add_user(username,password,email,name):
    user = {
        'username' : username,
        'password' : password,
        'email' : email,
        'name' : name,
        'status' : None,
        'description' : None
    }
    return users.insert(user)

def authenticate1( username, passw ):
    user = users.find_one({'username': username})
    #if username does not exist
    if user  == None:
        return "username does not exist"
    elif user['password'] != passw:
        return "password and username do not match"
        
    return "match"


@app.route("/", methods=["GET","POST"])
def home():
    if 'username' in session:
        return redirect(url_for('profile'))
    else:
        if request.method=="GET":
            return render_template("index.html", msg=None)
        else:
            username = request.form["name"]
            password = request.form["password"]
            
        msg = authenticate1( username, password )
        
        if (msg == "match"):
            session['username'] = username
            if 'next' in session:
                s = session['next']
                session.pop('next', None)
                return redirect(url_for(s))
            else:
                return redirect(url_for('profile'))
        else:
            return render_template("index.html", msg=msg)

@app.route("/about")
def about():
    username = None
    if 'username' in session:
        boo = True
        username = escape(session['username'])
    else:
        boo = False
    return render_template("about.html", boo=boo, user=username)

#register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html", msg = None)
       
    else:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        name = request.form["name"]

        msg = confirmation(username, password,email,name)
        if (msg == "good"):
            if users.find_one({'username': username}) != None:
                return render_template( "register.html", msg="username already exists")
            if users.find_one({'email': email}) != None:
                return render_template( "register.html", msg="email already registered to another account" )

            add_user(username,password,email,name)
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return render_template("register.html", msg=msg)


@app.route("/profile", methods=["GET","POST"])
@authenticate
def profile():

        username = escape(session['username'])
        user = users.find_one({'username':username})
        name = user['name']
        email = user['email']
        description = user['description']
        status = user['status']

        if request.method=="GET":
            return render_template("profile.html", username=username, name=name, email=email, description=description, status = status)
            

        if request.method=="POST":
            statt = request.form["status"]
            descrip = request.form["description"]
            if statt != "":
                db.users.update({ 'username': username },{'$set': {'status': statt}})
                status = statt
                if descrip != "":
                    db.users.update({ 'username': username },{'$set': {'description': descrip}})
                    description = descrip
                    
            return render_template("profile.html", username=username, name=name, email=email, description=description, status = status)
            


@app.route("/log_out")
def log_out():
    session.pop('username',None)
    return redirect(url_for('home'))


@app.route("/explore", methods=["GET","POST"])
@authenticate
def explore():
    username = escape(session['username'])
    today = datetime.date.today()
    today = today.strftime('%A,%B%dth, %Y')
    time = datetime.datetime.now().time()
    time = time.strftime("%I:%M")
    
    return render_template("explore.html", today=today, time=time, username=username)
        

if __name__=="__main__":
    app.debug = True
    app.run()

