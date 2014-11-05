from flask import Flask, flash, render_template, request, redirect, url_for,session
from pymongo import Connection

app = Flask(__name__)
app.secret_key = "shhh"
conn = Connection()
db = conn ['aaez']

@app.route("/")
def home(): 
    return render_template("home.html",url1="/login",link1="Login",url2="/register",link2="Register")

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
        for x in db.users.find():
            print x
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
            return render_template("loggedin.html", username=username, n=n,url1="/exclusive",link1="Exclusively for Users",url2="/",link2="Logout")
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
            return "<h1>Thanks for joining!</h1>" + str ( { 'name':username, 'pword': passw } )
            #flash("Thanks for joining")
            #return redirect(url_for('login'))
            #return redirect(url_for('home'))
        else:
            flash("Please select an available username")
            #return "<h1>Please select an available username</h1>"
            return redirect(url_for('register'))
    return render_template("register.html",url1="/login",link1="Login",url2="/",link2="Home")

@app.route("/exclusive/<user>")
def exclusive(user):
    return render_template("justforusers.html",user=user,url2="/",link2="Home")

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1847)
    
