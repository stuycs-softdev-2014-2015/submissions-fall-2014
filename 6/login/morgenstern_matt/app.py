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
                    session['username'] = request.form['username']
                    print "loggedinswag"
                    return redirect(url_for("loggedin1"))

        print "wrong username password"
        return redirect(url_for("home"))
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

@app.route("/")
def home():
    return render_template("home.html")


if __name__=="__main__":
    app.debug=True
    app.run();


