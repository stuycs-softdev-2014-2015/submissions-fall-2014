from flask import Flask, flash, render_template, request, redirect, url_for,session
from pymongo import Connection

app = Flask(__name__)
app.secret_key = "shhh"
conn = Connection()
db = conn ['aaez']



@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":        
        button = request.args.get("sub", None)
        username = request.args.get("username", None)
        passw = request.args.get("password", None)
        error = None     
        if button == "Login":
            loginfo = { 'name': username, 'pword': passw }
            if db.users.find_one ( { 'name' : username , 'pword' : passw } ) != None:
                #flash("correct login info")
                return redirect(url_for('home.html'))
            else: 
                flash("incorrect login info")
                return redirect(url_for('login.html'))
        
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        button = request.args.get("sub", None)
        username = request.args.get("username", None)
        passw = request.args.get("password", None)
        error = None
        if db.users.find_one ( { 'name' : username } ) == None:
            db.users.insert ( { 'name': username, 'pword': passw } )
            #return "<h1>Thanks for joining!</h1>"
            flash("Thanks for joining")
            return redirect(url_for('login'))
            #return redirect(url_for('home'))
        else:
            #return "<h1>Please select an available username</h1>"
            flash("Please select an available username")
            #return redirect(url_for('register'))
            
    return render_template("register.html")


if __name__=="__main__":
    app.debug = True
    app.run()
    
