from flask import Flask, render_template, request, redirect, flash, session
import mongo

app = Flask(__name__)
app.secret_key = 'secret'

from functools import wraps
def auth(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print session
        if not(mongo.exists_user(kwargs['user'])):
            flash("There is no such user.")
            return redirect("/")
        if 'name' not in session:
            flash("You don't have permission to view that user's profile.")
            return redirect("/")
        return func(*args)
    return inner

@app.route("/")
def home():
    user = request.args.get("user")
    password = request.args.get("pwd")
    login = request.args.get("login")
    register = request.args.get("register")

    try:
        if (session['name']!=""):
            return redirect("/page")
    except KeyError:
        if (login == "Login" and user != "" and password != ""):
            if (password == mongo.get_password(user)):
                mongo.login_user(user)
                session['name']=user
                return redirect("/page")
            else:
                flash("Username or password is not valid.")
                return redirect("/")
                #return login
        elif (register == "r"):
            return redirect("/register")
        else:
            return render_template("home.html")


@app.route("/page")
def page():
    if not(mongo.exists_user(session['name'])):
        flash("There is no such user.")
        return redirect("/")
    if (mongo.exists_user(session['name'])):
        return render_template("user.html", user=session['name'])
    else:
        flash("You don't have permission to view that user's page.")
        return redirect("/")

@app.route("/profile")
@app.route("/profile/<user>")
@auth
def profile():
    ctr = mongo.get_info(session['name'])
    return render_template("profile.html", user=session['name'], ctr=ctr)
 
@app.route("/about")
def about(user=None):
    try:
        return render_template("about.html", user=session['name'])
    except:
        return render_template("about.html", user=None)

@app.route("/logout")
def logout():
    mongo.logout_user(session['name'])
    flash("Logged out successfully")
    session.clear()
    return redirect("/")

@app.route("/register")
def register():
    user = request.args.get("user")
    password = request.args.get("pwd")
    pcheck = request.args.get("pwdcheck")
    register = request.args.get("register")

    if (user != None and password != None and pcheck != None):
        if (len(password) < 5):
            flash("Password must be at least 5 characters.")
            return redirect("/register")
        if (password == pcheck and not(mongo.exists_user(user))):
            session['name']=user
            mongo.add_user(user,password)
            mongo.login_user(user)
            return redirect("/page")
        if (mongo.exists_user(user)):
            flash("This username is taken.")
            return redirect("/register")
        if (password != pcheck):
            flash("The passwords do not match.")
            return redirect("/register")
    else:
        return render_template("register.html")

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

    
