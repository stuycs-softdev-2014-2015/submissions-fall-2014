"""
	Sample Flask application that demonstrates use of an authentication
	decorator, used to display pages only when a user is logged in.
"""

from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request, send_from_directory
from functools import wraps

app = Flask(__name__)
app.secret_key = "0xdeadbeef"
app.jinja_env.line_statement_prefix = "="

def auth(func, *args, **kwargs):
	"""
	Execute function if the user is logged in;
	otherwise, redirect to the home page.
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		if "username" in session:
			return func()
		else:
			return index("You must log in!")
	return wrapper

@app.route("/")
def index(msg = None):
	"""
	Return home page.
	"""
	return render_template("index.html", msg = msg)

@app.route("/login", methods=["GET", "POST"])
def login():
	"""
	Handle attempted user login.
	"""
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		if authenticate(username, password):
			session["username"] = username
			return index("You've logged in successfully!")
		else:
			return index("That user does not exist.")

@app.route("/profile")
@auth
def profile():
	"""
	Return page displaying user's profile.
	"""
	return render_template("profile.html")

@app.route("/logout")
@auth
def logout():
	"""
	Log user out of application.
	"""
	session.pop("username")
	return redirect(url_for("index"))

def authenticate(username, password):
	"""
	Authenticate username and password combination.
	"""
	return username == "sevko" and password == "flask"

if __name__ == "__main__":
	app.run(debug = True)
