from flask import Flask, render_template, request
import utils
import writing 

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
            return render_template("create.html")

@app.route("/love1", methods=["GET", "POST"])
def love1():
    if request.method=="GET":
        return render_template("love1.html")
    else:
        button = request.form["b"]
        f = open("love1.txt" , "r")
        s = f.read()
        f.close()
        Q1 = request.form['Q1']
        Q2 = request.form['Q2']
        Q3 = request.form['Q3']
        Q4 = request.form['Q4']
        Q5 = request.form['Q5']
        t = s.split(" ")
        for n in t:
            if n == "Q1":
                i = t.index(n)
                t[i] = Q1
            elif n == "Q2":
                i = t.index(n)
                t[i] = Q2
            elif n == "Q3":
                i = t.index(n)
                t[i] = Q3
            elif n == "Q4":
                i = t.index(n)
                t[i] = Q4
            elif n == "Q5":
                i = t.index(n)
                t[i] = Q5
                poem = " ".join(t)
        if button==None:
            return render_template("love1.html")
        else:
            return render_template("poem.html", p=poem)

def writing():
    Q1 = request.form['Q1']
    Q2 = request.form['Q2']
    Q3 = request.form['Q3']
    Q4 = request.form['Q4']
    Q5 = request.form['Q5']
    t = s.split(" ")
    for n in t:
        if n == "Q1":
	    i = t.index(n)
            t[i] = Q1
        elif n == "Q2":
	    i = t.index(n)
            t[i] = Q2
        elif n == "Q3":
	    i = t.index(n)
            t[i] = Q3
        elif n == "Q4":
	    i = t.index(n)
            t[i] = Q4
        elif n == "Q5":
	    i = t.index(n)
            t[i] = Q5
    poem = " ".join(t)
    return poem


if __name__ == '__main__':
    app.debug = True
    app.run()
