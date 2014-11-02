from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method=="POST":
        return render_template("login.html")
    
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method =="GET":
        return render_template("register.html")

@app.route("/logout", methods = ["GET"])
def logout():
    pass

if (__name__=='__main__'):
    app.debug=True
    app.run()
