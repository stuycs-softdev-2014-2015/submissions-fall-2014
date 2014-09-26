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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("love1.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/love2", methods=["GET", "POST"])
def love2():
    if request.method=="GET":
        return render_template("love2.html")
    else:
        button = request.form["b"]
        f = open("love2.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("love2.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/love3", methods=["GET", "POST"])
def love3():
    if request.method=="GET":
        return render_template("love3.html")
    else:
        button = request.form["b"]
        f = open("love3.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("love3.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/love4", methods=["GET", "POST"])
def love4():
    if request.method=="GET":
        return render_template("love4.html")
    else:
        button = request.form["b"]
        f = open("love4.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("love4.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/pain1", methods=["GET", "POST"])
def pain1():
    if request.method=="GET":
        return render_template("pain1.html")
    else:
        button = request.form["b"]
        f = open("pain1.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("pain1.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/pain2", methods=["GET", "POST"])
def pain2():
    if request.method=="GET":
        return render_template("pain2.html")
    else:
        button = request.form["b"]
        f = open("pain2.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("pain2.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/pain3", methods=["GET", "POST"])
def pain3():
    if request.method=="GET":
        return render_template("pain3.html")
    else:
        button = request.form["b"]
        f = open("pain3.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("pain3.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/pain4", methods=["GET", "POST"])
def pain4():
    if request.method=="GET":
        return render_template("pain4.html")
    else:
        button = request.form["b"]
        f = open("pain4.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("pain4.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/life1", methods=["GET", "POST"])
def life1():
    if request.method=="GET":
        return render_template("life1.html")
    else:
        button = request.form["b"]
        f = open("life1.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("life1.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/life2", methods=["GET", "POST"])
def life2():
    if request.method=="GET":
        return render_template("life2.html")
    else:
        button = request.form["b"]
        f = open("life2.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("life2.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/life3", methods=["GET", "POST"])
def life3():
    if request.method=="GET":
        return render_template("life3.html")
    else:
        button = request.form["b"]
        f = open("life3.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("life3.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/life4", methods=["GET", "POST"])
def life4():
    if request.method=="GET":
        return render_template("life4.html")
    else:
        button = request.form["b"]
        f = open("life4.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("life4.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/death1", methods=["GET", "POST"])
def death1():
    if request.method=="GET":
        return render_template("death1.html")
    else:
        button = request.form["b"]
        f = open("death1.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("death1.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/death2", methods=["GET", "POST"])
def death2():
    if request.method=="GET":
        return render_template("death2.html")
    else:
        button = request.form["b"]
        f = open("death2.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("death2.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/death3", methods=["GET", "POST"])
def death3():
    if request.method=="GET":
        return render_template("death3.html")
    else:
        button = request.form["b"]
        f = open("death3.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("death3.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/death4", methods=["GET", "POST"])
def death4():
    if request.method=="GET":
        return render_template("death4.html")
    else:
        button = request.form["b"]
        f = open("death4.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("death4.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/experiences1", methods=["GET", "POST"])
def experiences1():
    if request.method=="GET":
        return render_template("experiences1.html")
    else:
        button = request.form["b"]
        f = open("experiences1.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("experiences1.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/experiences2", methods=["GET", "POST"])
def experiences2():
    if request.method=="GET":
        return render_template("experiences2.html")
    else:
        button = request.form["b"]
        f = open("experiences2.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("experiences2.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/experiences3", methods=["GET", "POST"])
def experiences3():
    if request.method=="GET":
        return render_template("experiences3.html")
    else:
        button = request.form["b"]
        f = open("experiences3.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("experiences3.html")
        else:
            return render_template("poem.html", p=poem)

@app.route("/experiences4", methods=["GET", "POST"])
def experiences4():
    if request.method=="GET":
        return render_template("experiences4.html")
    else:
        button = request.form["b"]
        f = open("experiences4.txt" , "r")
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
            else:
                i = None
        poem = " ".join(t)
        if button==None:
            return render_template("experiences4.html")
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
