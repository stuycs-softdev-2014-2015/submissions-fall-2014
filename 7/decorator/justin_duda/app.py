from functools import wraps
from flask import Flask, session, redirect, request
from flask import url_for, render_template

app = Flask(__name__)
app.secret_key = "secret secrets"


def auth(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		# user logged in
		if "user" in session:
			# redirect to desired page
			# i.e. continue with function
			return func(*args,**kwargs)
		# user not logged in
		else:
			# redirect to login page
			return redirect(url_for("login"))
	return wrapper


@app.route('/', methods=["GET","POST"] )
@auth
def index():
	if request.method == "GET":
		return render_template("index.html")
	else: #request.method == POST
		return redirect(url_for("logout"))

@app.route('/login', methods=["GET","POST"] )
def login():
	if request.method == "GET":
		return render_template("login.html")
	else: #request.method == "POST"
		usr = request.form['username']
		pwd = request.form['password']
		if usr == "justin" and pwd == "duda":
			session["user"] = "justin"
			return redirect(url_for("index"))
		# login failed
		else:
			return render_template("login.html")

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("index"))

		

if __name__ == "__main__":
	app.debug = True
	app.run()

