from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask.ext.pymongo import PyMongo
import mongo
import sqlite3, hashlib

app = Flask(__name__)

app.secret_key="SOMETHINGUNIQUEANDSECRET" # Don't use this key if you were actually going to deploy!

NOT_LOGGED_IN = "You are not logged in!"
ALREADY_LOGGED_IN = "You are already logged in!"

@app.route("/home", methods = ["GET","POST"])
@app.route("/", methods = ["GET","POST"])
def home():
    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if 'user' in session:
        flash(ALREADY_LOGGED_IN)
        return redirect(url_for('dashboard'))

    # Logging in
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']

        # Login attempt
        result, passed = mongo.authenticate_user(user, pwd)

        if result: # Success
            session['user'] = user
            flash(passed)
            #redirect(url_for('dashboard'))
            return redirect('dashboard')

        else: # Failure
            flash(passed)
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if 'user' in session:
        flash(ALREADY_LOGGED_IN)
        return redirect(url_for('dashboard'))

    # Registration form submitted
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']

        # Reigstration attempt
        result, passed = mongo.create_user(user, pwd)

        if result: #Success
            flash(passed)
            return redirect(url_for('login'))

        else: # Failure
            flash(passed)
            return redirect(url_for('register'))

    # Viewing registration page
    else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        flash(NOT_LOGGED_IN)
        return redirect(url_for('login'))

@app.route('/exclusive')
def exclusive():
    if 'user' in session:
        return render_template('exclusive.html')
    else:
        flash(NOT_LOGGED_IN)
        return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(e): # Return rendering, 404
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
