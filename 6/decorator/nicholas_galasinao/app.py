from flask import Flask, render_template, request, session, url_for, redirect

app = Flask( __name__ )

def auth(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        if "username" in session:
            return func()
        else:
            return redirect()
    return wrapper


@app.route("/")
@auth()
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        username=request.form["username"]#.encode("ascii","ignore")
        password=request.form["password"]#.encode("ascii","ignore")
        if username == "nick" and password == "1234":
            session[username] = request.form[username]
            return redirect("/")
        
@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=7777)
