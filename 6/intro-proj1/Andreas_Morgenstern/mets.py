from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        button = request.form["b"]
        uname = request.form["uname"]
        pword = request.form['pword']
        if button=="cancel" or uname=="":
            return render_template("login.html")
        else:
            inStream = open("data01.csv",'r')
            data = inStream.read()
            inStream.close()
            rows = data.split("\n")
            for i in range(0,len(rows)):
                rows[i] = rows[i].split(",")
            return render_template("data.html", info = rows, name = uname)

@app.route("/")
def home():
     return redirect(url_for('login'))

@app.route("/analysis")
def analysis():
    inStream = open("averages_hw25.csv","r")
    data = inStream.read()
    inStream.close()
    rows = data.split("\n")
    for i in range(0,len(rows)):
        rows[i] = rows[i].split(",")
    return render_template("analysis.html", info=rows)
if __name__=="__main__":
    app.debug=True
    app.run() 

    
