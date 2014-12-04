from flask import Flask, render_template, request, session, redirect, url_for
from utils import loginChecker, dbManager
from pymongo import Connection
import pymongo

app = Flask(__name__)
app.secret_key ='secretKeyThatShouldntBeOnGithub'

#
# conn = pymongo.MongoClient()
# db = conn.userDatabase
conn = Connection()
db = conn["userDatabase"]


@app.route("/login", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('logout'))

    if request.method=='GET':
        return render_template("login.html", nextPage="/")
    else:
        print "loginform POSTING"
        uName = request.form["uName"]
        pword = request.form["pword"]
        session['username'] = uName
        if (loginChecker.checkLogin(uName, pword)):
            print uName
            print pword
            return render_template("profile.html",
                                   first = uName,
                                   last = uName
                                   )
        else:
            return render_template("login.html", tryagain=True)

@app.route("/signup", methods=['GET','POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('logout'))

    if request.method=='GET':
        print "GETTING"
        return render_template("signup.html", nextPage="/")
    else:
        print "signupform POSTING"
        em = request.form["email"]
        fName = request.form["fName"]
        lName = request.form["lName"]
        uName = request.form["uName"]
        pword = request.form["pword"]
        confPword = request.form["confPword"]
        if (dbManager.addUser(uName, pword, confPword, fName, lName, em)==True):
            print "ADDED" + fName + " " + lName
            return redirect(url_for('logout'))
        else:
            print "SOMETHING WENT WRONG ADDING YOU BRO"
            return render_template("signup.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    if not 'username' in session:
        return redirect(url_for('login'))
    else:
        return render_template("profile.html"
                               )

@app.route("/secret")
def secret():
    if not 'username' in session:
        return redirect(url_for('login'))
    else:
        return render_template("secret.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run()
