from functools import wraps
from flask import Flask, session, flash, redirect, render_template, request, url_for
import database
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Dennis and I worked on this together, and did approximately half each.

def checklogin(f):
    @wraps(f)
    def inner(*args):
        if 'username' not in session:
            flash("You have to be logged in in order to view this page.")
            return redirect(url_for('login'))
        else:
            return f(*args)
    return inner

@app.route('/', methods=["GET","POST"])
@app.route('/login', methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if(database.validateUser(username,password) == False):
            error = 'Unregistered username or incorrect password'
            return redirect(url_for('login'))
        flash("You've logged in successfully")
        session['username'] = request.form['username']
        return redirect(url_for("private"))
    return render_template("login.html")

@app.route('/signup', methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not database.addUser(username,password):
            flash("Registered username, too short username, or too short password.")
            return redirect(url_for('signup'))
        flash("Great! You've registered! Now you can log in.")
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route('/posts/public',methods=["GET","POST"])
def public():
    posts = database.getPublicPosts()
    return render_template("public.html", posts = posts)

@app.route('/posts/private',methods=["GET","POST"])
@checklogin
def private():
    username = session['username']
    posts = database.getPrivatePosts() + database.getPublicPosts()
    return render_template("private.html", posts = posts, username = username)

@app.route('/posts/submit',methods=["GET","POST"])
@checklogin
def submit():
    if request.method == "POST":
        if request.form["type"] == "private":
            database.addPrivatePost(session['username'],request.form["post"])
        else:
            database.addPublicPost(session['username'],request.form["post"])
        return redirect(url_for(request.form["type"])) 
    return render_template("submit.html") 

@app.route('/logout')
def logout():
    error = None
    session.pop('username', None)
    return redirect(url_for('login'))    

if __name__ == '__main__':
    app.debug=True
    app.run()
