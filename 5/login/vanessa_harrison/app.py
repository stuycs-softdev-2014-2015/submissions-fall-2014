from flask import Flask, session, redirect, url_for, escape, request, render_template
import mongo

app = Flask(__name__)

@app.route("/")
def index():
    if "username" in session:
        return "YOURE LOGGED IN AS %s" % escape(session["username"])
    else:
        return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
        return "youre already logged in as %s" % escape(session["username"])
    if request.method == "POST":
        #print "sdfsdfsdfds"
        try:
            if request.form["login"] == "Submit":
                if mongo.get(request.form["username"], request.form["password"]) != None:
                    #login successful things
                    session["username"] = request.form["username"]
                    return redirect("/")
                else:
                    return "that's not valid"
        except:
            pass
        if request.form["register"] == "Submit":
            if (request.form["passwordR"] != request.form["passwordR1"]):
                return "passwords dont match"
            if not mongo.add(request.form["usernameR"], request.form["passwordR"], {}):
                #change {} into something
                return "registry successful"
            else:
                return "already registered"
    return render_template("login.html")
    
@app.route("/logout", methods = ["GET", "POST"])
def logout():
    if "username" not in session:
        return "you're not logged in"
    elif request.method == "POST":
        session.pop("username", None)
        session.pop("password", None)
        return redirect("/")
    return render_template("logout.html")

if __name__ == "__main__":
    app.secret_key = "asdf"
    app.run(debug=True)
