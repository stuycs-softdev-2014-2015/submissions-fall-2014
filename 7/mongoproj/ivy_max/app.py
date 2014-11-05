from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
import config

app = Flask(__name__)
client = MongoClient('mongodb://kirsche:cherry@ds045077.mongolab.com:45077/granatapfel')
db = client['granatapfel']
users = db['users']

def init():
    try:
        user = { 'username': 'test', 'password': 'abc' }
        user_id = users.insert(user)
        print user_id
    except:
        print "user already in database"

def auth(user, pw):
    u = users.find_one({"username": user, "password":pw })
    #print u
    return u != None

def create_user(user, pw):
    new = { 'username': user, 'password': pw }
    try:
        user_id = users.insert(new)
        print user_id
        return "User successfully created."
    except:
        return "Username already in database."

@app.route('/')
def index():
    a = ''
    if 'username' in session:
        a = session['username']
    return render_template("index.html")

@app.route('/login', methods=["GET","POST"])
def login():
    error=""
    if request.method=="POST":
        user = request.form['username']
        pw = request.form['password']
        valid = auth(user,pw)
        if valid:
            session['username'] = request.form['username']
            #session['logged_in'] = True
            flash('You were successfully logged in')
            prev = session.pop('prev_page', None)
            if prev: #came from somewhere
                return redirect(url_for('profile', username=prev))
            return redirect(url_for('profile',username=user))
        else:
            error = "Page not found."
    return render_template("login.html",error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    print session['username']
    session.pop('username', None)
    
    #flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/register', methods=["GET","POST"])
def register():
    error = ""
    if request.method == "POST":
        user = request.form['username']
        pw = request.form['password']
        pw2 = request.form['confirm_password']
        if (user != "" or pw != "" or pw2 != "") and pw == pw2:
            error = create_user(user,pw)
        else:
            error = "Please enter a valid username and password."
    if(error):
        flash(error)
    return render_template("register.html")

@app.route('/u/<username>')
def profile(username=None):
    if not 'username' in session:
        #session['prev_page'] = '/u/%s' %username
        session['prev_page'] = username
        flash("You must login to access that page.")
        return redirect(url_for("login"))
    u = users.find_one({'username':username})
    #print u
    if u != None:
        return render_template("profile.html", username=username, user=u)
    else:
        flash("User not found.")
        return redirect(url_for("index"))

@app.route('/settings', methods=["GET","POST"])
def settings(username=None):
    if not 'username' in session:
        flash("You must login to access this page.")
        session['prev_page'] = "settings"
        return redirect(url_for("login"))
    #print session
    user = users.find_one({'username':session['username']})
    error = ""
    if request.method == "POST":
        loc = request.form['location']
        color = request.form['color']
        animal = request.form['animal']
        
        db.users.update(
                { 'username': session['username'] },
                { '$set': { 'location':loc, 'color':color, 'animal':animal } } )
        user = users.find_one({'username':session['username']})
        flash("Changed settings.")
    return render_template("settings.html", user=user)

if __name__ == "__main__":
    #init()
    app.secret_key = config.getSecret()
    app.debug = True
    app.run()

