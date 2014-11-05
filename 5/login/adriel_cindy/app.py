from flask import Flask, render_template, request, redirect, flash, session
import mongo

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def home():
    user = request.args.get("user")
    password = request.args.get("pwd")
    login = request.args.get("login")
    register = request.args.get("register")

    try:
        if (session['name']!=""):
            return redirect("/page/"+session['name'])
    except KeyError:
        if (login == "Login" and user != "" and password != ""):
            if (password == mongo.get_password(user)):
                mongo.login_user(user)
                session['name']=user
                print session['name']
                return redirect("/page/"+user)
            else:
                flash("Username or password is not valid.")
                return redirect("/")
                #return login
        elif (register == "r"):
            return redirect("/register")
        else:
            return render_template("home.html")

@app.route("/page")
@app.route("/page/<user>")
def page(user):
    if not(mongo.exists_user(user)):
        flash("There is no such user.")
        return redirect("/")
    if (mongo.exists_user(user)):
        if(mongo.logged_in(user)=="y"):
            return render_template("user.html", user=user)
        else:
            flash("You don't have permission to view that user's page.")
            return redirect("/")

@app.route("/profile")
@app.route("/profile/<user>")
def profile(user):
    if not(mongo.exists_user(user)):
        flash("There is no such user.")
        return redirect("/")
    if (mongo.exists_user(user)):
        if(session['name']==user):
            ctr = mongo.get_info(user)
            return render_template("profile.html", user=user, ctr=ctr)
        else:
            flash("You don't have permission to view that user's profile.")
            return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout/<user>")
def logout(user=None):
    mongo.logout_user(user)
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
            print session['name']
            mongo.add_user(user,password)
            mongo.login_user(user)
            return redirect("/page/"+user)
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

    
