

from flask import Flask, request, session, redirect

USERNAME = "one"
PASSWORD = "two"

app = Flask(__name__)
app.secret_key = "sidfhoiuhro4ewuief"


def auth(func):
    def wrapper():
        if "username" in session:
            return func()
        else:
            return login()
        
    return wrapper
            


@app.route("/")
@auth
def index():
    return 'Hello %s<br /><br /><a href="logout">Logout</a>'%(session["username"])


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["username"] = request.form["username"]
            return redirect("/")
    else:
        return """
Please login.  (Username=one, Password=two)
<form action="login" method="post"><table>
<tr><td>Username</td><td><input type="text" name="username" /></td></tr>
<tr><td>Password</td><td><input type="password" name="password" /></td></tr>
<tr><td colspan="2" style="text-align:center;"><input type="submit" value="Login" /></td></tr>
</table></form>"""

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
