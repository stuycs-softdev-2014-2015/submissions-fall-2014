from flask import  Flask,sessiom,redirect,request,url_for,render_template
from functools import wraps

app=Flask(__name__)
app.secret_key="decorator"

def auth(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not "username" in session:
            return redirect(url_for("Login",x=request.endpoint))
        return func(*args,**kwargs)
    return wrapper

@app.route("/",methods-["GET","POST"])
@auth
def Home():
    if request.method == "POST":
        return redirect(url_for("Logout"))
    return render_template("Home.html")

@app.route("/Login/<x>",methods=["GET","POST"])
def Login(x):
    if request.method == "GET":
        return render_template("Login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == "sabs" and password == "sabs":
            session["username"] = "sabs"
            return redirect(url_for(x))
        return render_template("Login.html")

@app.rout("/Logout")
def Logout():
    session.pop("Username",None)
    return redirect(url_for("Home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
