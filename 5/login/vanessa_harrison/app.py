from flask import Flask, session, redirect, url_for, escape, request, render_template

'''
login
logout
register

stufffff
'''

app = Flask(__name__)

@app.route("/")
def index():
    if "username" in session:
        return "YOURE LOGGED IN AS %s" %escape(session["username"])
    else:
        return "this is the home page which means you arent logged in"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
        return "youre already logged in as %s" %escape(session["username"])
    elif request.method == "POST":
        session["username"] = request.form["username"]
        return redirect("/")
    return render_template("login.html")
    
@app.route("/logout", methods = ["GET", "POST"])
def logout():
    if "username" not in session:
        return "you're not logged in"
    elif request.method == "POST":
        session.pop("username", None)
        return redirect("/")
    return render_template("logout.html")

if __name__ == "__main__":
    app.secret_key = "asdf"
    app.run(debug=True)
