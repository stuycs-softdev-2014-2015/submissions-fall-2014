from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import Connection

#mongo setup
conn = Connection()
db = conn["leon_miranda"]

#flask setup
app = Flask(__name__)

def lenCursor(cursor):
    count = 0
    for x in cursor:
        count += 1
    return count
def authenticate(func):
    def inner(*args):
        if args[0] == "" or args[1] == "":
            return "You must enter a username AND a password"
        pword = db.users.find({"user":args[0]}, {"_id":0, "pwd":1})
        #print [f for f in pword]
        if lenCursor(pword) == 0:
            return "Wrong. Try again. (Hint: check your username)"
        elif db.users.find({"user":args[0]}, {"_id":0, "pwd":1})[0]["pwd"] != args[1]:
            return "Wrong. Try again. (Hint: check your password)"
        return True
    return inner

@authenticate
def checkLogin(user, pwd):
    if user.lower() == "miranda":
       return "Mirandas are not welcome here!"

def checkRegister(user, pwd):
    if user == "" or pwd == "":
        return "You must enter a username AND a password"
    elif lenCursor(db.users.find({"user":user})) != 0:
        return "Username has been taken, please try again"
    db.users.insert({"user":user, "pwd":pwd})
    return True
    
@app.route("/login", methods = ["GET", "POST"])
def login():
    error=None
    if "user" not in session:
        if request.method == "POST":
            username = request.form["user"]
            pwd = request.form["pwd"]
            error = checkLogin(username, pwd)
            if error == True:
                session["user"]=username
                return redirect(url_for("user"))
        
        return render_template("login.html",error=error)
    else:
        return redirect(url_for("user"))


@app.route("/register", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
def register():
    if "user" not in session:
        error=None
        if request.method == "POST":
            username = request.form["user"]
            pwd = request.form["pwd"]
            error = checkRegister(username, pwd)
            if error == True:
                session["user"]=username
                return redirect(url_for("user"))
        return render_template("home.html", error=error)
    else:
        return redirect(url_for("user"))

#logout button on other pages will redirect to this
@app.route("/logout")
def logout():
    #log user out
    #page will have button to return to login page
    session.pop('user',None)
    return render_template("logout.html")

@app.route("/about")
#unprotected page
def about():
    user=None
    if "user" in session:
        user=session["user"]
    return render_template("about.html",user=user)

@app.route("/settings", methods = ["GET", "POST"])
#protected, allows user to change info and put more info also
def settings():
    error = None
    if "user" in session:
        #try:
            print "TrYING"
            if request.method == "POST":
                print "POSTing"
                username = request.form["user"]
                pwd = request.form["pword"]
                db.users.update({"user":session["user"]},{"$set": {'user':username,"pwd":pwd}})
                session["user"]=username
                error = "Your username and password have been updated"
                return render_template("settings.html", user=session["user"],error=error)
            #except:
            return render_template("settings.html", user=session["user"],error=error)
    return redirect(url_for("login",error="Please login to access this page"))

@app.route("/user",methods = ["GET", "POST"])
#protected, what they are sent to immediately, idek what it should contain
def user():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("user.html", user=session["user"])

if __name__ == "__main__":
    app.debug = True
    app.secret_key=open("secret_key.txt").read()
    app.run()
    #name = request.form["name"]
    #email = request.form["email"]
    #age = request.form["age"]
            #if (name == None or email == None or age == None or
         #   username == None or pwd == None): #b/c they are all mandatory
          #  if len(db.users.find({"name":name})) == 0:
           #     db.users.insert({"name":name, "email":email, "age":age,
            #                     "user":username, "pwd":pwd})
             #   return redirect(url_for("main"))
