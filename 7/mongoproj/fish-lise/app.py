from flask import Flask, render_template, request, redirect, url_for,session
from pymongo import MongoClient

app = Flask(__name__)

#viewable when logged in and not logged in
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
            return redirect(url_for('myinfo'))

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="GET":
        return render_template("login.html", message = "")
    else:
        username = request.form.get("uname",None)
        password = request.form.get("pswd",None)
        validity = authenticate(username,password)
        if not(validity):
            return render_template("login.html", msg="Incorrect Username and Password. Try again.")
        else:
                      ####### cur_name = get_name(username) #### IMPLEMENT IN UTILS
            session['myuser'] = username
            return redirect(url_for('myinfo'))
        #else:
            #return redirect(url_for('register'))
        
@app.route("/logout")
def logout():
    session.pop("myuser", None)
    return render_template("base.html", msg = "YOU HAVE LOGGED OUT")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        username = request.form.get("runame",None)
        password = request.form.get("rpswd",None)
        confirm = request.form.get("confirm_password",None)
        if (len(username)<3 or len(username)<3):
            return render_template("register.html",rconf="Please fill in required elements. Each required element must have at least 3 characters.")
        elif(confirm == password):
            if adduser(username,password):
                return render_template("register.html", rconf="You have successfully registered.")
            else:
                return render_template("register.html", rconf="Username taken. Try Again.")
        else:
            return render_template("register.html", rconf = "Password doesn't match confirmation.")

 
#only viewable when user is logged in       
@app.route("/info")
def info():
    if "myuser" in session and not session["myuser"] == None :
        return render_template("secretpg.html")
    return render_template("login.html")

#only viewable when user is logged in
@app.route("/myinfo")
def myinfo():
    if "myuser" in session and not session["myuser"]==None :
        return render_template("myinfo.html", user=session["myuser"], password=getpword(session["myuser"]))
    return redirect(url_for('login'))

def getpword(uname):
    names = db.info.find()
    for name in names:
        if name['user'] == uname:
            return name['pass']

def authenticate(uname,pword):
    names = db.info.find()
    for name in names:
        if name['user'] == uname:
            if name['pass'] == pword:
                return True
    return False

def adduser(uname,pword):
    if db.info.find_one({'user':uname}) == None:
        d = {'user':uname,'pass':pword}
        db.info.insert(d)
        return True
    return False

if __name__=="__main__":
    client = MongoClient()
    db = client['1258']
    app.secret_key="*]%4WQ4ki[uUF!3pZcNbM8_4SsDFSEsd"
    app.debug = True
    app.run()


