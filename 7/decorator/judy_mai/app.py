from flask import Flask, session, render_template, request, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = "my secret key"

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return func()
        else:
            return redirect(url_for("login"))
    return wrapper


@app.route("/")
@auth
def home():
    return render_template("index.html")


#@app.route("/register", methods=["GET","POST"])
#def register():
#    return "Register page"
                    
@app.route("/login", methods=["GET","POST"])
def login():
    if "user" in session:
        return redirect(url_for("home"))
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form["user"]
        pw = request.form["pw"]
        if user == "judy" and pw == "mai":
            session["user"] = user
            return redirect(url_for("home"))
        else:
            return render_template("login.html")


@app.route("/logout")
@auth
def logout():
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 1996)
