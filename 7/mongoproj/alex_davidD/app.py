#Alex Libman, David Dvorkin pd.7 Soft Dev
from flask import Flask, render_template, request, redirect, url_for, session
import login

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
@app.route("/home",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        if request.form['b'] == "Register":
            return redirect(url_for("register"))
        if request.form['b'] == "Logout":
            return logout()
        user = request.form["username"]
        pword = request.form["password"]
        msg = login.login(user,pword)
        if msg == "Successfully logged in.":
            session["user"] = user
            return redirect(url_for("inform"))
            #redirect to info page
        else:
            return render_template("login.html",message=msg)
    else:
        if "user" in session:
            return render_template("textwithlogout.html",message="You are already logged in.")
        return render_template("login.html")

@app.route("/register",methods = ["POST","GET"])
def register():
    if request.method == "POST":
        if request.form['b'] == "Logout":
            return logout()
        user = request.form["username"]
        pword = request.form["password"]
        pword2 = request.form["confirm_password"]
        name = request.form["name"]
        msg = login.register(user,pword,pword2,name)
        if msg == "Successfully registered.":
            return redirect(url_for("home"))
        else:
            return render_template("register.html",message=msg)
    else:
        if "user" in session:
            return render_template("textwithlogout.html",message="You are already logged in.")
        return render_template("register.html")

@app.route("/mainpage",methods = ["POST","GET"])
def inform():
    if request.method == "POST" and request.form['b'] == "Logout":
        return logout()
    if "user" in session:
        info = login.getinfo(session["user"])#dict which includes "user" and "name"
        return render_template("mainpage.html",info=info)
    else:
        return render_template("text.html",message="You must be logged in to view this page.")

@app.route("/page")
def page():
    if request.method == "POST" and request.form['b'] == "Logout":
        return logout()
    if "user" in session:
        return render_template("page.html")
    else:
        return render_template("text.html",message="You must be logged in to view this page.")

@app.route("/about")
def about():
    return render_template("about.html")

def logout():
    session.pop("user",None)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()

