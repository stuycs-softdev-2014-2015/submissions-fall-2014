from flask import *

'''
login
logout
register

stufffff
'''

app = Flask(__name__)

@app.route("/")
def index():
    if session['username'] == None:
        return redirect(url_for("login"))
    else:
        return "YOURE LOGGED IN"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
    return render_template("login.html")

@app.route("/logout")
def logout():
    if request.args.get("logout")=="logout":
        session.pop('username', None)
        return redirect(url_for("index"))
    elif session['username'] != None:
        return render_template("logout.html")
    else:
        return "water u doing youa rent in"

if __name__ == "__main__":
    app.secret_key = "asdf"
    app.run(debug=True)
