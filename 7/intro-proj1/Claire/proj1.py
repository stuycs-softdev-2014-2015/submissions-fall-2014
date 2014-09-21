from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['b']
        uname = request.form['uname']
        pword = request.form['pword']
        valid_user = utils.authenticate(uname,pword)
        if button=="cancel" or not(valid_user):
            return render_template("login.html")
        else:
            return render_template("welcome.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
