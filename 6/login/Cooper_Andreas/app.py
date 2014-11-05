from flask import Flask, render_template, request, redirect, url_for, session
from dbmanager import *

app=Flask(__name__)


@app.route("/profile")
def profile():
    if 'n' not in session:
        session['n'] = None
    return render_template("profile.html", name = session['n'])


@app.route("/login", methods=["GET","POST"])
def login():
    if  'n' not in session:
        session['n'] = None
    print_Everything()
    if request.method=="GET":
        return render_template("login.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        valid = authenticate(email,pword)
        if not(valid):
            return render_template("login.html", error="Not a valid Email or Password")
        else:
            name = getName(email)
            session['n'] = name
            return render_template("secure_page.html",name=name)


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        name = request.form["name"]
        valid_email = not checkEmail(email)
        if not(valid_email):
            error = "Email Already Exists"
            return render_template("register.html", error=error)
        add(name,email,pword)
        return redirect(url_for('login'))

    
@app.route("/secure_page", methods = ["GET", "POST"])
def secure_page():
    if 'n' not in session:
        session['n'] = None
    return render_template("secure_page.html", name = session['n'])

@app.route("/logout")
def logout():
    session.pop('n',None)
    return redirect("/")

@app.route("/", methods=["GET","POST"])
@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.secret_key="This is a secret key"
    app.debug=True
    app.run()
