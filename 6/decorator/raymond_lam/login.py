from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory

app = Flask(__name__)
app.secret_key = "asdfghjkl"

def auth(func):
	def wrapper(*args):
		if "username" in session:
			return func()
		else:
			return redirect("/login")
	return wrapper

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		if username == "lang" and password == "jai":
			session["username"] = username
			return redirect("/secret1")
		else:
			return redirect("/secret2")

@app.route("/secret1")
@auth
def secret1():
	return render_template("secret1.html")

@app.route("/secret2")
def secret2():
	return render_template("secret2.html")

@app.route("/logout")
def logout():
	session.pop("username", None)
	return redirect("/login")

if __name__ == "__main__":
	app.debug = True
	app.run()