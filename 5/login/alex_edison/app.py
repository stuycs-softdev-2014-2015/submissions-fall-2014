from flask import Flask, render_template, request, g, flash, redirect, url_for
from pymongo import Connection

app = Flask(__name__)
app.secret_key = "SWAG"
conn = Connection()
db = conn ['sweg']

username=""
pwd=""
Login=False

def correct_login():
    global username,pwd
    users = db.userswags.find({'un' : username})
    for user in users:
        return user["pwd"] == pwd
    return False

@app.route("/", methods=["GET","POST"])
def home():
    global username,pwd,Login
    if Login==False:
        if request.method=="POST":
            button = request.form.get("sub", None)
            username = request.form.get("username", None)
            pwd = request.form.get("pwd", None)
            if db.userswags.find_one ( { 'un' : username } ) != None:
                if username == "":
                    flash("Please enter a swagname")
                    return redirect(url_for('home'))
                elif pwd == "":
                    flash("Please enter a passwag")
                    return redirect(url_for('home'))
                elif correct_login():
                    Login=True
                    return redirect(url_for('logged'))
                else:
                    flash("Wrong passwag")
                    return redirect(url_for('home'))
            else:
                flash("Name not found, swaggy")
                return redirect(url_for('home'))
        return render_template("home.html")
    else: 
        return redirect(url_for('logged'))

@app.route("/swagister", methods=["GET","POST"])
def swagister():
    global username,pwd,Login
    if request.method=="POST":
        Login=False
        button = request.form.get("sub", None)
        username = request.form.get("username", None)
        pwd = request.form.get("pwd", None)
        if db.userswags.find_one ( { 'un' : username } ) == None:
            if username == "":
                flash("Please enter a swagname")
                return redirect(url_for('swagister'))
            elif pwd == "":
                flash("Please enter a passwag")
                return redirect(url_for('swagister'))
            else: 
                db.userswags.insert ( { 'un': username, 'pwd': pwd } )
                Login=True
                return redirect(url_for('user'))
        else:
            flash("Yo name is taken, swaggy")
            return redirect(url_for('swagister'))
    return render_template("register.html")

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route("/user", methods=["GET","POST"])
def user():
    global Login
    if Login==True:
        return render_template("user.html",un=username)
    else:
        return redirect(url_for('swagister'))

@app.route("/logged", methods=["GET","POST"])
def logged():
    global Login
    if Login==True:
        return render_template("logged.html",un=username)
    else:
        return redirect(url_for('swagister'))

@app.route("/logout", methods=["GET","POST"])
def logout():
    global Login,username,pwd
    if Login==True:
        Login=False
        flash("Adios my swag hombre, "+username+"!")
        username=""
        pwd=""
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
    
if __name__=="__main__":    
    app.debug=True
    app.run(host="127.0.0.1",port=5678)

