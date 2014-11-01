from flask import Flask, render_template, request, redirect
import mongo

app = Flask(__name__)

@app.route("/")
def home():
    user = request.args.get("user")
    password = request.args.get("pwd")
    login = request.args.get("login")
    register = request.args.get("register")
    if (login == "Login" and user != "" and password != ""):
        print mongo.get_password(user)
        if (password == mongo.get_password(user)):
            return "success"
        else:
            return "Username or password is not valid"
        #return login
    elif (register == "r"):
        return redirect("/register")
    else:
        return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run()

    
