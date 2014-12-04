from flask import Flask, render_template, request, session, redirect, url_for
from utils import loginChecker, dbManager
import pymongo

app = Flask(__name__)
app.secret_key ='secretKeyThatShouldntBeOnGithub'


conn = pymongo.MongoClient()
db = conn.userDatabase


@app.route("/login", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('logout'))

    if request.method=='GET':
        return render_template("login.html", nextPage="/")
    else:
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

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method=="GET":
        return render_template("signup.html", nextPage="/")
    else:
        em = request.form["email"]
        fName = request.form["fName"]
        lName = request.form["lName"]
        uName = request.form["uName"]
        pword = request.form["pword"]
        confPword = request.form["confPword"]
        if (dbManager.addUser(uName, pword, fName, lName, em)):
            print "ADDED" + fName + " " + lName
            return render_template("login.html")
        else:
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
