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
                    else:
                        session['error'] = "Already logged in. Log out to log in as another user."
                        return redirect(url_for("error"))
                    print "loggedinswag"
                    return redirect(url_for("loggedin1"))

        print "wrong username password"
        session['error']= "Incorrect username/password combination. Please try again."
        return redirect(url_for("error"))
    else:
        return render_template("login.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        d = {'username':request.form['username'], 'password':request.form['password']}
        print d
        collection.insert(d)
        print db.collection_names()
        return redirect(url_for("login"))
    else:
        return render_template("register.html")

@app.route("/loggedin1")
def loggedin1():
    return render_template("loggedin1.html")
@app.route("/error")
def error():
    e= session['error']
    return render_template("error.html",e=e)

@app.route("/")
def home():
    if 'username' in session:
        u=session['username']
    return render_template("home.html", u=u)


if __name__=="__main__":
    app.debug=True
    app.run("0.0.0.0");


