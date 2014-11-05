from flask import Flask, render_template, request, redirect, flash, session
import pymongo, data

app = Flask(__name__)
app.secret_key = "wow"

@app.route("/")
@app.route("/main")
def main():
    button = request.args.get("b",None)
    if button == 'login':
        return login()
    elif button == 'regist':
        return register()
    else:
        return render_template("main.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        user_id = request.form["uname"]
        password = request.form["pw"]
        #check login, send to private page if successful
        if data.check(user_id, password):
            return private1(user_id)
        else:
            flash("Invalid Username or Password!")
            return redirect("/login")
    
@app.route("/logout")
def logout():
    button = request.args.get("b",None)
    login = False
    if button == 'home':
        flash("Successfully logged out")
        return main()
    else:
        return render_template("logout.html")
    
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user_id = request.form["uname"]
        password = request.form["pw"]
        #add new data to db, if taken dont do anything
        if data.addNew(user_id, password):
            flash("Successfully registered!")
            return redirect("/login")
        else:
            flash("Sorry, the username is already taken.")
            return redirect("/register")


@app.route("/private1")
#private pages
def private1(user=None):
    if user==None:
        return main()
    else:
        button = request.args.get("b",None)
        if button == None:
            return render_template("private1.html",user=user)
        else:
            return private2(user)

@app.route("/private2")
#private pages
def private2(user=None):
    if user==None:
        return main()
    else:
        button = request.args.get("b",None)
        if button == None:
            return render_template("private2.html",user=user)
        else:
            return private1(user)

@app.route("/public")
#public pages
def public():
    button = request.args.get("b", None)
    if button == 'home':
        return redirect("/main")
    else:
        return render_template("public.html")

#main
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1234)
