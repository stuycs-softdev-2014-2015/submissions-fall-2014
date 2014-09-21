import random
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cssdemo")
def cssdemo():
    return render_template("cssdemo.html")

if __name__=="__main__":
    app.debug=True
    app.run()

