from flask import Flask, render_template
from pymongo import Connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pform", methods=["GET", "POST"])
def pform():
    if request.method == "GET":
        return render_template("pform.html")
    else:
        uname = request.form['uname']
        pword = request.form['pass']
        print "uname: " + uname + "\npass" + pword


                              
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=1847)
