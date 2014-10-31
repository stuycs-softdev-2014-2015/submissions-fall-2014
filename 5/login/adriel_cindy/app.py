from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    login = request.args.get("login")
    register = request.args.get("register")
    if (login == "l"):
        if 
    if (register == "r"):
        return redirect("/register")
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run()

    
