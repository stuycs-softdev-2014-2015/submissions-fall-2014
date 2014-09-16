# Justin Strauss
# Soft Dev Pd 7
# Project 1: Analysis

from flask import Flask, render_template

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	html = """
	<h1>Welcome to the homepage of Justin's first software development project.</h1>
	<button><a href="/about">About My Project</a></button>
	"""
	return html

@app.route("/about")
@app.route("/about/<name>")
def about(name=None):
	return render_template("about.html",name=name)

@app.route("/analyze")
def analyze():
	return render_template("analyze.html")

if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run(port=4242)