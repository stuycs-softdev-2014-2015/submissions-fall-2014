# Justin Strauss and Lev Akabas
# Soft Dev Pd 7
# Project 1: Analysis

from flask import Flask, render_template

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	html = """
	<title>Home</title>
	<h1>Welcome to the homepage of Justin and Lev's first software development project.</h1>
	<button><a href="/about">Background Information</a></button>
	<button><a href="/data">Raw Data</a></button>
	<button><a href="/analysis">Summary of Analysis</a></button>
	<button><a href="/conclusion">Conclusion</a></button>
	"""
	return html

@app.route("/about")
@app.route("/about/<first>/<last>")
def about(first=None,last=None):
	return render_template("about.html",first=first,last=last)

@app.route("/conclusion")
def conclusion():
	return render_template("conclusion.html")

@app.route("/data")
def data():
	return render_template("data.html")

@app.route("/analysis")
def analysis():
	return render_template("analysis.html")

if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run(port=4242)