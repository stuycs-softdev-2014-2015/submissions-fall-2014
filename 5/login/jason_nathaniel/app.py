#from pymongo import Connection
from flask import Flask, render_template,session,redirect,request,flash
import mongo_help

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        button = request.form["SignUp"]
        #add username and password
        username = request.form["name"]
        password = request.form["password"]
        mongo_help.insert(username,password)
        return render_template("login.html")
    
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        session['username'] = request.form['username']
        return render_template('user.html',
                               username = request.form['username'])

                               
@app.route("/user",methods=["GET","POST"])
def user(username = None):
    username = request.form['name']
    password = request.form['password']
    if (mongo_help.authenticate(username, password)):
        session['username'] = request.form['username']
        return render_template("user.html",username = username)
    else:
        flash("Login error: Incorrect username or password.")
 

    
@app.route("/Tour",methods=["GET","POST"])
def tour():
    return render_template("Tour.html")

'''
@app.route("/logout")
def logout():
    session.pop('n',None)
    return redirect("/")
'''

if __name__=="__main__":
    app.debug=True
    app.secret_key="Captian Swanson"
    app.run()
