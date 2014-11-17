from flask import Flask, flash, render_template, request, redirect, url_for,session
from pymongo import Connection
from functools import wraps

app = Flask(__name__)
app.secret_key = "shhh"
conn = Connection()
db = conn ['aaez']

def decorate(func):
    @wraps(func)
    def inner(**args):
        print "inner"
        try:
            print 'session.user: ' + session['user']
        except KeyError:
            return "Don't try to view this page without logging in first"
        return func(args)
    return inner

@app.route("/")
def home(): 
    return render_template("home.html",url1="/login",link1="Login",url2="/register",link2="Register",url0="/about",link0="About")

@app.route("/about")
def about(): 
    return render_template("about.html",url1="/login",link1="Login",url2="/register",link2="Register",url0="/",link0="Home")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        button = request.form.get("sub",None)
        excl=request.form.get("ex",None)
        username = request.form.get("username", None)
        username2 = request.form.get("user",None)
        passw = request.form.get("password", None)
        error = None     
        loginfo = { 'name': username, 'pword': passw }
        #for x in db.users.find():
        #print x
        #print "AAAAAAA" + str(db.users.find_one ( { 'name' : username , 'pword' : passw } ) )
        #print username + passw
        if (excl != None): 
            #return exclusive(username2)
            return redirect(url_for('exclusive', user=username2))
        if db.users.find_one ( { 'name' : username , 'pword' : passw } ) != None:
            #flash("correct login info")
            n = db.users.update ( { 'name': username } , { '$inc': { 'n' : 1 } } )
	    #for q in db.users.find({'name':username}):
 	        #print int(str(q)[str(q).find("u'n': ")+6: str(q).rfind("}")])
	    q = db.users.find({'name':username})[0]
	    n = int(str(q)[str(q).find("u'n': ")+6: str(q).rfind("}")])
            #n = n + 1
            #session['n']=n
	    for x in db.users.find({'name': username,'pword':passw}):
	        print "bleh" + str(db.users.find({'name':username,'pword':passw}))
            session['user']=username
            return render_template("loggedin.html", username=username, n=n,url1="/exclusive",link1="Exclusively for Users",url2="/logout",link2="Logout")
        else: 
            flash("incorrect login info")
            return redirect(url_for('login'))
    return render_template("login.html",url2="/",link2="Home",url1="/register",link1="Register")

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
            db.users.insert ( { 'name': username, 'pword': passw, 'n': 0 } )
            #return "<h1>Thanks for joining!</h1>" + str ( { 'name':username, 'pword': passw } )
            flash("Thanks for joining! Please log in now.")
            return redirect(url_for('login'))
        else:
            flash("Please select an available username")
            #return "<h1>Please select an available username</h1>"
            return redirect(url_for('register'))
    return render_template("register.html",url2="/login",link2="Login",url0="/",link0="Home",url1="/about",link1="About")

@app.route("/exclusive/<user>")
@decorate
def exclusive(user):
    return render_template("justforusers.html",user=user,url1="/logout",link1="Logout")

@app.route("/logout")
def logout():
    print "logout"
    del session['user']
    return redirect(url_for('home'))

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1847)
    
