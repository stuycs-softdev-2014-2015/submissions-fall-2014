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
        return redirect(url_for(index))
    return render_template("login.html")
    
@app.route("/logout")
def logout():
    if "username" in session:
        return render_template("logout.html")
    elif request.args.get("logout") == "logout":
        session.pop("username", None)
        return redirect(url_for(index))
    else:
        return "water u dongyou arent in"
    '''
    if request.args.get("logout")=="logout":
        session.pop('username', None)
        return redirect(url_for(index))
    elif session['username'] != None:
        return render_template("logout.html")
    else:
        return "water u doing youa rent in"
    '''

if __name__ == "__main__":
    app.secret_key = "asdf"
    app.run(debug=True)
