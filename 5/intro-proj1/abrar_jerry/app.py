from flask import Flask, render_template
import os

app = Flask(__name__)

def conv (filename):
    f = open(filename)
    s = f.readlines()
    s= "".join(s)
    s = s.split("\n")
    datalist = s[:len(s)-1] 
    return datalist

def makeTable (x):
    m = "<center><table> \n<table border='2'>\n"
    for info in x:
        m+= "<tr>"
        splitted = info.split(",")
        count = 0
        while count < len(splitted):
            m+= "<td> " + splitted[count] + " </td>"
            count += 1
        m+= "</tr> \n"
    m+= "</table> \n</center>"
    return m

@app.route("/miami")
def help1(table=None):
    return render_template("miami.html",
		table=makeTable(conv("heat2011-12")) )

@app.route("/dallas")
def help2(table=None):
    return render_template("dallas.html",
		table=makeTable(conv("mavs2010-11")) )

@app.route("/la")
def help3(table=None):
    return render_template("la.html",
		table=makeTable(conv("lakers2009-10")) )

@app.route("/home")
@app.route("/")
def data():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=1061)
    
