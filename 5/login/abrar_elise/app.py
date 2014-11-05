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
        button = request.form.get("sub")
        username = request.form.get("username", None)
        passw = request.form.get("password", None)
        error = None     
        loginfo = { 'name': username, 'pword': passw }
        for x in db.users.find():
            print x
        print "AAAAAAA" + str(db.users.find_one ( { 'name' : username , 'pword' : passw } ) )
        print username + passw
        if db.users.find_one ( { 'name' : username , 'pword' : passw } ) != None:
            #flash("correct login info")
            if 'n' not in session:
                session['n'] = 0
            n = session['n']
            n = n + 1
            session['n']=n
            return render_template("loggedin.html", username=username, n=n)
        else: 
            flash("incorrect login info")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        button = request.form.get("sub", None)
        username = request.form.get("username", None)
        passw = request.form.get("password", None)
        error = None
        if db.users.find_one ( { 'name' : username } ) == None:
            if username == "":
                flash("Please enter a username")
                return redirect(url_for('register'))
            if passw == "":
                flash("Please enter a password")
                return redirect(url_for('register'))
            db.users.insert ( { 'name': username, 'pword': passw } )
            return "<h1>Thanks for joining!</h1>" + str ( { 'name':username, 'pword': passw } )
            #flash("Thanks for joining")
            #return redirect(url_for('login'))
            #return redirect(url_for('home'))
        else:
            flash("Please select an available username")
            #return "<h1>Please select an available username</h1>"
            return redirect(url_for('register'))
    return render_template("register.html")

@app.route("/exclusive")
def exclusive():
    return render_template("justforusers.html")

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1847)
    
