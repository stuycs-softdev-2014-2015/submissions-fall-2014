from functools import wraps
from flask import Flask, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "fluffy unicorns"

def auth(func):
  @wraps(func)
  def inner():
    if "username" in session:
      return func()
    else:
      return redirect("/login")
  return inner

@app.route("/")
def home():
  return '<a href="/login">login</a> <a href="/logout">logout</a> <a href="/test">test</a>'

@app.route("/logout")
def logout():
  if "username" in session:
    session.pop("username")
  return redirect(url_for("home"))

@app.route("/login")
def login():
  if not "username" in session:
    session["username"] = "bananas"
  return redirect(url_for("home"))

@app.route("/test")
@auth
def test():
  return "You're logged in, yo"

if __name__ == "__main__":
  app.run(debug=True)
