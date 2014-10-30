from flask import Flask, render_template,session,redirect
#
#import pymongo
#from pymongo import MongoClient
#client=MongoClient('localhost',1614)

app=Flask(__name__)

@app.route("/")
def index():
    if 'n' not in session:
        session['n']=0
        
    n = session['n']
    n=n+1
    session['n']=n
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('n',None)
    return redirect("/")

@app.route("/home")
def home():
    return render_template("home.html",username)

@app.route("/info")
def info():
    return render_template("info.html",username)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.debug=True
    app.secret_key="this key shouldn't be on github"
    app.run(host="0.0.0.0",port=1119)
