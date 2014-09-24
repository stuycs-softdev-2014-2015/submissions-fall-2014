# Justin Strauss and Lev Akabas
# Soft Dev Pd 7
# Project 1: Analysis

from flask import Flask, render_template, request
import utils

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	html = """
<head>
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-min.css">

</head>

<style>                                                                                                                                                                            

h1{                                                                                                                                                                                
text-shadow: 1px 1px blue;                                                                                                                                                        text-align: center;
border-color: aqua;
border-style: solid;
border-width: 5px;
background-color: yellow; 
}     
div.overall {background-color: #99FF99; height:300px;}                                                                                                
</style>
                                                                                                                                <title>Home</title>                                                                                                                                                              

<div class="overall">

<div class="pure-menu pure-menu-open pure-menu-horizontal">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/analysis">Analysis</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/conclusion">Conclusion</a></li>
        <li><a href="/data">Raw Data</a></li>
    </ul>
</div>

  
<h1>Welcome to the homepage of Justin and Lev's first software development project.</h1>                                                                                           
</div>

	"""
	return html

@app.route("/about",methods=["GET","POST"])
@app.route("/about/<first>/<last>")
def about(first=None,last=None):
  if request.method=="GET":
    return render_template("about.html")
  else:
    button = request.form['b']
    first  = request.form['first']
    last   = request.form['last']
    valid_name = utils.verify(first,last)
    if button=="Clear" or not(valid_name):
      return render_template("about.html")
    else:
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
