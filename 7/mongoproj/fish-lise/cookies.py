from flask import Flask, render_template, request, redirect, url_for,session
#from pymongo import Connection
from utils import adduser, authenticate

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
@app.route("/home")
def home():
    if request.method=="GET":
        return render_template("base.html")
    else:
        u = request.form.get('uname',None)
        pswd = request.form.get('pswd',None)
        valid_user = authenticate(u,pswd)
        if not(valid_user) and not u == None:
            return render_template("base.html",msg=u)
        else:
            session['myuser'] = u
            return redirect(url_for('loggedin1'))

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="GET":
        #return "<h1>This is the login page</h1>"
        return render_template("login.html", message = "")
    else:
        username = request.form.get("uname",None)
        password = request.form.get("pswd",None)
        #button = request.form["b"]
        #if button == "Login":
        validity = authenticate(username,password)
        if not(validity):
            #return "<h1>This is the login page</h1>"
            return render_template("login.html", msg="Incorrect Username and Password. Try again.")
        else:
                      ####### cur_name = get_name(username) #### IMPLEMENT IN UTILS
            session['myuser'] = username
            print session
            return redirect(url_for('loggedin1'))
        #else:
            #return redirect(url_for('register'))
        
@app.route("/logout")
def logout():
    session.pop("myuser", None)
    return render_template("base.html", msg = "YOU HAVE LOGGED OUT")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        #return "<h1>This is the register page</h1>"
        return render_template("register.html")
    else:
        username = request.form.get("runame",None)
        password = request.form.get("rpswd",None)
        confirm = request.form.get("confirm_password",None)
        name = request.form.get("nickname",None)
        if (len(username)<3 or len(username)<3):
            return render_template("register.html",rconf="Please fill in required elements. Each required element must have at least 3 characters.")
        elif(confirm == password):
            if adduser(username,name): #took out password -> reput when dictionary made into mongodb AND also add the nickname
                return render_template("register.html", rconf="You have successfully registered.")
                #return redirect(url_for('login'))
            else:
                return render_template("register.html", rconf="Username taken. Try Again.")
        else:
            #return "<h1>This is the register page</h1>"
            return render_template("register.html", rconf = "Password doesn't match confirmation.")
        
@app.route("/info")
def info():
    if "myuser" in session and not session["myuser"] == None :
        return render_template("secretpg.html")
    return render_template("login.html")
@app.route("/loggedin1")
def loggedin1():
    print session
    if "myuser" in session and not session["myuser"] == None :
        return render_template("myindex.html")
    return render_template("login.html")

@app.route("/loggedin2")
def loggedin2():
    if "myuser" in session and not session["myuser"]==None :
        return render_template("myinfo.html")
    return render_template("login.html")

if __name__=="__main__":
 #   conn = Connection()
  #  db = conn['1258']
    print authenticate("zum","zum")
    app.secret_key="*]%4WQ4ki[uUF!3pZcNbM8_4SsDFSEsd"
    app.debug = True
    app.run()

