from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request, send_from_directory
from functools import wraps

app = Flask(__name__)
app.secret_key = "SUPERSECRETKEY"
app.jinja_env.line_statement_prefix = "poo"

def auth(func, *args, **kwargs):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if "username" in session:
			return func()
		else:
			return index("Log the f*** in first")
	return wrapper

@app.route("/")
def index(msg = None):
	return render_template("index.html", msg=msg)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		if username == "roger" and password == "awesome":
			session["username"] = username
			return index("You've logged the f*** in!")
		else:
			return index("Wrong, loser")

@app.route("/profile")
@auth
def profile():
	return render_template("profile.html")

@app.route("/logout")
@auth
def logout():
	session.pop("username")
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug = True)
