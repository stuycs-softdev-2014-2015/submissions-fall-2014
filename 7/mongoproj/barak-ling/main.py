import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, session, url_for, escape

app = Flask(__name__)

# DON'T DO THIS, IT'S JUST FOR REFERENCE, and for local testing...
# mongod --dbpath ../barak-ling/database

# Create a MongoClient to the running mongod instance.
# Assumes that a MongoDB instance is running on default host and port
# http://api.mongodb.org/python/current/tutorial.html godbless
client = MongoClient()

#declares a database for users
db = client.user_database

#declares a collection of users
users = db.users


#testing a user document
#user = {"username":"user1",
#        "password":"qwer"}
#user2 = {"username":"user2",
#        "password":"tyui"}

#adding a user document to the collection
#user_id = users.insert(user)
#user_id = users.insert(user2)

#print users.find_one({"username":"user3"})

# kill the current database
# db.dropDatabase()

# checks if the username is not used; returns False if username is already registered
def check_username(username):
    if users.find_one({"username":username}) != None:
        return False #not valid
    return True #valid

# registers a user. Returns the user_id for no apparent reason
def register_user(username, password):
    user = {"username":username, "password":password, "message":"No message set."}
    user_id = users.insert(user)
    return user_id

# checks if the username and password together works
def check_login(username, password):
    if users.find_one({"username":username,"password":password}) == None:
        return False
    return True

#for now, home page is login page
#@app.route('/home')
@app.route("/login", methods=["GET","POST"])
#def home():
def login():
    if 'username' in session:
        return redirect(url_for('logout'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_login(username,password):
            session['username'] = request.form['username']

            return redirect(url_for('home'))
        else:
            return redirect(url_for('login_failure')) #needs something better

    return render_template("login.html")

@app.route('/login_failure')
def login_failure():
    return render_template("login_0.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        print username
        if not check_username(username):
            return redirect(url_for('register_failure'))
        else:
            register_user(username, password)
            return redirect(url_for('register_success'))
    return render_template("register.html")

@app.route('/register_success')
def register_success():
    return render_template("register_1.html")
@app.route('/register_failure')
def register_failure():
    return render_template("register_0.html")

@app.route("/", methods=["GET","POST"])
@app.route('/home')
def home():
    if 'username' in session:
        name = escape(session['username'])
        #return "logged in as %s" % name
        message = users.find_one({"username":name})["message"]
        #print message
        return render_template("home.html", name=name,message=message);
    return redirect(url_for('login'))

@app.route('/settings', methods=["GET","POST"])
def settings():
    if not 'username' in session:
        return redirect(url_for('login'))
    else:
        name = escape(session['username'])
        if request.method == 'POST':
            password = request.form['password']
            message = request.form['message']
        #print users.find_one({"username":name})["message"]
            if password == users.find_one({"username":name})["password"]:
                users.update({'username':name},
                             { '$set': {'message':message} },
                             upsert=False)

                return redirect(url_for('home'))
            else:
                return render_template("settings_error.html",name=name)
        return render_template("settings.html", name=name)

@app.route('/about')
def about():
    if 'username' in session:
        name = escape(session['username'])
        header = "Welcome, "
    else:
        name = ""
        header = "Simple"
    return render_template("about.html", header=header, name=name)
    
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist!!', 404

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RRR'

if __name__ == "__main__":
    app.debug=True
    app.run(port = 5005)
    
