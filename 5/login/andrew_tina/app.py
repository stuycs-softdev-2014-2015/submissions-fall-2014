from flask import Flask, flash, redirect, request, render_template, url_for, session
from pymongo import Connection

app = Flask(__name__)
app.secret_key = 'dont_tell'

conn = Connection()
db = conn['data']
users = db.posts

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    error = None
    print 'ok'
    if request.method == 'GET':
        return render_template('register.html')
    else:
        button = request.form['b']
        user = request.form['username']
        pw = request.form['password']
        if button == 'cancel':
            return redirect(url_for('register'))
        elif button == 'submit':
            flash('Successfully registered!')
            post = {"username": user,
                    "password": pw}
            post_id = users.insert(post)
            post_id
            print db.collection_names()
            print users.find_one()
            return redirect(url_for('login'))
        
if __name__ == "__main__":
    app.debug = True
    app.run()
