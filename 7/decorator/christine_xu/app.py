
from flask import Flask
from flask import render_template, session, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "awesome"


@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    if request.method == "POST":
        return redirect(url_for("/Home"));
		
@app.route('/Home', methods = ["POST", "GET"])
def Home():
    if request.method == "GET":
        return render_template('Home.html')




if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)
