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
<style>
button {
   border: 3px solid #0a3c59;
   background: #3e779d;
   background: -moz-linear-gradient(top, #65a9d7, #3e779d);
   padding: 10px 20px;
   text-shadow: #7ea4bd 0 1px 0;
   color: #06426c;
   font-size: 16px;
   font-family: helvetica, serif;
   text-decoration: none;
   vertical-align: middle;
   }
button:hover {
   background: white;
   }
button:active {
   background: gray;
   }
   
h1{
text-shadow: 1px 1px blue;
}

</style>

	<title>Home</title>
	<h1>Welcome to the homepage of Justin and Lev's first software development project.</h1>
	<a href="/about"> <button> Background Information </button> </a>
	<a href="/data"> <button> Raw Data </button> </a>
	<a href="/analysis"> <button> Summary of Analysis </button> </a>
	<a href="/conclusion"> <button> Conclusion </button> </a>
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
