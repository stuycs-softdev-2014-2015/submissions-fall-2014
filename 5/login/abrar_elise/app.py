from flask import Flask, render_template
from pymongo import Connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/form", methods=["GET", "POST"])
def form():

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=1847)
