from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
import mongo

app = Flask(__name__)

@app.route("/")
def index():
    if "username" in session:
<<<<<<< HEAD
        return "YOURE LOGGED IN AS %s" % escape(session["username"])
=======
        return render_template("loggedin.html", name=escape(session["username"]))
>>>>>>> cf294cd332ca0cae8095e21f5c4a65cb711fdd4a
    else:
        return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
<<<<<<< HEAD
        return "youre already logged in as %s" % escape(session["username"])
    if request.method == "POST":
        #print "sdfsdfsdfds"
=======
        flash("Already logged in as %s" %escape(session["username"]), "error")
        return redirect(url_for("index"))
    elif request.method == "POST":
>>>>>>> cf294cd332ca0cae8095e21f5c4a65cb711fdd4a
        try:
            if request.form["login"] != None:
                if (mongo.get(request.form["username"], request.form["password"]) != None):
                    session["username"] = request.form["username"]
                    flash("Logged in", "success")
                    return redirect(url_for("index"))
                else:
                    print("sdfsdfdf")
                    flash("Invalid Credentials", "error")
        except:
            pass
        try:
            if request.form["register"] != None:
                if (request.form["passwordR"] != request.form["passwordR1"]):
                    flash("Passwords don't match", "error")
                elif not mongo.add(request.form["usernameR"], request.form["passwordR"], {}):
                    flash("Registered", "success")
                else:
                    flash("Already registered", "error")
        except:
            pass
    return render_template("login.html")
    
@app.route("/logout", methods = ["GET", "POST"])
def logout():
    if "username" not in session:
        return render_template("notloggedin.html")
    elif request.method == "POST":
        session.pop("username", None)
        session.pop("password", None)
        return redirect("/")
    return render_template("logout.html")

@app.route("/thankyou")
def thanks():
    if "username" not in session:
        flash("Whoa there, that's for members only.", "error")
        return redirect(url_for("login"))
    else:
        return render_template("thankyou.html", name=escape(session["username"]))

@app.route("/bird")
def bird():
    if "username" not in session:
        flash("Whoa there, that's for members only.", "error")
        return redirect(url_for("login"))
    else:
        return render_template("bird.html")


if __name__ == "__main__":
    app.secret_key = "asdf"
    app.run(debug=True)
