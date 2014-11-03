#from pymongo import Connection
from flask import Flask, render_template,session,redirect,request
import mongo_help

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        button = request.form["SignUp"]
        #add username and password
        return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")
    
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
