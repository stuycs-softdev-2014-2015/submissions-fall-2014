from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory

app = Flask(__name__)
app.secret_key = "abcd"
app.jinja_env.line_statement_prefix = "="

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func()
        else:
            return index("Log In or Leave!")
    return wrapper

@app.route('/')
def index(message = None):
    return render_template("index.html", message = message)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == "arfan" and password == "rehab":
            session["username"] = username
            return index("Successful login!")
        else:
            return index("Nope!")
@auth
@app.route("/mystery")
def mystery():
    return render_template("mystery.html")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True