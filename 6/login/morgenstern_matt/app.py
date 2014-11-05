import pymongo
from flask import Flask, session, redirect, url_for, escape, request, render_template
app=Flask(__name__)
app.secret_key= 'N\x93\xd6\x87\x13>\x06\x04\xdb\xec\xdd)N\x80A\xa6 \xd6\xb0s\xd4Z\xd8'

conn=pymongo.MongoClient()
db=conn.userdb
collection = db.test
#db.drop_collection("test")
@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        euser = request.form['username']
        epassword = request.form['password']
        f = db.test.find({})
        good = False
        for l in f:
            if l['username']==euser:
                if l['password']==epassword:
                    good=True
                    if 'username' not in session:
                        session['username'] = request.form['username']
                        session['logged']=1
                    else:
                        session['error'] = "Already logged in. Log out to log in as another user."
                        return redirect(url_for("error"))
                    print "loggedinswag"
                    return redirect(url_for("loggedin1"))

        print "wrong username password"
        session['error']= "Incorrect username/password combination. Please try again."
        return redirect(url_for("error"))
    else:
        if 'username' in session:
            u=session['username']
        else:
            u=""

        return render_template("login.html",logged=session['logged'], u=u)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if 'username' in session:
        u=session['username']
    else:
        u=""

    if request.method == "POST":
        f = db.test.find({})
        euser = request.form['username']
        for l in f:
            if l['username'] == euser:
                session['error'] = "Sorry, someone else already has that username. Please try again."
                return redirect(url_for("error"))
        epass =request.form['password']
        if len(epass) < 8:
            session["error"] = 'Your password was less than 8 characters, doofus.'
            return redirect(url_for("error"))
        d = {'username':request.form['username'], 'password':request.form['password']}
        print d
        collection.insert(d)
        print db.collection_names()
        return redirect(url_for("login"))

    else:
        if 'username' in session:
            u=session['username']
        else:
            u=""

        return render_template("register.html", logged = session['logged'], u=u)


@app.route("/loggedin1")
def loggedin1():
    if 'username' not in session:
        session['error'] = "You cannot access this page if you are not logged in! Silly goose."
        return redirect(url_for("login"))
    if 'username' in session:
        u=session['username']
    else:
        u=""

    return render_template("loggedin1.html", logged = session['logged'], u=u)

@app.route("/loggedin2", methods=["GET", "POST"])
def loggedin2():
    if 'username' not in session:
        session['error'] = "You cannot access this page if you are not logged i\
n! Silly goose."
        return redirect(url_for("login"))
    if 'username' in session:
        u=session['username']
    else:
        u=""

    return render_template("loggedin2.html", logged = session['logged'], u=u)


@app.route("/notloggedin")
def notloggedin():
    if 'username' in session:
        u=session['username']
    else:
        u=""

    return render_template("notloggedin.html", logged = session['logged'], u=u)


@app.route("/error")
def error():
    if 'logged' not in session:
        session['logged']=2
    print session['logged']
    if 'username' in session:
        u=session['username']
    else:
        u=""

    e= session['error']
    return render_template("error.html",e=e,logged = session['logged'], u=u)

@app.route("/")
def home():
    if 'logged' not in session:
        session['logged']=2
    if 'username' in session:
        u=session['username']
    else:
        u=""

    return render_template("home.html", logged=session['logged'], u=u)

@app.route("/logout")
def logout():
    session.pop('username',None)
    session['logged'] = 2
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run();
    


