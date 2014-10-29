from flask import Flask, render_template, request
#let this be the main file

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        form = request.form

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
