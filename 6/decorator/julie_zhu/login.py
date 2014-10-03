from flask import Flask
from flask import render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'secretkey'

def auth(func):
    def wrapper(*args):
        if 'username' in session:
            return func()
        else:
            return redirect(url_for("login"))
    return wrapper

@app.route ("/", methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template ('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "name" and password == "pass":
            session["username"] = username
            return redirect("page")
        else:
            return redirect("login")

@app.route("/page")
@auth
def page():
    return render_template("page.html")
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
