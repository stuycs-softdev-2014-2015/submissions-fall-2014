from flask import Flask, redirect, session, request, url_for, render_template


app = Flask(__name__)
app.secret_key = "Shhhh"

def auth(function):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not "username" in session:
            return redirect(url_for("login", x=request.endpoint))
        return func(*args, **kwargs)
    return wrapper

@app.route("/", methods = ["GET","POST"])
@auth
def homepage():
    if request.method == "POST":
        return redirect(url_for("logout"))
    return render_template("homepage.html")


@app.route("/Login/<x>", methods = ["GET", "POST"])
def login(x):
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == "Dorit" and password == "Rein":
            session['username'] = user
            return redirect(url_for('home'))
        return render_template("login.html")

@app.route("/logout")
@auth
def logout():
    session.pop("user")
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.debug = True
    app.run()
